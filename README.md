# Selenium Tests for Money Advice Service

A bunch of selenium tests.

## Dependencies

- Firefox Selenium IDE
- Python 2.7
- PyCharm (Recommended IDE)

## Tools

### MAS_search

Run from the Python console.  Accepts 2 arguments, Default values are 
specified in the function should no arguments be provided:

- url = The URL to test
- term = The term to test

```
import MAS_search as ms
reload(ms)
newinst = ms.MASsearch()
newinst.startSearch(url='<Enter_URL>', term="<Enter_Term>")
```

Performs the search and returns the number of instances of the term in
the results in the python console.

### tool_console_report

Hits the first page of each tool and reports console output.

Dependencies : Please place the chromedriver (http://chromedriver.chromium.org) in your home directory (/Users/yourname/chromedriver)

Accept arguments:

- url = The URL to test


```
import tool_console_report as tcr
reload(tcr)
newtest = tcr.testTools()
newtest.runtest(url='<Enter_URL>')
```
