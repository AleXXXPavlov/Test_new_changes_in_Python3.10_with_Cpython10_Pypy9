import parser_exist_tests
import unittest


testCases = list()

# test cases for testing removing outdated module named parser
testCases.append(parser_exist_tests.ParserExistTest)

# assembly of all tests
suites = list()
testLoad = unittest.TestLoader()
for case in testCases:
    # get a group of tests from a separate class
    suites.append(testLoad.loadTestsFromTestCase(case))

res_suite = unittest.TestSuite(suites)

runner = unittest.TextTestRunner(verbosity=2)
runner.run(res_suite)
