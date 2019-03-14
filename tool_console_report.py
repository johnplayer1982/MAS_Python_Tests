from selenium import webdriver
from os.path import expanduser
import csv

class testTools():

    def __init__(self):

        print 'Testing all tools'

    def runtest(self, url='preview.dev.mas.local'):

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
        globalCount = 0

        for tool in tools:

            print '\n' + 'Checking %s' % tool

            errorCount = 0
            warningCount = 0

            tool_path = 'https://www.%s/en/tools/%s' % (url, tool)
            driver.get(tool_path)

            for entry in driver.get_log('browser'):

                if entry['level'] == "SEVERE":
                    errorCount += 1
                    globalCount += 1
                elif entry['level'] == "WARNING":
                    warningCount += 1
                    globalCount += 1

                entry = entry['message']
                print entry
                results.update({tool: entry})

            print errorCount, 'errors found'
            print warningCount, 'warnings found'

        print '\nTotal Errors and Warnings:', globalCount

        driver.close()
