import sys
import unittest
import io


class GeneralTest(unittest.TestCase):
    def test_with_brackets(self):
        """
        When parsing code that contains unclosed parentheses or brackets
         the interpreter now includes the location of the unclosed bracket
         of parentheses
        """
        with self.assertRaisesRegex(SyntaxError, ".*unmatched '}'") as se:
            compile("dct = 'a': 1, 'b': 2}", "", "eval")
            print(se.exception)

    def test_with_missing_colon(self):
        """
        Testing with missing : before blocks
        """
        with self.assertRaisesRegex(SyntaxError, ".*expected ':'"):
            compile("for i in range(5)\n\tpass", "", "exec")

    def test_with_unparenthesised_tuples(self):
        """
        Testing with unparenthesised tuples in comprehensions targets:
        """
        with self.assertRaisesRegex(SyntaxError, ".*did you forget parentheses"
                                                 " around the comprehension target?"):
            compile("{x,y for x,y in zip('abcd', '1234')}", "", "eval")

    def test_with_mising_commas(self):
        """
        Testing with missing commas in collection literals and between expressions
        """
        with self.assertRaisesRegex(SyntaxError, ".*Perhaps you forgot a comma?"):
            compile("items = {z: 1, y: 2 x: 3}", "", "exec")

    def test_with_multiple_exception_types(self):
        """
        Testing with multiple exception types without parentheses
        """
        with self.assertRaisesRegex(SyntaxError, ".*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^.*"):
            compile("try:\n\tx = 5\nexcept SyntaxError, ZeroDivisionByError:\n\tpass", "", "eval")

    def test_with_try(self):
        """
        Testing with try blocks without except or finally blocks:
        """
        with self.assertRaisesRegex(SyntaxError, ".*expected 'except' or 'finally' block"):
            compile("try:\n\tx=5\ny=5", "", "exec")

    def test_with_comparison(self):
        """
        Testing usage of = instead of == in comparisons
        """
        with self.assertRaisesRegex(SyntaxError, ".*Maybe you meant '==' or ':=' instead of '='?"):
            compile("if x = y:\npass", "", "exec")


if __name__ == "__main__":
    unittest.main()
