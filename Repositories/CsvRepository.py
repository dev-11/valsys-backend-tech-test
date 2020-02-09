import csv


class CsvRepository:
    @staticmethod
    def get_headers(file_path):
        with open(file_path, 'r') as read_file:
            csv_reader = csv.reader(read_file, delimiter=',')
            return next(csv_reader)

    @staticmethod
    def get_metadata(file_path):
        with open(file_path, 'r') as read_file:
            csv_reader = csv.reader(read_file, delimiter=',')
            next(csv_reader)
            return next(csv_reader)
