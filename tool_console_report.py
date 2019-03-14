from selenium import webdriver
import pprint

class testTools():

    def __init__(self):

        print 'Testing all tools'

    def runtest(self, url='moneyadviceservice.org.uk', lang='en'):

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

        driver = webdriver.Chrome('/Users/johnplayer/chromedriver')

        for tool in tools:

            print 'Testing %s for console errors' % tool
            toolPath = 'https://www.%s/%s/tools/%s' % (url, lang, tool)
            driver.get(toolPath)

            for entry in driver.get_log('browser'):
                print 'ERROR:', entry['message'], '\nSOURCE:', entry['source'], '\n'


        driver.close()
