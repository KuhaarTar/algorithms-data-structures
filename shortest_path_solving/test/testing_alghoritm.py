import unittest
from shortest_path_solving.src.shortest_path_graph import (
    find_shortest_path_or_return_none,
)


class TestFindShortestWay(unittest.TestCase):
    def test_find_shortest_1(self):
        result = find_shortest_path_or_return_none("text_1.txt")
        self.assertEqual(result, 7)

    def test_find_shortest_2(self):
        result = find_shortest_path_or_return_none("input.txt")
        self.assertEqual(result, 12)


if __name__ == "__main__":
    unittest.main()
