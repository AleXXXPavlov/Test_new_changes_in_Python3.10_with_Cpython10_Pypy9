import unittest
import sys


class GeneralTest(unittest.TestCase):
    def test_with_if(self):
        """
        Testing that many IndentationError exceptions now have more context
        regarding what kind of block was expecting an indentation with -if
        """
        with self.assertRaisesRegex(IndentationError, ".*expected an indented block after 'if"):
            compile("if True:\nx=5", "", "exec")

    def test_with_while(self):
        """
        Testing that many IndentationError exceptions now have more context
        regarding what kind of block was expecting an indentation with -while
        """
        with self.assertRaisesRegex(IndentationError, ".*expected an indented block after 'while'"):
            compile("while True:\nx=5", "", "exec")


if __name__ == "__main__":
    unittest.main()
