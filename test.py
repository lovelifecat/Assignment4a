import unittest
from Assignment4a import GetRepoNameAndCommit

class Testfunction(unittest.TestCase):
    def testID1(self):
        self.assertEqual(GetRepoNameAndCommit('lovelifecat'), 200)

    def testID2(self):
        self.assertEqual(GetRepoNameAndCommit('richkempinski'), 200)
                        
    def testIDfault(self):
        self.assertNotEqual(GetRepoNameAndCommit('dasdasdafdsgfabv'), 200)
        self.assertEqual(GetRepoNameAndCommit('dasdasdafdsgfabv'), 404)
