import unittest
from Services import DirectoryScanner
from Tests.TestEnvironment import get_company_registry_mock


class DirectoryScannerTests(unittest.TestCase):
    def test_scan_new_files_finds_every_file_in_dir(self):
        dir_to_scan = 'Tests/TestEnvironment/'
        ds = DirectoryScanner([dir_to_scan], get_company_registry_mock())
        result = ds.scan_new_files()
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0][0], dir_to_scan + 'empty.csv')
        self.assertEqual(result[0][1], 'empty')

        self.assertEqual(result[1][0], dir_to_scan + 'header_and_desc.csv')
        self.assertEqual(result[1][1], 'header_and_desc')

        self.assertEqual(result[2][0], dir_to_scan + 'just_header.csv')
        self.assertEqual(result[2][1], 'just_header')
