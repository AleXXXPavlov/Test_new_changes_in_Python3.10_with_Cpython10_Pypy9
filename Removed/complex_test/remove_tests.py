import unittest
from sys import version_info


class ComplexRemoveTest(unittest.TestCase):
    def setUp(self) -> None:
        self.cmplx = 13.2 - 3.4j

    def test_removing_int(self):
        """
        Testing fact of removing __int__ of complex type in Python
        """
        with self.assertRaises(AttributeError):
            func = self.cmplx.__int__

    def test_removing_float(self):
        """
        Testing fact of removing __float__ of complex type in Python
        """
        with self.assertRaises(AttributeError):
            func = self.cmplx.__float__

    def test_removing_floordiv(self):
        """
        Testing fact of removing __floordiv__ of complex type in Python
        """
        with self.assertRaises(AttributeError):
            func = self.cmplx.__floordiv__

    def test_removing_mod(self):
        """
        Testing fact of removing __mod__ of complex type in Python
        """
        with self.assertRaises(AttributeError):
            func = self.cmplx.__mod__

    def test_removing_divmod(self):
        """
        Testing fact of removing __divmod__ of complex type in Python
        """
        with self.assertRaises(AttributeError):
            func = self.cmplx.__divmod__

    def test_removing_rfloordiv(self):
        """
        Testing fact of removing __rfloordiv__ of complex type in Python
        """
        with self.assertRaises(AttributeError):
            func = self.cmplx.__rfloordiv__

    def test_removing_rmod(self):
        """
        Testing fact of removing __rmod__ of complex type in Python
        """
        with self.assertRaises(AttributeError):
            func = self.cmplx.__rmod__

    def test_removing_rdivmod(self):
        """
        Testing fact of removing __rdivmod__ of complex type in Python
        """
        with self.assertRaises(AttributeError):
            func = self.cmplx.__rdivmod__


if __name__ == "__main__":
    unittest.main()
