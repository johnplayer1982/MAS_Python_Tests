# -----------------------------------------------------------
# import MAS_search as ms
# reload(ms)
# newinst = ms.MASsearch()
# newinst.startSearch(url='<Enter_URL>', term="<Enter_Term>")
# -----------------------------------------------------------

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class MASsearch():

    def __init__(self):

        print 'Search tool initialised'

    def startSearch(self, url='moneyadviceservice.org.uk', term='Benefits'):

        """
        Returns the success of the Money Advice Service Search
        :param url: The MAS environment to test
        :param term: The term to test
        """

        # Specify our URL to test and expected page title
        url = url
        pagetitle = 'Money Advice Service'

        # Search term
        term = term

        # Lowercase version of the search term
        term_lower = term.lower()

        # Time to allow for page load
        delay = 10

        # Launch firefox
        driver = webdriver.Firefox()

        # Use string substitution to contruct the URL
        driver.get('https://www.%s' % url)

        # Confirm the page title contains what we expected
        assert pagetitle in driver.title

        # Find the search field
        elem = driver.find_element_by_id("search")

        # Send the search term to the field
        elem.send_keys(term)

        # Submit the search form
        elem.send_keys(Keys.RETURN)

        # Wait until the search results are present before continuing
        try:
            myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'l-search-results')))

        # If it takes too long
        except TimeoutException:
            print "Loading took too much time!"

        # Create a list of the search results
        searchResults = driver.find_elements_by_css_selector('.search-results__heading > a')

        # Create an empty list to hold the results text
        resultText = []

        # Set a couple of counts for number of results AND how many of those results contain the search term
        resultCount = 0
        containsTermCount = 0

        # For each result in the searchResults (see line 48)
        for results in searchResults:

            # Get the text value
            text = results.text

            # Append the value to the resultText list (see line 51)
            resultText.append(text)

            # Increment the result count
            resultCount += 1

        # For each result in the resultText list (see line 51)
        for results in resultText:

            # If the result contains either the original term or the lowercase equivalent
            if term or term_lower in results:

                # Increment the containsTermCount value
                containsTermCount += 1

        print '%s of the %s results on page 1 contain the search term %s' % (containsTermCount, resultCount, term)
