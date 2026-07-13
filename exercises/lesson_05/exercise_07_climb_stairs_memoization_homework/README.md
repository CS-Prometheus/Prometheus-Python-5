# Exercise 07 — Climbing Stairs (Homework)

Write `climb_stairs(n)` that returns the number of distinct ways to climb
a staircase of `n` steps if you can take 1, 2, or 3 steps at a time.

- Base cases: `climb_stairs(0) == 1` (one way to already be at the top —
  do nothing), and `climb_stairs` of a negative number is `0`.
- Recursive case: `climb_stairs(n) == climb_stairs(n - 1) + climb_stairs(n - 2) + climb_stairs(n - 3)`.

Memoize it (with `@lru_cache` or a dictionary) and report `climb_stairs(20)`.

## Where to work

Edit `exercise.py` wherever you see `# TODO`. Don't edit `test_exercise.py`.
