import aliases_tests
import unittest


testCases = list()

# test cases for moving ABC classes to collections.abc module
testCases.append(aliases_tests.AliasExistTest)

# assembly of all tests
suites = list()
testLoad = unittest.TestLoader()
for case in testCases:
    # get a group of tests from a separate class
    suites.append(testLoad.loadTestsFromTestCase(case))

res_suite = unittest.TestSuite(suites)

runner = unittest.TextTestRunner(verbosity=2)
runner.run(res_suite)
