[![Build Status](https://travis-ci.org/dev-11/valsys-backend-tech-test.svg?branch=master)](https://travis-ci.org/dev-11/valsys-backend-tech-test)
[![codecov](https://codecov.io/gh/dev-11/valsys-backend-tech-test/branch/master/graph/badge.svg)](https://codecov.io/gh/dev-11/valsys-backend-tech-test)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/0c5c148925e04728a06df0a44d2ab43f)](https://www.codacy.com/manual/dev-11/valsys-backend-tech-test?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=dev-11/valsys-backend-tech-test&amp;utm_campaign=Badge_Grade)

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
