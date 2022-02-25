import unittest
from _markupbase import ParserBase


class ParserBaseTest(unittest.TestCase):
    def test_remove_error(self):
        """
        Testing fact of removing the ParserBase.error() from
            the private and undocumented _markupbase module
        """
        self.assertFalse("error" in dir(ParserBase))


if __name__ == "__main__":
    unittest.main()
