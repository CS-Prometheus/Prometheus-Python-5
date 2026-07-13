"""Exercise 08 — Word Break (Homework)"""


def can_segment(s, word_set):
    """Return True if s can be split into words that are all in word_set."""
    memo = {}

    def helper(remaining):
        # TODO: base case -- remaining == '' means we successfully segmented everything
        # TODO: check memo before recomputing
        # TODO: try every prefix of `remaining`; if it's in word_set, recurse on the rest
        # TODO: store the result in memo before returning it
        pass

    return helper(s)
