import unittest

from socket import htons, ntohs, ntohl


class HtonsTest(unittest.TestCase):
    int16_bit: int = 234
    int32_bit: int = 2147483000

    @unittest.expectedFailure
    def test_true_htons(self):
        """
        Testing correct working if data fit in a 16-bit
         unsigned integer for method - htons.
        """
        int16_host = ntohs(self.int16_bit)
        with self.assertRaises(OverflowError):
            # convert a 16-bit integer from host byte order to network byte order
            int16_network = htons(int16_host)

    def test_false_htons(self):
        """
        Testing throwing OverflowError exception if data does not
            fit in a 16-bit unsigned integer for method - htons.
        """
        int32_host = ntohl(self.int32_bit)
        with self.assertRaises(OverflowError):
            # try to convert a 32-bit integer from host byte order to network byte order
            int32_network = htons(int32_host)


if __name__ == "__main__":
    unittest.main()