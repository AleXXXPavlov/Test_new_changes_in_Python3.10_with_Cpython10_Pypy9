import collections
import unittest



class GeneralTest(unittest.TestCase):
    def test_with_namedtuple(self):
        """
        Testing When printing AttributeError, PyErr_Display() will offer
        suggestions of similar attribute names in the object that the exception
        was raised from
        """
        with self.assertRaisesRegex(AttributeError, ".*Did you mean: 'namedtuple'?"):
            exec("collections.namedtoplo")


if __name__ == "__main__":
    unittest.main()
