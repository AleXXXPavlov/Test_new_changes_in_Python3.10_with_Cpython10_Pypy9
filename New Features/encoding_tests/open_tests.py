import unittest

from warnings import filterwarnings


class OpenTest(unittest.TestCase):
    def test_warning(self):
        """
        Testing new EncodingWarning it is emitted when the encoding
        argument to open() is omitted and the default locale-specific
        encoding is used.
        """

        with self.assertWarns(EncodingWarning):
            with open("date/example.txt") as f:
                pass

    def test_locale(self):
        """
        A "locale" argument value is explicitly specifies that the locale encoding
         should be used, silencing the warning.
        """

        write_str = "abbababa"
        with open("date/example.txt", encoding="locale", mode="w") as file:
            file.write(write_str)

        save: str = ""
        with open("date/example.txt", encoding="locale", mode="r") as file:
            save = file.read()

        self.assertEqual(save, write_str)


if __name__ == "__main__":
    unittest.main()
