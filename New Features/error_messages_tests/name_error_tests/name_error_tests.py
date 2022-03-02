import unittest


class GeneralTest(unittest.TestCase):
    def test_with_hard_name(self):
        """
        Testing that when printing NameError raised by the interpreter, PyErr_Display()
        will offer suggestions of similar variable names in the function that the exception
        was raised from
        """
        with self.assertRaisesRegex(NameError, ".*Did you mean: 'schwarzschild_black_hole'?"):
            compile("schwarzschild_black_hole = None\nschwarschild_black_hole", "", "exec")


if __name__ == '__main__':
    unittest.main()

