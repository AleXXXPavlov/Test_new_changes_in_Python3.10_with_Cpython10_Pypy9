import inconsistent_args_tests

import unittest


testCases = list()

# test case for check difference between collections.abc.Callable.__args__ and typing.Callable.__args__
testCases.append(inconsistent_args_tests.InconsistentArgsTest)


# assembly of all tests
suites = list()
testLoad = unittest.TestLoader()
for case in testCases:
    # get a group of tests from a separate class
    suites.append(testLoad.loadTestsFromTestCase(case))

res_suite = unittest.TestSuite(suites)

runner = unittest.TextTestRunner(verbosity=2)
runner.run(res_suite)
