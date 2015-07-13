import pytest
class MyTestCase(unittest.TestCase):

    def test_add(self):
        # Could also be 'assertTrue' or 'failUnless'
        self.assert_(isinstance(2 + 4, int))

        self.assert_([2] + [4] == [6])
        # More explicit error message if it fails
        self.assertEqual([3] + [3], [6])
