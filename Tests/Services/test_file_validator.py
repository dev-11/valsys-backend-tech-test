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

    def test_get_statement_type_returns_balance_sheet_on_current_assets_in_desc(self):
        fv = FileValidator()
        result = fv.get_statement_type(['', 'current assets', ''])
        self.assertEqual(2, len(result))
        self.assertEqual('balance_sheet', result[0])
        self.assertEqual('balance sheet', result[1])

    def test_get_statement_type_returns_cash_flow_statement_on_operating_keyword_in_desc(self):
        fv = FileValidator()
        result = fv.get_statement_type(['', 'Operating', ''])
        self.assertEqual(2, len(result))
        self.assertEqual('cash_flow_statement', result[0])
        self.assertEqual('cash flow statement', result[1])

    def test_get_statement_type_returns_cash_flow_statement_on_activities_keyword_in_desc(self):
        fv = FileValidator()
        result = fv.get_statement_type(['', 'activities', ''])
        self.assertEqual(2, len(result))
        self.assertEqual('cash_flow_statement', result[0])
        self.assertEqual('cash flow statement', result[1])

    def test_get_statement_type_returns_cash_flow_statement_on_operations_keyword_in_desc(self):
        fv = FileValidator()
        result = fv.get_statement_type(['', 'Operations', ''])
        self.assertEqual(2, len(result))
        self.assertEqual('cash_flow_statement', result[0])
        self.assertEqual('cash flow statement', result[1])

    def test_get_statement_type_returns_income_statement_on_income_keyword_in_desc(self):
        fv = FileValidator()
        result = fv.get_statement_type(['', 'Income', ''])
        self.assertEqual(2, len(result))
        self.assertEqual('income_statement', result[0])
        self.assertEqual('income statement', result[1])

    def test_get_statement_type_returns_income_statement_on_revenues_keyword_in_desc(self):
        fv = FileValidator()
        result = fv.get_statement_type(['', 'revenues', ''])
        self.assertEqual(2, len(result))
        self.assertEqual('income_statement', result[0])
        self.assertEqual('income statement', result[1])

    def test_get_statement_type_returns_income_statement_on_revenue_keyword_in_desc(self):
        fv = FileValidator()
        result = fv.get_statement_type(['', 'revenue', ''])
        self.assertEqual(2, len(result))
        self.assertEqual('income_statement', result[0])
        self.assertEqual('income statement', result[1])

    def test_get_statement_type_returns_unknown_statement_on_empty_keyword_in_desc(self):
        fv = FileValidator()
        result = fv.get_statement_type(['', '', ''])
        self.assertEqual(2, len(result))
        self.assertEqual('unknown_statement', result[0])
        self.assertEqual('unknown statement', result[1])

    def test_get_statement_type_raises_attribute_error_on_None_keyword_in_desc(self):
        fv = FileValidator()
        self.assertRaises(AttributeError, fv.get_statement_type, ['', None, ''])

    def test_get_statement_type_returns_unknown_statement_on_alien_keyword_in_desc(self):
        fv = FileValidator()
        result = fv.get_statement_type(['', '!@#$%^&*(ASDFGHJK', ''])
        self.assertEqual(2, len(result))
        self.assertEqual('unknown_statement', result[0])
        self.assertEqual('unknown statement', result[1])

    def test_is_file_in_good_dir_returns_true_for_balance_sheet(self):
        fv = FileValidator()
        result = fv.is_file_in_good_dir('balance_sheet', '/foo/dir/balance_sheet/file.ext')
        self.assertTrue(result)

    def test_is_file_in_good_dir_returns_true_for_income_statement(self):
        fv = FileValidator()
        result = fv.is_file_in_good_dir('income_statement', '/foo/dir/income_statement/file.ext')
        self.assertTrue(result)

    def test_is_file_in_good_dir_returns_true_for_cash_flow_statement(self):
        fv = FileValidator()
        result = fv.is_file_in_good_dir('cash_flow_statement', '/foo/dir/cash_flow_statement/file.ext')
        self.assertTrue(result)

    def test_is_file_in_good_dir_returns_false_on_wrong_dir_for_cash_flow_statement(self):
        fv = FileValidator()
        result = fv.is_file_in_good_dir('cash_flow_statement', '/foo/dir/income_statement/file.ext')
        self.assertFalse(result)

    def test_is_file_in_good_dir_returns_false_on_wrong_dir_for_cash_flow_statement_2(self):
        fv = FileValidator()
        result = fv.is_file_in_good_dir('cash_flow_statement', '/foo/dir/balance_sheet/file.ext')
        self.assertFalse(result)

    def test_is_file_in_good_dir_returns_false_on_wrong_dir_for_cash_flow_statement_3(self):
        fv = FileValidator()
        result = fv.is_file_in_good_dir('cash_flow_statement', '/foo/dir/dummy_dir/file.ext')
        self.assertFalse(result)

    def test_is_file_in_good_dir_returns_false_on_empty_dir(self):
        fv = FileValidator()
        result = fv.is_file_in_good_dir('test_statement', '')
        self.assertFalse(result)

    def test_is_file_in_good_dir_returns_false_on_None_dir(self):
        fv = FileValidator()
        result = fv.is_file_in_good_dir('test_statement', '')
        self.assertFalse(result)

    def test_is_file_in_good_dir_returns_false_on_empty_statement(self):
        fv = FileValidator()
        result = fv.is_file_in_good_dir('', 'test_dir')
        self.assertFalse(result)

    def test_is_file_in_good_dir_raises_type_error_on_None_statement(self):
        fv = FileValidator()
        self.assertRaises(TypeError, fv.is_file_in_good_dir, None, 'test_dir')
