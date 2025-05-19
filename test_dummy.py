import unittest

class TestDummy(unittest.TestCase):

    # Alwass passes
    def test_dummy_pass(self):
        self.assertTrue(True)

    # Alwass fails
    #def test_dummy_fail(self):
    #    self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
