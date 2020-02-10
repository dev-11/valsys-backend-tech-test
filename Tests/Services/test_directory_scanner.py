import unittest
from Services import DirectoryScanner
from Tests.TestEnvironment import get_company_registry_mock


class DirectoryScannerTests(unittest.TestCase):
    def test_scan_new_files_finds_every_file_in_dir(self):
        dir_to_scan = 'Tests/TestEnvironment/'
        ds = DirectoryScanner([dir_to_scan], get_company_registry_mock())
        result = ds.scan_new_files()
        self.assertEqual(len(result), 3)

        expected_file_list = [[dir_to_scan + 'empty.csv', 'empty'],
                              [dir_to_scan + 'just_header.csv', 'just_header'],
                              [dir_to_scan + 'header_and_desc.csv', 'header_and_desc']]

        self.assertEqual(sorted(expected_file_list), sorted(result))
