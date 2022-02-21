import unittest

from collections.abc import Callable as abcCallable
from sys import version_info
from typing import Callable as tCallable

if version_info.minor > 9:
    from typing import ParamSpec, TypeVar


class InconsistentArgsTest(unittest.TestCase):
    def test_inconsistent(self):
        """
        Testing two ways of getting a parametrised Callable have inconsistent __args__
        """
        args1 = abcCallable[[int, int], int].__args__
        args2 = tCallable[[int, int], int].__args__

        self.assertEqual(args1, args2)

    @unittest.skipIf(version_info.minor < 10, "since 10th version")
    def test_paramspec_typevar(self):
        """
        Testing collections.abc.Callable supporting ParamSpec and TypeVar
        """

        ps = ParamSpec("ps")
        tv = TypeVar("tv")

        def example_logging(func: abcCallable[ps, tv]) -> abcCallable[ps, tv]:
            def inner(*args: ps.args, **kwargs: ps.kwargs) -> tv:
                return func(*args, **kwargs)
            return inner

        @example_logging
        def concatenate(str1: str, str2: str) -> str:
            return str1 + str2

        self.assertEqual(concatenate("a", "b"), "ab")


if __name__ == "__main__":
    unittest.main()
