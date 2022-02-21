import unittest

from socket import ntohs


class NtohsTest(unittest.TestCase):
    int16_bit: int = 234
    int32_bit: int = 2147483000

    @unittest.expectedFailure
    def test_true_ntohs(self):
        """
        Testing correct working if data fit in a 16-bit
            unsigned integer for method - ntohs.
        """
        with self.assertRaises(OverflowError):
            # convert a 16-bit integer from network byte order to host byte order
            int16_host = ntohs(self.int16_bit)

    def test_false_ntohs(self):
        """
        Testing throwing OverflowError exception if data does not
            fit in a 16-bit unsigned integer for method - ntohs.
        """
        with self.assertRaises(OverflowError):
            # try to convert a 32-bit integer from network byte order to host byte order
            int32_host = ntohs(self.int32_bit)


if __name__ == "__main__":
    unittest.main()
