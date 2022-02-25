import unittest

from asyncio_loop_tests import loop_tests
from collections_aliases_tests import aliases_tests
from complex_test import remove_tests, still_error_tests
from formatter_tests import formatter_tests
from old_parser_tests import parser_exist_tests
from parser_base_tests import parser_tests


testCases = list()

# test cases for removing loop-parameter
testCases.append(loop_tests.AsyncioLoopTest)

# test cases for moving ABC classes to collections.abc module
testCases.append(aliases_tests.AliasExistTest)

# test cases for checking still raising TypeError with corresponding operations
testCases.append(still_error_tests.ComplexErrorTest)

# test cases for checking fact of removing special methods
testCases.append(remove_tests.ComplexRemoveTest)

# test cases for testing removing outdated module named formatter
testCases.append(formatter_tests.FormatterTest)

# test cases for testing removing outdated module named parser
testCases.append(parser_exist_tests.ParserExistTest)

# test cases for testing removing error() method from _markupbase.ParserBase
testCases.append(parser_tests.ParserBaseTest)

# assembly of all tests
suites = list()
testLoad = unittest.TestLoader()
for case in testCases:
    # get a group of tests from a separate class
    suites.append(testLoad.loadTestsFromTestCase(case))

res_suite = unittest.TestSuite(suites)

runner = unittest.TextTestRunner(verbosity=2)
runner.run(res_suite)
