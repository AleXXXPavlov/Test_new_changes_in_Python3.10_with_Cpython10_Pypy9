import format_exc_tests
import format_exc_only_tests
import print_exc_tests

import unittest


testCases = list()

# test cases for new opportunity in first parameter
testCases.append(format_exc_only_tests.FormatExcOnlyTest)
testCases.append(format_exc_tests.FormatExcTest)
testCases.append(print_exc_tests.PrintExceptionTest)

# assembly of all tests
suites = list()
testLoad = unittest.TestLoader()
for case in testCases:
    # get a group of tests from a separate class
    suites.append(testLoad.loadTestsFromTestCase(case))

res_suite = unittest.TestSuite(suites)

runner = unittest.TextTestRunner(verbosity=2)
runner.run(res_suite)
