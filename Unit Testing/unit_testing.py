# Import Python's built-in unittest module
import unittest

# Function that we want to test
def add(a, b):
    return a + b


# Create a test class. It must inherit from unittest.TestCase
class TestMath(unittest.TestCase):


    # Every test method must start with "test_"
    def test_add(self):

        # Check whether add(5, 3) returns 8
        self.assertEqual(add(5, 3), 8)


# Run the tests only when this file is executed directly.
# If another Python file imports this file,
# the tests will NOT run automatically.
if __name__ == "__main__":

    # Find and run all test methods.
    unittest.main()