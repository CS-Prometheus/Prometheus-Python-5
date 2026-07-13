# Exercise 02 — Memoized Fibonacci (Classwork)

## Part A — Naive recursion

Write `fib(n)` that returns `fib(n - 1) + fib(n - 2)`, with base cases for
`n == 0` and `n == 1`.

## Part B — Memoize it two ways

1. `fib_cached(n)` — the same logic, but decorated with
   `@lru_cache(maxsize=None)` from `functools`.
2. `fib_memo(n, memo=None)` — the same logic again, this time memoized by
   hand with a dictionary. (Careful with mutable default arguments — handle
   `memo=None` and create the dict inside the function.)

## Part C — Explain it

In the docstring at the top of `exercise.py`, write a few sentences
explaining why `fib(35)` is essentially instant once memoized but takes a
very long time without it. Mention how many times the naive version
recomputes the same value.

## Where to work

Edit `exercise.py` wherever you see `# TODO`. Don't edit `test_exercise.py`.
