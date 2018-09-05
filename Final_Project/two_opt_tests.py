import two_opt as to
import unittest

class TwoOptTestCase(unittest.TestCase):
    def test_two_opt_swap(self):
        # test middle of list
        reference_list = [0, 1, 2, 3, 4, 5, 6]
        test_list = reference_list[:]
        to.two_opt_swap(test_list, 2, 4)
        self.assertEqual(test_list[0], reference_list[0])
        self.assertEqual(test_list[1], reference_list[1])
        self.assertEqual(test_list[2], reference_list[4])
        self.assertEqual(test_list[3], reference_list[3])
        self.assertEqual(test_list[4], reference_list[2])
        self.assertEqual(test_list[5], reference_list[5])
        self.assertEqual(test_list[6], reference_list[6])

        # test lower bound of list
        test_list = reference_list[:]
        to.two_opt_swap(test_list, 0, 1)
        self.assertEqual(test_list[0], reference_list[1])
        self.assertEqual(test_list[1], reference_list[0])

        # test upper bound of list
        test_list = reference_list[:]
        lt = len(test_list) - 1
        to.two_opt_swap(test_list, lt - 1, lt)
        self.assertEqual(test_list[lt - 1], reference_list[lt])
        self.assertEqual(test_list[lt], reference_list[lt - 1])


if __name__ == '__main__':
    unittest.main()
    