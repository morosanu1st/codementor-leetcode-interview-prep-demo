def is_palindrome(s):
    """Valid palindrome ignoring non-alphanumerics and case. Time O(n), space O(1)."""
    i, j = 0, len(s) - 1
    while i < j:
        if not s[i].isalnum():
            i += 1
        elif not s[j].isalnum():
            j -= 1
        elif s[i].lower() != s[j].lower():
            return False
        else:
            i, j = i + 1, j - 1
    return True


def max_area(heights):
    """Container with most water: move the shorter wall inward. Time O(n)."""
    i, j, best = 0, len(heights) - 1, 0
    while i < j:
        best = max(best, (j - i) * min(heights[i], heights[j]))
        if heights[i] < heights[j]:
            i += 1
        else:
            j -= 1
    return best
