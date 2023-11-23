from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from App.Application import Application
from selenium.webdriver.support.wait import WebDriverWait

# behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/bestsellers.feature

def browser_init(context):
    """
    :param context: Behave context
    """
    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Firefox(service=service)


    """with chrome"""
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)
    # context.driver.maximize_window()

    """new chrome driver calling option"""
    context.driver = webdriver.Chrome()



    # driver_path = GeckoDriverManager().install()  # Use GeckoDriverManager for Firefox
    # context.driver = webdriver.Firefox(executable_path=driver_path)  # Use Firefox WebDriver here

    """### OTHER BROWSERS ###"""
    # service = Service(executable_path='/Users/svetlanalevinsohn/careerist/15-python-selenium-automation/geckodriver')
    # context.driver = webdriver.Firefox(service=service)
    # context.driver = webdriver.Safari()

    """### HEADLESS MODE ####"""
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    #
    # context.driver = webdriver.Chrome(
    #     options=options
    # )


    """### BROWSERSTACK ###"""
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    # bs_user = ''
    # bs_key = ''
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    # bstack_options = {
    #     'os': 'Windows',
    #     'osVersion': '10',
    #     'browserName': 'Firefox',
    #     'sessionName': scenario_name
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)

    context.driver.maximize_window()
    # context.driver.set_window_size(2024, 200200)
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()