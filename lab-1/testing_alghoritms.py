import unittest
from lab import plant_and_collect_pumpkins


class TestPumpkinAlgorithm(unittest.TestCase):

    def test_plant_and_collect_pumpkins_with_equal_m_and_n(self):
        m = 5
        n = 5
        result = plant_and_collect_pumpkins(m, n)
        expected_result = [1, 2, 3, 4, 5, 10, 9, 8, 7, 6, 11, 12, 13, 14, 15, 20, 19, 18, 17, 16, 21, 22, 23, 24, 25]
        self.assertEqual(result, expected_result)

    def test_plant_and_collect_pumpkins_with_m_2_and_n_4(self):
        m = 2
        n = 4
        result = plant_and_collect_pumpkins(m, n)
        expected_result = [1, 2, 3, 4, 8, 7, 6, 5]
        self.assertEqual(result, expected_result)

    def test_plant_and_collect_pumpkins_with_m_1_and_n_6(self):
        m = 1
        n = 6
        result = plant_and_collect_pumpkins(m, n)
        expected_result = [1, 2, 3, 4, 5, 6]
        self.assertEqual(result, expected_result)

    def test_plant_and_collect_pumpkins_with_m_6_and_n_2(self):
        m = 6
        n = 2
        result = plant_and_collect_pumpkins(m, n)
        expected_result = [1, 2, 4, 3, 5, 6, 8, 7, 9, 10, 12, 11]
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
