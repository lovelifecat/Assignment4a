import unittest
import Assignment4a
from unittest import mock


class Testfunction(unittest.TestCase):

    @mock.patch('Assignment4a.GetRepoNameAndCommit')
    def test_mock_url_function(self, mock_url):
        mock_url.return_value = 1
        result = Assignment4a.GetRepoNameAndCommit('lovelifecat')
        self.assertEqual(result, True)

    @mock.patch('Assignment4a.GetRepoNameAndCommit')
    def test_mock_url_false(self, mock_url):
        mock_url.return_value = 0
        result = Assignment4a.GetRepoNameAndCommit('dasfsdcxvzxcvafadf')
        self.assertEqual(result, False)
