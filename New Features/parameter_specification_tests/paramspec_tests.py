import unittest

from typing import ParamSpec, TypeVar, Callable, Optional


class GeneralTest(unittest.TestCase):
    def test_simple(self):
        """
        Testing parameter specification variable as the first argument to Callable.
        """
        T = TypeVar("T")
        P = ParamSpec("p")

        def add_none(func: Callable[P, T]) -> Callable[P, Optional[T]]:
            def inner(*args: P.args, **kwargs: P.kwargs) -> Optional[T]:
                try:
                    func(*args, **kwargs)
                except Exception:
                    return None
            return inner

        # function for checking
        @add_none
        def division_by_zero(x: int) -> float:
            return x / 0

        # checking
        self.assertEqual(division_by_zero(), None)


if __name__ == '__main__':
    unittest.main()
