import function_type_tests
import inconsistent_args_tests
import match_tests
import socket_tests
import syntax_tests
import traceback_tests

import unittest


testCases = list()

# test cases for new pattern matching
testCases.append(match_tests.MatchTest)

# test cases for new opportunity in first parameter
testCases.append(traceback_tests.FormatExcOnlyTest)
testCases.append(traceback_tests.FormatExcTest)
testCases.append(traceback_tests.PrintExceptionTest)

# test cases for conversion functions - htons(), ntohs()
testCases.append(socket_tests.ConvertFunctionTest)

# test cases for inherits the current builtins
testCases.append(function_type_tests.FunctionTypeTest)

# test cases for changes in python syntax
testCases.append(syntax_tests.SyntaxTest)

# assembly of all tests
suites = list()
testLoad = unittest.TestLoader()
for case in testCases:
    # get a group of tests from a separate class
    suites.append(testLoad.loadTestsFromTestCase(case))

res_suite = unittest.TestSuite(suites)

runner = unittest.TextTestRunner(verbosity=2)
runner.run(res_suite)
