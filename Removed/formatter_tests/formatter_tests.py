import unittest

from sys import version_info


class FormatterTest(unittest.TestCase):
    def test_exist_parser(self):
        """
        Testing removing outdated module named formatter replace new parsing module with PEG
        """
        with self.assertRaises(ModuleNotFoundError):
            import formatter

    # @unittest.skipIf(version_info.minor > 9 or version_info.minor < 5, "check in Python 3.9")
    # def test_warn_parser(self):
    #     """
    #     Testing warning outdated module named formatter replace new parsing module with PEG
    #     """
    #     with self.assertWarns(DeprecationWarning):
    #         import formatter


if __name__ == '__main__':
    unittest.main()
