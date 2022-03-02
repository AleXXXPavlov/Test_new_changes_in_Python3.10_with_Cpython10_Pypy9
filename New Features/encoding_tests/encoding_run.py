import open_tests
import text_io_wrapper_tests
import unittest


testCases = list()

# test cases for new encoding features with open
testCases.append(open_tests.OpenTest)

# test cases for new encoding features with io.TextIoWrapper
testCases.append(text_io_wrapper_tests.TextIoWrapperTest)

# assembly of all tests
suites = list()
testLoad = unittest.TestLoader()
for case in testCases:
    # get a group of tests from a separate class
    suites.append(testLoad.loadTestsFromTestCase(case))

res_suite = unittest.TestSuite(suites)

runner = unittest.TextTestRunner(verbosity=2)
runner.run(res_suite)
