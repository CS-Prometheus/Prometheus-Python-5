# Exercise 01 — Call Stack Tracing (Classwork)

Write two small recursive functions and practice tracing exactly how the
call stack grows and unwinds.

## Part A — `factorial(n)`

- Base case: `n == 0` returns `1`.
- Recursive case: returns `n * factorial(n - 1)`.

## Part B — `rec_sum(lst)`

- Base case: an empty list returns `0`.
- Recursive case: returns the first element plus `rec_sum` of the rest of
  the list.

## Part C — Trace it

In the docstring at the top of `exercise.py`, write out, line by line,
every call that gets pushed onto the stack for `factorial(5)` and for
`rec_sum([1, 2, 3, 4])`, and the order in which each call returns. Use the
same format we used on the whiteboard in class.

## Where to work

Edit `exercise.py` wherever you see `# TODO`. Don't edit `test_exercise.py`.
