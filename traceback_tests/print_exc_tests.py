import unittest

from inspect import getfullargspec
from sys import exc_info
from traceback import print_exception


class PrintExceptionTest(unittest.TestCase):
    def setUp(self) -> None:
        """
        Recording traceback to a file for later verification.
        """
        try:
            "text" + 10
        except TypeError as e:
            # new style
            with open("traceback_tests/exc_data/new_style.txt", mode="w") as exc_file:
                print_exception(e, file=exc_file)

            # old style
            with open("traceback_tests/exc_data/old_style.txt", mode="w") as exc_file:
                exc_type, exc_value, exc_tb = exc_info()
                print_exception(exc_type, exc_value, exc_tb, file=exc_file)

    def test_new_calling_style(self):
        """
        Testing new opportunity that an exception object can be passed
            as the first argument in method print_exception.
        """
        new_style: str = ""
        with open("traceback_tests/exc_data/new_style.txt", mode="r") as exc_file:
            new_style = exc_file.read()

        old_style: str = ""
        with open("traceback_tests/exc_data/old_style.txt", mode="r") as exc_file:
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
