import unittest

from inspect import getfullargspec
from sys import exc_info
from traceback import format_exception_only


class FormatExcOnlyTest(unittest.TestCase):
    def test_new_calling_style(self):
        """
        Testing new opportunity that an exception object can be passed
            as the first argument in method format_exception_only.
        """
        num1 = 1
        num2 = 0
        try:
            num1 / num2
        except ZeroDivisionError as e:
            # new style
            traceback_new_out: list = format_exception_only(e)
            # old style
            exc_type, exc_value, _ = exc_info()
            traceback_old_out: list = format_exception_only(exc_type, exc_value)

            self.assertEqual(traceback_new_out, traceback_old_out)
            self.assertEqual(''.join(traceback_old_out), 'ZeroDivisionError: division by zero\n')

    def test_new_arg_name(self):
        """
        Testing new name for first parameter in method format_exception_only.
        """
        check_name: str = getfullargspec(format_exception_only).args[0]
        self.assertEqual(check_name, "exc")


if __name__ == "__main__":
    unittest.main()
