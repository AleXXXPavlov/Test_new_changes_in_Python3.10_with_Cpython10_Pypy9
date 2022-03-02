import unittest

from typing import ParamSpec, Concatenate, TypeVar, Callable, Optional


class GeneralTest(unittest.TestCase):
    def test_add(self):
        """
        Testing Concatanate of using to type annotate a higher order callable
            which adds parameters of another callable.
        """
        T = TypeVar("T")
        P = ParamSpec("P")

        s_test = ""
        s_right = "test is right"

        # decorator which add new string argument
        def add_first_str(func: Callable[P, T]) -> Callable[Concatenate[str, P], T]:
            def inner(s: str, *args: P.args, **kwargs: P.kwargs) -> T:
                nonlocal s_test
                s_test = s
                return func(*args, **kwargs)

            return inner

        # function for checking
        @add_first_str
        def foo() -> None:
            pass

        foo(s_right)

        self.assertEqual(s_test, s_right)

    def test_remove(self):
        """
        Testing Concatanate of using to type annotate a higher order callable
            which removes parameters of another callable.
        """
        T = TypeVar("T")
        P = ParamSpec("P")

        s_test = ""
        s_right = "test is right"

        # decorator which remove first string argument
        def remove_first_str(func: Callable[Concatenate[str, P], T]) -> Callable[P, T]:
            def inner(*args: P.args, **kwargs: P.kwargs) -> T:
                nonlocal s_test, s_right
                s_test = s_right
                return func(s_test, *args, **kwargs)

            return inner

        # function for checking
        @remove_first_str
        def foo(s: str) -> None:
            pass

        foo()

        self.assertEqual(s_test, s_right)

    def test_transform(self):
        """
        Testing Concatanate of using to type annotate a higher order callable
            which transforms parameters of another callable.
        """
        P = ParamSpec("P")

        # decorator which transform return' value
        def transform_to_none(func: Callable[P, int]) -> Callable[P, None]:
            def inner(*args: P.args, **kwargs: P.kwargs) -> None:
                func(*args, **kwargs)
                return None

            return inner

        # function for checking
        @transform_to_none
        def foo() -> int:
            return 0

        self.assertEqual(foo(), None)


if __name__ == '__main__':
    unittest.main()
