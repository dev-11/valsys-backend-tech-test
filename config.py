DIRECTORIES_TO_SCAN = [
    'sample_data/balance_sheet/',
    'sample_data/cash_flow_statement/',
    'sample_data/income_statement/'
]

CSV_FILE_EXTENSION = 'csv'

SUPPORTED_METADATA_KEYWORDS = {
    'balance_sheet': 'Current assets',
    'cash_flow_statement': ['Operating', 'activities', 'Operations'],
    'income_statement': ['Income', 'revenues', 'revenue']
}

SUPPORTED_STATEMENT_TYPES = {
    'balance_sheet': 'balance sheet',
    'cash_flow_statement': 'cash flow statement',
    'income_statement': 'income statement'
}
