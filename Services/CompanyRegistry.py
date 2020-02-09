class CompanyRegistry:
    def __init__(self):
        self._companies = ['chipotle', 'mcdonalds', 'microsoft', 'starbucks']

    def is_company_unseen(self, company):
        return company not in self._companies
