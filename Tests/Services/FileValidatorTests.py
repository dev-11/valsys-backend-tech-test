import unittest
from Services import FileValidator


class FileValidatorTests(unittest.TestCase):
    def test_is_file_structure_valid_returns_true_on_three_headers(self):
        fv = FileValidator()
        result = fv.is_file_structure_valid(['a', 'b', 'c'])
        self.assertTrue(result)

    def test_is_file_structure_valid_returns_false_on_few_headers(self):
        fv = FileValidator()
        result = fv.is_file_structure_valid(['a', 'b'])
        self.assertFalse(result)

    def test_is_file_structure_valid_returns_false_on_too_many_headers(self):
        fv = FileValidator()
        result = fv.is_file_structure_valid(['a', 'b', 'c', 'd'])
        self.assertFalse(result)

    def test_is_file_structure_valid_returns_false_on_empty_headers(self):
        fv = FileValidator()
        result = fv.is_file_structure_valid([])
        self.assertFalse(result)

    def test_is_file_structure_valid_returns_false_on_missing_headers(self):
        fv = FileValidator()
        result = fv.is_file_structure_valid(None)
        self.assertFalse(result)
