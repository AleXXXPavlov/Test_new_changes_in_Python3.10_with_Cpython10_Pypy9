import concatenate_tests
import paramspec_tests
import unittest


testCases = list()

# test cases for parameter specification variable
testCases.append(paramspec_tests.GeneralTest)

# test cases for Concatanate of using to type annotate a higher order callable
testCases.append(concatenate_tests.GeneralTest)

# assembly of all tests
suites = list()
testLoad = unittest.TestLoader()
for case in testCases:
    # get a group of tests from a separate class
    suites.append(testLoad.loadTestsFromTestCase(case))

res_suite = unittest.TestSuite(suites)

runner = unittest.TextTestRunner(verbosity=2)
runner.run(res_suite)
