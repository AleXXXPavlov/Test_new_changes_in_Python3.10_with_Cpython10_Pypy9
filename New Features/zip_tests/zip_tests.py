import unittest

from inspect import getfullargspec


class OptionalParamTest(unittest.TestCase):
    def test_with_strict(self):
        """
        Testing with new optional length-checking in zip() classes.
        """

        lst1 = [1, 2, "A"]
        lst2 = [1]

        with self.assertRaises(ValueError):
            zip_obj = list(zip(lst1, lst2, strict=True))

    def test_without_strict(self):
        """
        Testing without new optional length-checking in zip() classes.
        """

        lst = [1, 2]
        zip_lst = list(zip(lst, lst, strict=False))

        self.assertEqual(zip_lst, [(1, 1), (2, 2)])


if __name__ == '__main__':
    unittest.main()
