#!/usr/bin/env python3
"""Regenerate the auto-maintained sections of README.md from solution headers."""
import glob, re
from collections import Counter, defaultdict
from datetime import datetime, timezone

SOLUTION_GLOBS = [
    "Data Structures & Algorithms/**/*.py",
    "solutions/**/*.py",
]
README = "README.md"
FIELDS = ["Problem", "Difficulty", "Topic", "Link"]
DIFF_ORDER = {"Easy": 0, "Medium": 1, "Hard": 2}

def parse(path):
    with open(path, encoding="utf-8") as f:
        head = f.read(1000)
    data = {}
    for field in FIELDS:
        m = re.search(rf"{field}:\s*(.+)", head)
        data[field] = m.group(1).strip() if m else ""
    data["path"] = path.replace("\\", "/")
    return data

def replace_block(text, name, new):
    return re.sub(
        rf"(<!-- {name}:START -->)(.*?)(<!-- {name}:END -->)",
        rf"\1\n{new}\n\3",
        text, flags=re.DOTALL,
    )

def main():
    files = []
    for pattern in SOLUTION_GLOBS:
        files += glob.glob(pattern, recursive=True)
    probs = [parse(p) for p in files]
    probs = [p for p in probs if p["Problem"]]
    diff = Counter(p["Difficulty"] for p in probs)
    total = len(probs)
    today = datetime.now(timezone.utc).strftime("%Y--%m--%d")  # -- escapes for shields.io

    badges = "\n".join([
        f"![Problems Solved](https://img.shields.io/badge/solved-{total}-blue)",
        f"![Easy](https://img.shields.io/badge/easy-{diff.get('Easy',0)}-brightgreen)",
        f"![Medium](https://img.shields.io/badge/medium-{diff.get('Medium',0)}-orange)",
        f"![Hard](https://img.shields.io/badge/hard-{diff.get('Hard',0)}-red)",
        f"![Last Updated](https://img.shields.io/badge/updated-{today}-lightgrey)",
    ])

    # per-topic counts
    topic_counts = defaultdict(int)
    for p in probs:
        for t in (x.strip() for x in p["Topic"].split(",") if x.strip()):
            topic_counts[t] += 1
    stats = (f"**Total solved:** {total}  |  "
             f"🟢 Easy {diff.get('Easy',0)} · 🟠 Medium {diff.get('Medium',0)} · 🔴 Hard {diff.get('Hard',0)}\n\n")
    if topic_counts:
        stats += "| Topic | Solved |\n|---|---|\n"
        stats += "\n".join(f"| {t} | {c} |"
                           for t, c in sorted(topic_counts.items(), key=lambda x: -x[1]))

    # problem log, sorted by difficulty (Easy → Medium → Hard), then by problem number
    probs.sort(key=lambda p: (DIFF_ORDER.get(p["Difficulty"], 999), -int(re.search(r'\d+', p["Problem"]).group() if re.search(r'\d+', p["Problem"]) else 0)))
    if probs:
        log = f"<div style='height: 400px; overflow-y: auto;'>\n\n"
        log += "| Problem | Difficulty | Topic | Code |\n|---|---|---|---|\n"
        log += "\n".join(
            f"| [{p['Problem']}]({p['Link']}) | {p['Difficulty']} "
            f"| {p['Topic']} | [link]({p['path']}) |" for p in probs)
        log += "\n\n</div>"
    else:
        log = "*No solutions yet.*"

    with open(README, encoding="utf-8") as f:
        text = f.read()
    text = replace_block(text, "BADGES", badges)
    text = replace_block(text, "STATS", stats)
    text = replace_block(text, "LOG", log)
    with open(README, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Updated README: {total} problems.")

if __name__ == "__main__":
    main()