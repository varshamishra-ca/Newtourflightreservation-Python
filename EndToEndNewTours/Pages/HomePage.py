class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.signoff_click_xpath ="//a[contains(text(),'SIGN-OFF')]"
        self.itinenary_click_xpath ="//a[contains(text(),'ITINERARY')]"
        self.profile_click_xpath = "//a[contains(text(),'PROFILE')]"
        self.support_click_xpath = "//a[contains(text(),'SUPPORT')]"


    def click_signoff(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath(self.signoff_click_xpath).click()