# DSA Journey

> Daily data-structures & algorithms practice — building toward an AI/ML engineering role.
> This README's stats and problem log update **automatically** on every push. 🤖

<!-- Badges auto-update via the workflow -->
<!-- BADGES:START -->
![Problems Solved](https://img.shields.io/badge/solved-15-blue)
![Easy](https://img.shields.io/badge/easy-4-brightgreen)
![Medium](https://img.shields.io/badge/medium-11-orange)
![Hard](https://img.shields.io/badge/hard-0-red)
![Last Updated](https://img.shields.io/badge/updated-2026--06--02-lightgrey)
<!-- BADGES:END -->

---

## Progress

<!-- STATS:START -->
**Total solved:** 15  |  🟢 Easy 4 · 🟠 Medium 11 · 🔴 Hard 0

| Topic | Solved |
|---|---|
| Arrays N Hashing | 9 |
| Two Pointers | 3 |
| Stack | 2 |
| Sliding Window | 1 |
<!-- STATS:END -->

---

## Repository structure

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

## Problem log

<!-- LOG:START -->
| Problem | Difficulty | Topic | Code |
|---|---|---|---|
| [853. Car Fleet](https://leetcode.com/problems/car-fleet/) | Medium | Stack | [link](solutions/stack/car_fleet.py) |
| [739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) | Medium | Stack | [link](solutions/stack/daily_temperatures.py) |
| [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/) | Medium | Arrays N Hashing | [link](solutions/array_n_hashing/group_anagrams.py) |
| [424. Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) | Medium | Sliding Window | [link](solutions/sliding_window/longest_repeating_char_replacement.py) |
| [36. Valid Sudoku](https://leetcode.com/problems/valid-sudoku/) | Medium | Arrays N Hashing | [link](solutions/array_n_hashing/valid_sudoku.py) |
| [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | Medium | Arrays N Hashing | [link](solutions/array_n_hashing/top_k_freq_elems.py) |
| [271. Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/) | Medium | Arrays N Hashing | [link](solutions/array_n_hashing/string_encode_decode.py) |
| [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/) | Easy | Arrays N Hashing | [link](solutions/array_n_hashing/is_anagram.py) |
| [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | Medium | Arrays N Hashing | [link](solutions/array_n_hashing/product_of_arr_except_self.py) |
| [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | Easy | Arrays N Hashing | [link](solutions/array_n_hashing/contains_duplicate.py) |

<div style='height: 400px; overflow-y: auto;'>

| Problem | Difficulty | Topic | Code |
|---|---|---|---|
| [167. Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | Medium | Two Pointers | [link](solutions/two_pointers/two_sum_II.py) |
| [15. 3Sum](https://leetcode.com/problems/3sum/) | Medium | Two Pointers | [link](solutions/two_pointers/three_sum.py) |
| [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | Medium | Arrays N Hashing | [link](solutions/array_n_hashing/longest_consecutive_sequence.py) |
| [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | Easy | Two Pointers | [link](solutions/two_pointers/is_palindrome.py) |
| [1. Two Sum](https://leetcode.com/problems/two-sum/) | Easy | Arrays N Hashing | [link](solutions/array_n_hashing/two_sum.py) |

</div>
<!-- LOG:END -->

---

## Local usage

```bash
# add a solution, then regenerate the README locally (optional — CI does this too)
python scripts/update_readme.py

# run a quick sanity test on a solution
python solutions/arrays/two_sum.py
```
