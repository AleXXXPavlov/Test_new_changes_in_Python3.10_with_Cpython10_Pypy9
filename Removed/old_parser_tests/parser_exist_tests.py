import unittest

from sys import version_info


class ParserExistTest(unittest.TestCase):
    def test_exist_parser(self):
        """
        Testing removing outdated module named parser replace new parsing module with PEG
        """
        with self.assertRaises(ModuleNotFoundError):
            import parser

    # @unittest.skipIf(version_info.minor > 9, "check in Python 3.9")
    # def test_warn_parser(self):
    #     """
    #     Testing warning outdated module named parser replace new parsing module with PEG
    #     """
    #     with self.assertWarns(DeprecationWarning):
    #         import parser


if __name__ == "__main__":
    unittest.main()