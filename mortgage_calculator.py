
# ----------------------------------------------------------------------
# import mortgage_calculator as mc
# reload(mc)
# test = mc.mortgageCalc()
# test.runTest()
# ----------------------------------------------------------------------
# Accepted arguments url,language, property price and deposit amount eg:
# test.runTest(url='qa.dev.mas.local', propPrice=1000000, deposit=45000, lang='cy')
# ----------------------------------------------------------------------

from selenium import webdriver

class mortgageCalc():

    def __init__(self):

        print 'Mortgage Calculator test initialized'

    def runTest(self, url='moneyadviceservice.org.uk', propPrice=340000, deposit=24000, lang='en'):

        """
        Tests the money advice service mortgage calculator tool
        :param url: The url to test, do not include https://www. (eg. preview.dev.mas.local)
        :param propPrice: The property Price
        :param deposit: The deposit amount
        :param lang: The site language, English by default (en|cy)
        """

        en_pagetitle = 'Money Advice Service'
        cy_pagetitle = 'Y Gwasanaeth Cynghori Ariannol'
        url = url
        propPrice = propPrice
        deposit = deposit
        lang = lang

        driver = webdriver.Firefox()

        if lang == 'en':
            driver.get('https://www.%s/%s/tools/mortgage-calculator' % (url, lang))
            assert en_pagetitle in driver.title
        elif lang == 'cy':
            driver.get('https://www.%s/%s/tools/cyfrifiannell-morgais' % (url, lang))
            assert cy_pagetitle in driver.title

        propertyPriceField = driver.find_element_by_id("repayment_price")
        propertyPriceField.send_keys(propPrice)

        depositField = driver.find_element_by_id("repayment_deposit")
        depositField.send_keys(deposit)

        driver.find_elements_by_class_name("mortgagecalc__submit")[0].click()
