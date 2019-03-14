from selenium import webdriver
from os.path import expanduser
import pprint
import csv

class testTools():

    def __init__(self):

        print 'Testing all tools'

    def runtest(self, url='moneyadviceservice.org.uk'):

        tools = {
            "mortgage-calculator",
            'house-buying/stamp-duty-calculator',
            "house-buying/mortgage-affordability-calculator",
            "pension-calculator",
            "annuities",
            "workplace-pension-contribution-calculator",
            "budget-planner",
            "debt-test",
            "savings-calculator",
            "savings-calculator/how_long",
            "savings-calculator/how_much",
            "loan-calculator",
            "car-costs-calculator",
            "credit-card-calculator",
            "quick-cash-finder",
            "redundancy-pay-calculator",
            "christmas-money-planner",
            "compare-bank-account-fees-and-charges",
            "health-check"
        }

        home = expanduser("~")
        driver = webdriver.Chrome(home + '/chromedriver')
        results = {}

        for tool in tools:

            print 'Testing %s for console errors' % tool
            toolPath = 'https://www.%s/en/tools/%s' % (url, tool)
            driver.get(toolPath)

            for entry in driver.get_log('browser'):
                print 'ERROR:', entry['message'], '\nSOURCE:', entry['source'], '\n'
                results.update({tool: entry})

        print pprint.pprint(results)

        file_path = home + '/console_results.csv'

        with open(file_path, 'wb') as f:
            w = csv.DictWriter(f, results.keys())
            w.writeheader()
            w.writerow(results)

        driver.close()
