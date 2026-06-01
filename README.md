# 🧠 DSA Journey

> Daily data-structures & algorithms practice — building toward an AI/ML engineering role.
> This README's stats and problem log update **automatically** on every push. 🤖

<!-- Badges auto-update via the workflow -->
<!-- BADGES:START -->
![Problems Solved](https://img.shields.io/badge/solved-0-blue)
![Easy](https://img.shields.io/badge/easy-0-brightgreen)
![Medium](https://img.shields.io/badge/medium-0-orange)
![Hard](https://img.shields.io/badge/hard-0-red)
![Last Updated](https://img.shields.io/badge/updated-never-lightgrey)
<!-- BADGES:END -->

---

## 📊 Progress

<!-- STATS:START -->
*No solutions yet.*
<!-- STATS:END -->

---

## 📁 Repository structure

```
.
├── solutions/            # all solutions, grouped by topic
│   ├── arrays_n_hashings/
│   ├── two_pointers/
│   ├── sliding_window/
│   ├── linked_lists/
│   ├── stacks_queues/
│   ├── binary_search/
│   ├── trees/
│   ├── heaps/
│   ├── graphs/
│   └── dynamic_programming/
├── scripts/
│   └── update_readme.py  # regenerates the auto sections
├── .github/workflows/
│   └── update-readme.yml # runs the script on each push
└── README.md
```

---

## ✍️ Solution file convention

Every solution is a `.py` file inside the matching topic folder, and **must start with this header** so the auto-updater can index it:

```python
"""
Problem: 1. Two Sum
Difficulty: Easy
Topic: Arrays, Hashing
Link: https://leetcode.com/problems/two-sum/
Date: 2026-06-02
"""

def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        if target - n in seen:
            return [seen[target - n], i]
        seen[n] = i
```

**Header fields:** `Problem`, `Difficulty` (Easy/Medium/Hard), `Topic` (comma-separated), `Link`, `Date` (YYYY-MM-DD). Miss the header and the file simply won't appear in the log — no other harm done.

---

## 📒 Problem log

<!-- LOG:START -->
*The full table of solved problems appears here automatically, newest first.*
<!-- LOG:END -->

---

## 🚀 Local usage

```bash
# add a solution, then regenerate the README locally (optional — CI does this too)
python scripts/update_readme.py

# run a quick sanity test on a solution
python solutions/arrays/two_sum.py
```

---

## 🎯 Goal & cadence

One morning block per weekday (9–10 AM), ramping easy → medium → hard from June through September. Consistency over volume — a missed day is skipped, never doubled.

*This file is partly machine-maintained. Hand-edit anything outside the `START`/`END` markers freely; content between them is overwritten on each push.*