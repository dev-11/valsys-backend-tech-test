import collections

ScannedFileResult = collections.namedtuple('ScannedFileResult',
                                           'path statement_type company is_file_in_good_dir is_valid')
