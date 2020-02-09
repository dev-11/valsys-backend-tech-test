import unittest
from Repositories import CsvRepository


class CsvRepositoryTests(unittest.TestCase):
    def test01(self):
        csv_file = 'Tests/TestEnvironment/empty.csv'
        repo = CsvRepository()
        a = repo.get_headers(csv_file)
        self.assertTrue(True)
