import io
import unittest


class TextIoWrapperTest(unittest.TestCase):
    def test_warning(self):
        """
        Testing new EncodingWarning it is emitted when the encoding
        argument to TextIoWrapper() is omitted and the default locale-specific
        encoding is used.
        """

        buff = io.BytesIO(b"")
        with self.assertWarns(EncodingWarning):
            wp_stream = io.TextIOWrapper(buffer=buff)

    def test_locale(self):
        """
        A "locale" argument value is explicitly specifies that the locale encoding
         should be used, silencing the warning.
        """
        s_test = "test is right"
        buff = io.BytesIO(b"")
        
        with io.TextIOWrapper(buff, encoding="locale") as wp_stream:
            wp_stream.write(s_test)
            wp_stream.seek(io.SEEK_SET)

            s_save = wp_stream.read()
            self.assertEqual(s_save, s_test)


if __name__ == "__main__":
    unittest.main()
