import unittest

from inspect import getfullargspec
from sys import exc_info
from traceback import format_exception


class FormatExcTest(unittest.TestCase):
    def test_new_calling_style(self):
        """
        Testing new opportunity that an exception object can be passed
            as the first argument in method format_exception.
        """
        try:
            chr(-97)
        except ValueError as e:
            # new style
            traceback_new_out: list = format_exception(e)
            # old style
            exc_type, exc_value, exc_tb = exc_info()
            traceback_old_out: list = format_exception(exc_type, exc_value, exc_tb)

            self.assertEqual(traceback_new_out, traceback_old_out)

    def test_new_arg_name(self):
        """
        Testing new name for first parameter in method format_exception.
        """
        check_name: str = getfullargspec(format_exception).args[0]
        self.assertEqual(check_name, "exc")


if __name__ == "__main__":
    unittest.main()
    