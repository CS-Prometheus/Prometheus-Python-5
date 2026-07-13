# Exercise 03 — Fast Exponentiation (Classwork)

Write `power(x, n)` that computes `x` raised to the power `n` in
`O(log n)` time using divide and conquer:

- Base case: `power(x, 0)` returns `1`.
- If `n` is even: `x**n == (x**(n // 2)) ** 2`.
- If `n` is odd: `x**n == x * power(x, n - 1)`.

In the docstring at the top of `exercise.py`, write one sentence explaining
why halving `n` each time gives `O(log n)` calls instead of `O(n)`.

## Where to work

Edit `exercise.py` wherever you see `# TODO`. Don't edit `test_exercise.py`.
