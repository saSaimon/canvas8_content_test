from selenium.webdriver.common.by import By
from behave import given, when, then


@then('User can see the content related to the subject')
def content_page_is_loading(context):
    context.app.content_page.heading_is_not_empty()


@then('Test all articles have content')
def every_article_has_content(context):
    context.app.content_page.test_article_has_heading()

