import unittest

from typing import TypeAlias


class CheckingTypes:
    def __init__(self):
        self.x = 0


class GeneralTest(unittest.TestCase):
    def test_simple(self):
        """
        Testing new explicit type alias with simple types and class
        """
        # declaration our types
        type_int: TypeAlias = int
        type_str: TypeAlias = str
        type_list: TypeAlias = list
        type_list_with_int: TypeAlias = list[int, ...]
        type_inner: TypeAlias = CheckingTypes

        # definition variables with nour types
        check_int: type_int = 0
        check_str: type_str = ""
        check_list: type_list = ["", ""]
        check_list_with_int: type_list_with_int = [1, ""]
        check_class: type_inner = CheckingTypes()

        # checking
        self.assertEqual(check_int, 0)
        self.assertEqual(check_str, "")
        self.assertEqual(check_list, ["", ""])
        self.assertEqual(check_list_with_int, [1, ""])
        self.assertEqual(check_class.x, 0)

    def test_backward_compatibility(self):
        """
        Testing implicit syntax (pre-existing)
        """
        # declaration our types
        type_int = int
        type_str = str
        type_list = list
        type_list_with_int = list[int, ...]
        type_inner = CheckingTypes

        # definition variables with nour types
        check_int: type_int = 0
        check_str: type_str = ""
        check_list: type_list = ["", ""]
        check_list_with_int: type_list_with_int = [1, ""]
        check_class: type_inner = CheckingTypes()

        # checking
        self.assertEqual(check_int, 0)
        self.assertEqual(check_str, "")
        self.assertEqual(check_list, ["", ""])
        self.assertEqual(check_list_with_int, [1, ""])
        self.assertEqual(check_class.x, 0)

    def test_functions(self):
        """
        Testing type alias with functions
        """
        type_int: TypeAlias = int
        type_class: TypeAlias = CheckingTypes

        # functions which return our type
        def foo_int() -> type_int:
            return 0

        def foo_class() -> type_class:
            return CheckingTypes()

        # checking
        self.assertEqual(foo_int(), 0)
        self.assertEqual(foo_class().x, 0)


if __name__ == "__main__":
    unittest.main()

