import unittest
from Assignment4a import GetRepoNameAndCommit

class Testfunction(unittest.TestCase):
    def testID1(self):
        self.assertEqual(GetRepoNameAndCommit('lovelifecat'), 1)

    def testID2(self):
        self.assertEqual(GetRepoNameAndCommit('richkempinski'), 1)

    def testIDfault(self):
        self.assertNotEqual(GetRepoNameAndCommit('dasfsdcxvzxcvafadf'), 1)
        self.assertEqual(GetRepoNameAndCommit('dasdasdafdsgfabv'), 0)
