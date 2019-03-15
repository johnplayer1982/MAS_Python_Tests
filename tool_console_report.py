from selenium import webdriver
from os.path import expanduser
import pprint
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

        pages = {
            "",
            "categories/tools-and-calculators",
            "users/sign_in",
            "users/sign_up",
            "categories/debt-and-borrowing",
            "articles/how-much-rent-can-you-afford",
            "corporate/about-us",
            "corporate/media-centre",
            "corporate_categories/partners",
            "corporate_categories/our-debt-work",
            "corporate/jobs",
            "corporate/contact-us",
            "corporate/terms-and-conditions",
            "corporate/privacy",
            "corporate/accessibility",
            "corporate/cookie_notice_en",
            "sitemap"
        }

        home = expanduser("~")
        driver = webdriver.Chrome(home + '/chromedriver')
        results = {}
        globalCount = 0

        for tool in tools:

            tool_path = 'https://www.%s/en/tools/%s' % (url, tool)
            driver.get(tool_path)

            print '\n' + 'Checking %s (%s)' % (tool, tool_path)

            errorCount = 0
            warningCount = 0

            for entry in driver.get_log('browser'):

                if entry['level'] == "SEVERE":
                    errorCount += 1
                    globalCount += 1
                elif entry['level'] == "WARNING":
                    warningCount += 1
                    globalCount += 1

                entry = entry['message']
                print entry
                results.update({tool_path: entry})

            print errorCount, 'errors found'
            print warningCount, 'warnings found'

        for page in pages:

            page_path = 'https://www.%s/en/%s' % (url, page)
            driver.get(page_path)
            print '\n' + 'Checking %s (%s)' % (page, page_path)

            errorCount = 0
            warningCount = 0

            for entry in driver.get_log('browser'):

                if entry['level'] == "SEVERE":
                    errorCount += 1
                    globalCount += 1
                elif entry['level'] == "WARNING":
                    warningCount += 1
                    globalCount += 1

                entry = entry['message']
                print entry

                results.update({page_path: entry})

            print errorCount, 'errors found'
            print warningCount, 'warnings found'

        print '\nTotal Errors and Warnings:', globalCount

        pprint.pprint(results)

        f = open("output.txt" , "w+")
        f.write('%s \n' % results)

        driver.close()
