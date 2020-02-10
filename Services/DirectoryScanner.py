import os
import config


class DirectoryScanner:
    def __init__(self, directories, company_registry):
        self._directories = directories
        self._company_registry = company_registry

    def scan_new_files(self):
        news = []
        for current_dir in self._directories:
            for file in os.listdir(current_dir):
                if file[0] != '.':  # skipping hidden files
                    filename, extension = file.split('.')
                    if extension == config.CSV_FILE_EXTENSION and self._company_registry.is_company_unseen(filename):
                        news.append([current_dir + file, filename])
        return news
