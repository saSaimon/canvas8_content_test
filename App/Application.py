from Pages.Login_Page import LoginPage
from Pages.Home_Page import HomePage
from Pages.Content_Page import ContentPage
class Application:

    def __init__(self, driver):
        self.driver = driver
        self.login_page = LoginPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.content_page = ContentPage(self.driver)