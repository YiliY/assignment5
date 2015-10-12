import unittest
from tests import test_commands

# This file runs the test_commands file, outputting the results to an output file
outfilename = 'test_output2.txt'
with open(outfilename, 'w') as outfile:
    runner = unittest.TextTestRunner(stream=outfile, verbosity=3)
    unittest.main(module=test_commands, testRunner=runner)