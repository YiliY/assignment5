import unittest
from tests import test_commands

with open('test_output1.txt', 'w') as outfile:
    runner = unittest.TextTestRunner(stream=outfile, verbosity=3)
    unittest.main(module=test_commands, testRunner=runner)