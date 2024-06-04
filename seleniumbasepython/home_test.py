from seleniumbase import BaseCase

class HomeTest(BaseCase):
    def test_home_page(self):
        #Open website
        self.open("https://www.saucedemo.com/")
        #Assert Page title
        self.assert_title("Swag Labs")

    def test_verify_logo(self):
        #Assert Logo
        self.open("https://www.saucedemo.com/")
        self.assert_element('.login_logo')

    def test_dashboard_login(self):
        self.open('https://www.saucedemo.com/')
        self.type("//input[@id='user-name']",'standard_user')
        self.type("//input[@id='password']",'secret_sauce')
        self.click("//input[@id='login-button']")
        self.wait(3)
        self.assert_element_visible("//div[@class='app_logo']")