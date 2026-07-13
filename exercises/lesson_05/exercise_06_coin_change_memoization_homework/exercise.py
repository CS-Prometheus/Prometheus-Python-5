"""Exercise 06 — Minimum Coin Change (Homework)"""

from functools import lru_cache


def coin_change(coins, amount):
    """Return the fewest coins needed to make amount, or -1 if impossible."""
    coins = tuple(coins)

    @lru_cache(maxsize=None)
    def dp(remaining):
        # TODO: base case -- remaining == 0
        # TODO: base case -- remaining < 0 (return something that never wins a min())
        # TODO: try every coin, take the best (fewest coins) option
        pass

    # TODO: call dp(amount) and convert an "impossible" result into -1
    pass
