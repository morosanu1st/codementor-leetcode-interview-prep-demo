import unittest

from patterns.hashing import two_sum, group_anagrams
from patterns.two_pointers import is_palindrome, max_area
from patterns.sliding_window import longest_unique_substring
from patterns.binary_search import search_rotated, min_eating_speed
from patterns.graphs import num_islands, shortest_path_grid
from patterns.dp import climb_stairs, coin_change, length_of_lis


class TestPatterns(unittest.TestCase):
    def test_hashing(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(two_sum([3, 3], 6), [0, 1])
        groups = sorted(sorted(g) for g in group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
        self.assertEqual(groups, [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]])

    def test_two_pointers(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
        self.assertFalse(is_palindrome("race a car"))
        self.assertEqual(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)

    def test_sliding_window(self):
        self.assertEqual(longest_unique_substring("abcabcbb"), 3)
        self.assertEqual(longest_unique_substring("bbbbb"), 1)
        self.assertEqual(longest_unique_substring(""), 0)

    def test_binary_search(self):
        self.assertEqual(search_rotated([4, 5, 6, 7, 0, 1, 2], 0), 4)
        self.assertEqual(search_rotated([4, 5, 6, 7, 0, 1, 2], 3), -1)
        self.assertEqual(min_eating_speed([3, 6, 7, 11], 8), 4)

    def test_graphs(self):
        grid = [list("11000"), list("11000"), list("00100"), list("00011")]
        self.assertEqual(num_islands(grid), 3)
        self.assertEqual(shortest_path_grid([[0, 0, 0], [1, 1, 0], [0, 0, 0]]), 4)
        self.assertEqual(shortest_path_grid([[0, 1], [1, 0]]), -1)

    def test_dp(self):
        self.assertEqual(climb_stairs(5), 8)
        self.assertEqual(coin_change([1, 2, 5], 11), 3)
        self.assertEqual(coin_change([2], 3), -1)
        self.assertEqual(length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]), 4)


if __name__ == "__main__":
    unittest.main()
