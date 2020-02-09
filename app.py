import sys
import Services
import Repositories
import config
import Entities


def main():
    # scan folders DONE
    # identify new files in folder DONE
    # verify file is in correct folder
    # print result

    scanner = Services.DirectoryScanner(config.DIRECTORIES_TO_SCAN, Services.CompanyRegistry())
    repo = Repositories.CsvRepository()
    file_validator = Services.FileValidator()
    new_files = []

    for new_file in scanner.scan_new_files():
        file, company = new_file
        metadata = repo.get_metadata(file)
        headers = repo.get_headers(file)
        statement_type = file_validator.get_statement_type(metadata)
        is_file_structure_valid = file_validator.is_file_structure_valid(headers)
        is_file_in_good_dir = file_validator.is_file_in_good_dir(statement_type, file)
        new_files.append(Entities.ScannedFileResult(file, statement_type, company, is_file_in_good_dir,
                                                    is_file_structure_valid))

    print(f'new files of unseen companies: {len(new_files)}')
    for new_file in new_files:
        print(f'\n'
              f'company: {new_file.company}\n'              
              f'file path: {new_file.path}\n'
              f'statement type: {new_file.statement_type}\n'
              f'is file in good dir: {new_file.is_file_in_good_dir}\n'
              f'is file valid: {new_file.is_valid}')


if __name__ == '__main__':
    sys.exit(main())
