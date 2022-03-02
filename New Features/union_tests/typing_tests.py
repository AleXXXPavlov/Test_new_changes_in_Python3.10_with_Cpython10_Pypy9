import unittest

from typing import Union, Optional


class GeneralTest(unittest.TestCase):
    def test_equal_with_typing(self):
        """
        The existing typing.Union and | syntax should be equivalent.
            - the order of the items in Union should not matter for equality
            - optional values should be equivalent to the new union syntax
            - a new Union.__repr__() method should be implemented
        """

        self.assertEqual(Union[int, int], int | int)
        self.assertEqual(Union[int, str], int | str)
        self.assertEqual(Union[float, int, str], float | int | str)

        self.assertEqual(Union[int, str], str | int)
        self.assertEqual(Union[int, float], float | int)

        self.assertEqual(Optional[int], int | None)
        self.assertEqual(Optional[str], str | None)

        self.assertEqual(str(int | list[str]), "int | list[str]")
        self.assertEqual(str(int | int), "int")

    def test_isinstance(self):
        """
        Testing that new syntax supports for calls to isinstance as long as the Union
            items are valid arguments to isinstance.
        """

        self.assertTrue(isinstance("", int | str))
        self.assertTrue(isinstance(0., int | float))

        self.assertFalse(isinstance("", float | tuple))
        self.assertFalse(isinstance([1], tuple | dict | set))

    def test_issubclass(self):
        """
        Testing that new syntax supports for calls to issubclass as long as the Union
            items are valid arguments to issubclass.
        """
        self.assertTrue(issubclass(bool, int | str))
        self.assertTrue(issubclass(bool, int | int))

        self.assertFalse(issubclass(bool, float | list))
        self.assertFalse(issubclass(int, float | str))

    def test_metaclass(self):
        """
        Testing that in some situations, some exceptions will not be raised as expected.
        """

        s_changes: str = "Incompatible changes"

        class MetaOr(type):
            def __or__(self, other):
                return s_changes

        class TestWithMeta(metaclass=MetaOr):
            pass

        self.assertEqual(s_changes, TestWithMeta | int)


if __name__ == "__main__":
    unittest.main()
