import unittest
from Assignment4a import GetRepoNameAndCommit

class Testfunction(unittest.TestCase):
    def testID1(self):
        self.assertEqual(GetRepoNameAndCommit('lovelifecat'), 200)

    def testID2(self):
        self.assertEqual(GetRepoNameAndCommit('richkempinski'), 200)

