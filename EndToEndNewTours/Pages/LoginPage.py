from selenium import *


class LoginPage():

    def __init__(self, driver):
        self.driver = driver
        # These are locators of 3 elements

        self.username_textbox_xpath = "//input[@name='userName']"
        self.password_text_xpath = "//input[@name='password']"
        self.signin_click_xpath = "//input[@name='login']"
        self.signon_click_xpath = "//a[contains(text(),'SIGN-ON')]"
        self.register_click_xpath = "//a[contains(text(),'REGISTER')]"
        self.support_click_xpath = "//a[contains(text(),'SUPPORT')]"
        self.contact_click_xpath = "//a[contains(text(),'CONTACT')]"
        self.home_click_xpath = "//a[contains(text(),'Home')]"
        self.flights_click_xpath = "//a[contains(text(),'Flights')]"
        self.hotels_click_xpath = "//a[contains(text(),'Hotels')]"

    def enter_username(self,username):
        self.driver.find_element_by_xpath(self.username_textbox_xpath).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element_by_xpath(self.password_text_xpath).send_keys(password)
    def click_signin(self):
        self.driver.find_element_by_xpath(self.signin_click_xpath).click()




