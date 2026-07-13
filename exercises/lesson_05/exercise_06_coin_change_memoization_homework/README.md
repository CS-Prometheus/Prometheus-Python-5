# Exercise 06 — Minimum Coin Change (Homework)

Write `coin_change(coins, amount)` that returns the minimum number of
coins from the given denominations needed to make exactly `amount`, or
`-1` if it's impossible.

Use a memoized inner recursive function `dp(remaining)`:

- `dp(0) == 0`
- `dp(remaining)` tries every coin, taking the minimum of
  `1 + dp(remaining - coin)` over all coins that don't make `remaining`
  negative.

## Where to work

Edit `exercise.py` wherever you see `# TODO`. Don't edit `test_exercise.py`.
