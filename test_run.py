import function_type_tests.function_type_tests as function_type_tests
import match_tests.match_tests as match_tests
import socket_tests.htons_tests as htons_tests
import socket_tests.ntohs_tests as ntohs_tests
import syntax_tests.syntax_tests as syntax_tests
import traceback_tests.format_exc_only_tests as format_exc_only_tests
import traceback_tests.format_exc_tests as format_exc_tests
import traceback_tests.print_exc_tests as print_exc_tests

import unittest


testCases = list()

# test cases for new pattern matching
testCases.append(match_tests.MatchTest)

# test cases for new opportunity in first parameter
testCases.append(format_exc_only_tests.FormatExcOnlyTest)
testCases.append(format_exc_tests.FormatExcTest)
testCases.append(print_exc_tests.PrintExceptionTest)

# test cases for conversion functions - htons(), ntohs()
testCases.append(htons_tests.HtonsTest)
testCases.append(ntohs_tests.NtohsTest)

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
