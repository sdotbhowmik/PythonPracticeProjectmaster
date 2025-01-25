from seleniumbase import BaseCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class OpenExistingBrowser(BaseCase):
    def setUp(self):
        # Overriding the setUp method to use an existing browser session
        chrome_options = webdriver.ChromeOptions()
        chrome_options.debugger_address = "127.0.0.1:9222"  # Connect to the running Chrome instance
        self.driver = webdriver.Chrome(service=Service(), options=chrome_options)
        super().setUp()

    def test_open_url_in_existing_browser(self):
        # Now you can use SeleniumBase commands with the existing browser instance
        self.open("https://www.subrata.tech")
        self.assert_title("Example Domain")

    def tearDown(self):
        # Overriding the tearDown to avoid closing the existing browser
        pass  # Comment out super().tearDown() to prevent closing the browser

# To run this test, use the following command:
# pytest <name_of_your_test_file>.py
