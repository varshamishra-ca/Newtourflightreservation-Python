import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
import HtmlTestRunner
import unittest

from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage

class LoginTest(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.driver =  webdriver.Chrome(executable_path ="/Users/sumit/Desktop/CACC Barsha/EndToEndNewTours/drivers/chromedriver")
        cls.driver.implicitly_wait(5)


    def test_login(self):
        driver = self.driver
        driver.get("http://newtours.demoaut.com/")
        titleofloginPage = driver.title
        print(titleofloginPage)

        login= LoginPage(driver)
        login.enter_username("mercury")
        login.enter_password("mercury")
        login.click_signin()
        time.sleep(10)
        print(1)
        titleofHomePage = self.driver.title
        print(titleofHomePage)
        self.assertNotEqual(titleofHomePage,titleofloginPage, "title does not changes")
        driver.get_screenshot_as_file("/Users/sumit/Desktop/CACC Barsha/EndToEndNewTours/screenshots/LoginTestscreenshots/login_page.png")
        logout = HomePage(driver)
        logout.click_signoff()
        time.sleep(5)
        driver.get_screenshot_as_file("/Users/sumit/Desktop/CACC Barsha/EndToEndNewTours/screenshots/LoginTestscreenshots/loggedout_page.png")

    @classmethod
    def tearDownClass(cls):
        print("close")
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/Users/sumit/Desktop/CACC Barsha/EndToEndNewTours/reports/LoginTest reports"))





