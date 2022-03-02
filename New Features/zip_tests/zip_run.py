import zip_tests
import unittest


testCases = list()

# test cases for new optional length-checking parameter - strict
testCases.append(zip_tests.OptionalParamTest)

# assembly of all tests
suites = list()
testLoad = unittest.TestLoader()
for case in testCases:
    # get a group of tests from a separate class
    suites.append(testLoad.loadTestsFromTestCase(case))

res_suite = unittest.TestSuite(suites)

runner = unittest.TextTestRunner(verbosity=2)
runner.run(res_suite)
