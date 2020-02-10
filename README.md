[![Build Status](https://travis-ci.org/dev-11/valsys-backend-tech-test.svg?branch=master)](https://travis-ci.org/dev-11/valsys-backend-tech-test)
[![codecov](https://codecov.io/gh/dev-11/valsys-backend-tech-test/branch/master/graph/badge.svg)](https://codecov.io/gh/dev-11/valsys-backend-tech-test)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/0c5c148925e04728a06df0a44d2ab43f)](https://www.codacy.com/manual/dev-11/valsys-backend-tech-test?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=dev-11/valsys-backend-tech-test&amp;utm_campaign=Badge_Grade)

---

## The approach

The solution scans the directories which are defined in the `config.py` and looks for unseen company files. A company is considered to be unseen if the `CompanyRegistry` service doesn't recognise it as a known company. If the `DirectoryScanner` finds a new file the `FileValidator` will do a rudimentary check on it, like do we have enough header to process it later, what kind of keywords are present in the `line item` column of the first data row, and what is the path to the file. Based on these validaton checks the system will try to tell the statement type, and is the file in the right folder or not (for example is the balance sheet in the balance sheet folder or not). Once we have processed every new file it will be available in a collection, and the system will print out the collected information about them. The whole workflow is controlled in the `main()` method which behaves like a controller function.

### Improvements
Right now the `CompanyRegistry` uses a baked-in list to check is a company unseen or not. In the future I would change that so we can add new companies to the list after every directory scan. The keywors used for determining the statement types are also baked in, that also should be a _live_ dictionary which can have new values. To determine what is keyword and what is not is also an interseting question to solve. The keyword check should be done on the whole file, not just on the first data row. The directory scan is triggered manually instead of an event which in a real life could be file system changed event, in a lambda. The result list of the scan could also be grouped by company and statement type. 

In general I would change the application from the POC approach to a real life, production ready approach. 

---

## Technical test


**Background:** We ingest a large amount of data across many different companies and time periods. One of the first challenges you face when trying to organise large chunks of files is identifying the main components. In financial statements, the 3 main file types are the income statement, balance sheet and cash flow statement. Each of these (typically) have unique properties.


**The challenge:** Write a program that allows you to categorise the different types of statements found in the sample data folder. The three child folders (income statement, balance sheet, cash flow statement) are the statement types your program will need to identify. The format is "/sample_data/statement_type/company_filing.csv". Once completed, your program should be able to identify an unseen company's filing by stating whether it is an income statement, balance sheet or cash flow statement. Each of the folders in /sample_data contain example files which you will need to analyse in order to identify the differences between the file types; rely on anything you can think of to try and identify the filings (short of matching the file path)! The challenge should be written either in Python or Golang.


**What we’ll be assessing:**

- Functionality - does it work?

- File structure and design patterns

- Data structures

- Dependencies

**Improvements:**
Given more time, what improvements (if any) would you make to your code? Please include this in your repository.

## Submitting
When you're ready to submit, upload the repository to a code hosting service like Github or Bitbucket and share it with us!
