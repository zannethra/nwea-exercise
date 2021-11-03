import sys
import inspect
import unittest
from flatten import flatten

class TestFlatten(unittest.TestCase):
    def test_flatten_integer(self):
        res = flatten(5)
        self.assertEqual(res, [5])

    def test_flatten_empty(self):
        res = flatten([])
        self.assertEqual(res, [])

    def test_flatten_simple_list(self):
        res = flatten([3, 2, 1, 0])
        self.assertEqual(res, [3, 2, 1, 0])

    def test_flatten_simple_list_with_large_range(self):
        res = flatten([3, 2, sys.maxsize + 1, -sys.maxsize - 1, 1])
        self.assertEqual(res, [3, 2, sys.maxsize + 1, -sys.maxsize - 1, 1])

    def test_flatten_nested_1_level(self):
        res = flatten([[5, 6], 6, [7], 8, 10])
        self.assertEqual(res, [5, 6, 6, 7, 8, 10])

    def test_flatten_nested_multi_level(self):
        multilevel = [
            [5, 6], 
            6, 
            [
                7, 
                [
                    8, 
                    [],
                    9, 
                    10, 
                    [3], 
                    [1, 7, 4, 0, 3452345345],
                    ],
                ], 
            8, 
            10,
            ]
        expected = [5, 6, 6, 7, 8, 9, 10, 3, 1, 7, 4, 0, 3452345345, 8, 10 ]

        res = flatten(multilevel)
        self.assertEqual(res, expected)

    def test_flatten_unexpected_type(self):
        self.assertRaises(ValueError, flatten, [[5, 6.7], 6, 8, 10])
        self.assertRaises(ValueError, flatten, [[5, 6], "apple", 6, 8, 10])
        self.assertRaises(ValueError, flatten, [[5, 6], ["banana"], 6, 8, 10])

    @unittest.skip("unsure how this test will run in other environments")
    def test_flatten_nested_extreme_level(self):
        stack_size = len(inspect.stack(0))
        max_recursion = sys.getrecursionlimit() - stack_size - 10

        input = 1
        for i in range(max_recursion):
            input = [input]

        res = flatten(input)
        self.assertEqual(res, [1])

if __name__ == '__main__':
    unittest.main()
