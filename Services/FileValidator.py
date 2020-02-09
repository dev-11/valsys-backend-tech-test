import config


class FileValidator:
    _header_length = 3
    _balance_sheet = 'balance_sheet'
    _cache_flow_statement = 'cache_flow_statement'
    _income_statement = 'income_statement'

    def is_file_structure_valid(self, data):
        return len(data[0]) == self._header_length

    def get_file_type(self, data):
        desc = data[1].lower()

        if self._is_balanced_sheet(desc):
            return config.SUPPORTED_TYPES[self._balance_sheet]

        if self._is_description_in_list(self._cache_flow_statement, desc):
            return self._cache_flow_statement

        if self._is_description_in_list(self._income_statement, desc):
            return self._income_statement

        return 'unknown type'

    def _is_balanced_sheet(self, desc):
        return config.SUPPORTED_METADATA[self._balance_sheet] in desc

    @staticmethod
    def _is_description_in_list(key, desc):
        matching = [s for s in config.SUPPORTED_METADATA[key] if s in desc]
        return len(matching) > 0

    @staticmethod
    def is_file_in_good_dir(file_type, path):
        return file_type in path