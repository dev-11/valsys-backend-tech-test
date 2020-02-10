import unittest
from Repositories import CsvRepository


class CsvRepositoryTests(unittest.TestCase):
    def test_get_headers_raises_StopIteration_on_empty_csv(self):
        csv_file = 'Tests/TestEnvironment/empty.csv'
        repo = CsvRepository()
        self.assertRaises(StopIteration, repo.get_headers, csv_file)

    def test_get_headers_returns_headers(self):
        csv_file = 'Tests/TestEnvironment/just_header.csv'
        repo = CsvRepository()
        result = repo.get_headers(csv_file)
        self.assertEqual(3, len(result))
        self.assertEqual(['header1', 'header2', 'header3'], result)

    def test_get_metadata_raisesStopIteration_on_missing_description_row(self):
        csv_file = 'Tests/TestEnvironment/just_header.csv'
        repo = CsvRepository()
        self.assertRaises(StopIteration, repo.get_metadata, csv_file)

    def test_get_metadata_returns_description_row(self):
        csv_file = 'Tests/TestEnvironment/header_and_desc.csv'
        repo = CsvRepository()
        result = repo.get_metadata(csv_file)
        self.assertEqual(3, len(result))
        self.assertEqual(['desc1', 'desc2', 'desc3'], result)
