import unittest
from Services import CompanyRegistry


class CompanyRegistryTests(unittest.TestCase):
    def test_is_company_unseen_returns_true_on_new_company(self):
        cr = CompanyRegistry()
        result = cr.is_company_unseen('new company')
        self.assertTrue(result)

    def test_is_company_unseen_returns_true_on_empty_company(self):
        cr = CompanyRegistry()
        result = cr.is_company_unseen('')
        self.assertTrue(result)

    def test_is_company_unseen_returns_true_on_None_company(self):
        cr = CompanyRegistry()
        result = cr.is_company_unseen(None)
        self.assertTrue(result)

    def test_is_company_unseen_returns_false_on_seen_company(self):
        cr = CompanyRegistry()
        result = cr.is_company_unseen('starbucks')
        self.assertFalse(result)
