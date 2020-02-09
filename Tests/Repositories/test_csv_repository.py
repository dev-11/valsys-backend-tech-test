import unittest
from Repositories import CsvRepository


class CsvRepositoryTests(unittest.TestCase):
    def test_get_headers_raises_StopIteration_on_empty_csv(self):
        csv_file = 'Tests/TestEnvironment/empty.csv'
        repo = CsvRepository()
        self.assertRaises(StopIteration, repo.get_headers, csv_file)
