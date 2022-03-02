import unittest
from typing import TypeGuard, TypeVar, Type, Any


class GeneralTest(unittest.TestCase):
    def test_standard_type(self):
        """
        Testing a way for programs to influence conditional type narrowing
        employed by a type checker based on runtime checks with standard_type.
        """
        # typeguard function - new style
        def is_one_element_list(lst: list[object]) -> TypeGuard[list[int]]:
            return len(lst) == 1

        lst = [1]
        self.assertTrue(is_one_element_list(lst))
        lst.append(1)
        self.assertFalse(is_one_element_list(lst))

    def test_with_add_param(self):
        """
        Testing a way for programs to influence conditional type narrowing employed
        by a type checker based on runtime checks with standard_type with add parameter.
        """
        T = TypeVar("T")

        def is_tuple_of(tp: tuple[object], type_elem: Type[T], allow_empty: bool = True) -> TypeGuard[tuple[T]]:
            if len(tp) == 0:
                return allow_empty
            else:
                return all(isinstance(elem, type_elem) for elem in tp)

        self.assertFalse(is_tuple_of(("", 2), int))
        self.assertFalse(is_tuple_of((), str, False))
        self.assertTrue(is_tuple_of(([], []), list))

    def test_with_class(self):
        class Point:
            __match_args__ = ("x", "y", "name")

            def __init__(self, x, y, name):
                self.x = x
                self.y = y
                self.name = name

        def is_point(var: object) -> TypeGuard[Point]:
            try:
                return isinstance(var.x, int) and isinstance(var.y, int) and \
                       isinstance(var.name, str)
            except AttributeError:
                return False

        def is_set_of_points(st: set[object]) -> TypeGuard[set[Point]]:
            return all(is_point(point) for point in st)

        self.assertFalse(is_point(""))
        self.assertTrue(is_point(Point(1, 1, "")))
        self.assertTrue({Point(0, 0, ""), Point(-1, -1, "")})


if __name__ == '__main__':
    unittest.main()
