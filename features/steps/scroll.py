from behave import given, when, then
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

from Pages.Base_Page import logger

# Initialize logger



ALL_ARTICLES = (By.CSS_SELECTOR,'[class="SearchResult_searchResult__r_A_s"]')


@then('scroll down {n} times')
def scroll(context, n):
    actions = ActionChains(context.driver)

    # Perform scroll down action using the mouse wheel (or trackpad)
    amount_of_scroll = int(n)
    for i in range(amount_of_scroll):
        actions.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(2)
    articles = context.driver.find_elements(*ALL_ARTICLES)
    logger.info(len(articles))