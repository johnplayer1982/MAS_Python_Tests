from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class mortgageCalc():

    def __init__(self):

        print 'Mortgage Calculator test initialized'

    def runTest(self, url='moneyadviceservice.org.uk', propPrice=340000, deposit=24000):

        url       = url
        pagetitle = 'Money Advice Service'
        propPrice = propPrice
        deposit   = deposit
        delay     = 10

        # Launch firefox
        driver = webdriver.Firefox()

        # Use string substitution to contruct the URL
        driver.get('https://www.%s/en/tools/mortgage-calculator' % url)

        # Confirm the page title contains what we expected
        assert pagetitle in driver.title

        propertyPriceField = driver.find_element_by_id("repayment_price")
        propertyPriceField.send_keys(propPrice)

        depositField = driver.find_element_by_id("repayment_deposit")
        depositField.send_keys(deposit)

        # Submit form
        driver.find_elements_by_class_name("mortgagecalc__submit")[0].click()

