# Exercise 05 — Count Unique Grid Paths (Homework)

Write `count_paths(m, n)` that returns the number of unique paths through
an `m x n` grid, moving only right or down, starting at the top-left
corner and ending at the bottom-right corner.

- Base case: if `m == 1` or `n == 1`, there is exactly one path.
- Recursive case: `count_paths(m, n) == count_paths(m - 1, n) + count_paths(m, n - 1)`.

Decorate your function with `@lru_cache` (from `functools`) so repeated
subproblems aren't recomputed.

## Where to work

Edit `exercise.py` wherever you see `# TODO`. Don't edit `test_exercise.py`.
