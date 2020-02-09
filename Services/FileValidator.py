import config


class FileValidator:
    _header_length = 3
    _balance_sheet = 'balance_sheet'
    _cache_flow_statement = 'cache_flow_statement'
    _income_statement = 'income_statement'

    def is_file_structure_valid(self, header):
        return False if not header else len(header) == self._header_length

    def get_statement_type(self, data):
        desc = data[1].lower()
        key = None

        if self._is_balanced_sheet(desc):
            key = self._balance_sheet
        elif self._is_description_in_list(self._cache_flow_statement, desc):
            key = self._cache_flow_statement
        elif self._is_description_in_list(self._income_statement, desc):
            key = self._income_statement

        return 'unknown statement' if key is None else config.SUPPORTED_STATEMENT_TYPES[key]

    def _is_balanced_sheet(self, desc):
        return config.SUPPORTED_METADATA[self._balance_sheet].lower() in desc

    @staticmethod
    def _is_description_in_list(key, desc):
        return any([s for s in config.SUPPORTED_METADATA[key] if s.lower() in desc])

    @staticmethod
    def is_file_in_good_dir(statement_type, path):
        return False if statement_type == '' else statement_type in path
