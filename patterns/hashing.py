from collections import defaultdict


def two_sum(nums, target):
    """Return indices of the two numbers adding to target.

    Intuition: store each value's index; for x, look up target - x.
    Time O(n), space O(n). Edge cases: duplicates (e.g. [3, 3]), no answer.
    """
    seen = {}
    for i, x in enumerate(nums):
        if target - x in seen:
            return [seen[target - x], i]
        seen[x] = i
    return []


def group_anagrams(words):
    """Group words that are anagrams. Key = sorted letters. Time O(n k log k)."""
    groups = defaultdict(list)
    for w in words:
        groups["".join(sorted(w))].append(w)
    return list(groups.values())
