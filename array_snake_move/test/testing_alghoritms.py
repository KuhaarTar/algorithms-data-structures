import unittest
from tripleSumSolving.src.triple_sumn_algorithm import plant_and_collect_pumpkins


class TestMatrixFunctions(unittest.TestCase):

    def test_plant_and_collect_pumpkins(self):
        m = 3
        n = 3
        result = plant_and_collect_pumpkins(m, n)
        expected_result = [1, 4, 7, 8, 5, 2, 3, 6, 9]
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
