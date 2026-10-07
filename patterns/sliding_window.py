def longest_unique_substring(s):
    """Length of the longest substring without repeating characters.

    Keep a window [left, right]; when a char repeats, jump left past its last index.
    Time O(n), space O(min(n, alphabet)).
    """
    last, left, best = {}, 0, 0
    for right, ch in enumerate(s):
        if ch in last and last[ch] >= left:
            left = last[ch] + 1
        last[ch] = right
        best = max(best, right - left + 1)
    return best
