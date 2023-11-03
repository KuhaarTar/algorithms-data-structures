import unittest
from shortest_path_solving.src.shortest_path_graph import find_shortest_path_or_return_none


class TestFindShortestWay(unittest.TestCase):
    def test_leftLeavesSum_root(self):
        result = find_shortest_path_or_return_none("text_1.txt")
        self.assertEqual(result, 7)


if __name__ == "__main__":
    unittest.main()
