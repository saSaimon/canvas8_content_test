from selenium.webdriver.common.by import By
from behave import given, when, then


@given('User can enter to the {website}')
def enter_into_website(context,website):
    context.app.login_page.enter_to_website(url=website)


@given('User can login')
def login_to_canvas8(context):
    context.app.login_page.sign_in('sadiqul.alam@canvas8.com', 'SAcanvas8')


@then('Verify Home link is present')
def home_text_is_present(context):
    context.app.home_page.verify_home_text_present()
