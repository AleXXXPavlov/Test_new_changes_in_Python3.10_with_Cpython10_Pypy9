import sys
import unittest


def foo() -> (int, int):
    # len.__builtins__ <- __globals__['__builtins__']
    len_before: int = len("test")

    # change foo's definition in __globals__
    builtins_ns = foo.__globals__['__builtins__']
    if hasattr(builtins_ns, '__dict__'):
        builtins_ns = builtins_ns.__dict__
    builtins_ns['len'] = lambda x: 8

    # new definition using in Python3.10, but using old definition in Python3.9
    len_after: int = len("test")
    return len_before, len_after


class FunctionTypeTest(unittest.TestCase):
    @unittest.skipIf(sys.version_info.minor < 10, "specific test")
    def test_hack_v10(self):
        """
        Testing types.FunctionType constructor with Cpython
        """
        len_before1, len_after1 = foo()  # first call - checking modifying
        len_before2, len_after2 = foo()  # second call - checking saving

        self.assertTrue(len_before1 == 4 and len_after1 == 8)
        self.assertTrue(len_before2 == 8 and len_after2 == 8)

    @unittest.skipIf(sys.version_info.minor > 9, "specific test")
    def test_hack_v9(self):
        """
        Testing types.FunctionType constructor with Pypy

        In Python 3.9 the binding is more late-ish binding, than true late binding.
        Because globals['__builtins__'] is cached for each function activation,
        executing functions don't see updates.

        But I was surprised...This test is correct, you know?
        """
        len_before1, len_after1 = foo()  # first call - checking saving
        len_before2, len_after2 = foo()  # second call - checking modifying

        self.assertFalse(len_before1 == 4 and len_after1 == 4)
        self.assertTrue(len_before2 == 8 and len_after2 == 8)


if __name__ == "__main__":
    unittest.main()
