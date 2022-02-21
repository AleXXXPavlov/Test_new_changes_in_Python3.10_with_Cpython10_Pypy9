import htons_tests
import ntohs_tests
import unittest


testCases = list()

# test cases for conversion functions - htons(), ntohs()
testCases.append(htons_tests.HtonsTest)
testCases.append(ntohs_tests.NtohsTest)

# assembly of all tests
suites = list()
testLoad = unittest.TestLoader()
for case in testCases:
    # get a group of tests from a separate class
    suites.append(testLoad.loadTestsFromTestCase(case))

res_suite = unittest.TestSuite(suites)

runner = unittest.TextTestRunner(verbosity=2)
runner.run(res_suite)
