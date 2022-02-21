import unittest

from inspect import getfullargspec
from sys import exc_info
from traceback import format_exception_only, format_exception, print_exception


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


class PrintExceptionTest(unittest.TestCase):
    def setUp(self) -> None:
        """
        Recording traceback to a file for later verification.
        """
        try:
            "text" + 10
        except TypeError as e:
            # new style
            with open("new_style.txt", mode="w") as exc_file:
                print_exception(e, file=exc_file)

            # old style
            with open("old_style.txt", mode="w") as exc_file:
                exc_type, exc_value, exc_tb = exc_info()
                print_exception(exc_type, exc_value, exc_tb, file=exc_file)

    def test_new_calling_style(self):
        """
        Testing new opportunity that an exception object can be passed
            as the first argument in method print_exception.
        """
        new_style: str = ""
        with open("new_style.txt", mode="r") as exc_file:
            new_style = exc_file.read()

        old_style: str = ""
        with open("old_style.txt", mode="r") as exc_file:
            old_style = exc_file.read()

        self.assertEqual(new_style, old_style)

    def test_new_arg_name(self):
        """
        Testing new name for first parameter in method print_exception.
        """
        check_name: str = getfullargspec(print_exception).args[0]
        self.assertEqual(check_name, "exc")


if __name__ == "__main__":
    unittest.main()


