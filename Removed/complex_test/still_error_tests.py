import unittest


"""
After removing them the corresponding operations (converting to int and float,
 operators // and %, function divmod()) will still a TypeError.
"""


class ComplexErrorTest(unittest.TestCase):
    def test_operation_div(self):
        """
        Testing that operation like // raise a TypeError with complex type.
        """
        self.assertRaises(TypeError, lambda: (0+0j) // 1)
        self.assertRaises(TypeError, lambda: (1+0j) // 1)
        self.assertRaises(TypeError, lambda: (0+1j) // 1)
        self.assertRaises(TypeError, lambda: (1-1j) // 1)
        self.assertRaises(TypeError, lambda: (2+1j) // 1)
        self.assertRaises(TypeError, lambda: (3.2-3.12j) // 1)

    def test_operation_mod(self):
        """
        Testing that operation like % raise a TypeError with complex type.
        """
        self.assertRaises(TypeError, lambda: (0+0j) % 1)
        self.assertRaises(TypeError, lambda: (1+0j) % 1)
        self.assertRaises(TypeError, lambda: (0+1j) % 1)
        self.assertRaises(TypeError, lambda: (1-1j) % 1)
        self.assertRaises(TypeError, lambda: (2+1j) % 1)
        self.assertRaises(TypeError, lambda: (3.2-3.12j) % 1)

    def test_converting_int(self):
        """
        Testing that converting with int raise a TypeError with complex type.
        """
        self.assertRaises(TypeError, int, (0 + 0j))
        self.assertRaises(TypeError, int, (1 + 0j))
        self.assertRaises(TypeError, int, (0 + 1j))
        self.assertRaises(TypeError, int, (1 - 1j))
        self.assertRaises(TypeError, int, (2 + 1j))
        self.assertRaises(TypeError, int, (3.2 - 3.12j))

    def test_converting_float(self):
        """
        Testing that converting with float raise a TypeError with complex type.
        """
        self.assertRaises(TypeError, float, (0 + 0j))
        self.assertRaises(TypeError, float, (1 + 0j))
        self.assertRaises(TypeError, float, (0 + 1j))
        self.assertRaises(TypeError, float, (1 - 1j))
        self.assertRaises(TypeError, float, (2 + 1j))
        self.assertRaises(TypeError, float, (3.2 - 3.12j))

    def test_function_divmod(self):
        """
        Testing that function - divmod() raise a TypeError with complex type.
        """
        self.assertRaises(TypeError, divmod, (0 + 0j), (0+0j))
        self.assertRaises(TypeError, divmod, (1 + 1j), 1.)
        self.assertRaises(TypeError, divmod, (1 + 1j), 1)
        self.assertRaises(TypeError, divmod, (1 + 1j), -1)
        self.assertRaises(TypeError, divmod, 1., (1+1j))
        self.assertRaises(TypeError, divmod, 1, (1+1j))


if __name__ == "__main__":
    unittest.main()


