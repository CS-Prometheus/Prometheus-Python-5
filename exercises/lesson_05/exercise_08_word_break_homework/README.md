# Exercise 08 — Word Break (Homework)

Write `can_segment(s, word_set)` that returns `True` if the string `s` can
be split into a sequence of one or more words that are all present in
`word_set` (a Python `set` of allowed words), and `False` otherwise.

For example, `can_segment('pythoncode', {'python', 'code'})` should return
`True`.

- Try every prefix of `s`; if that prefix is in `word_set`, recursively
  check whether the remaining suffix can also be segmented.
- Use `word in word_set` for an `O(1)` average membership check rather
  than looping over the set.
- Add memoization keyed on the remaining substring (a manual dictionary
  works well here, since `@lru_cache` needs hashable arguments — strings
  already are, but this exercise wants you to practice the manual-dict
  approach) so the same suffix is never re-checked from scratch.

## Where to work

Edit `exercise.py` wherever you see `# TODO`. Don't edit `test_exercise.py`.
