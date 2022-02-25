import remove_tests
import still_error_tests
import unittest


testCases = list()

# test cases for checking still raising TypeError with corresponding operations
testCases.append(still_error_tests.ComplexErrorTest)

# test cases for checking fact of removing special methods
testCases.append(remove_tests.ComplexRemoveTest)

# assembly of all tests
suites = list()
testLoad = unittest.TestLoader()
for case in testCases:
    # get a group of tests from a separate class
    suites.append(testLoad.loadTestsFromTestCase(case))

res_suite = unittest.TestSuite(suites)

runner = unittest.TextTestRunner(verbosity=2)
runner.run(res_suite)
