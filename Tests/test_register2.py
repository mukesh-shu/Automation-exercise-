from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.register2 import Register_wrong
from Utlities.read_properties import Read_config
from Utlities.custom_logger import Log_maker
class Test_register2:
    url = Read_config.get_url()
    name = Read_config.get_name()
    email = Read_config.get_email()
    logger = Log_maker.log_gen()
    def test_verify_homepage(self,setup:webdriver):
        self.logger.info("*****************test_verify_hompage******************")
        self.driver = setup
        self.driver.get(self.url)
        self.logo = self.driver.find_element(By.XPATH,"//img[@alt='Website for automation practice']")
        self.register = Register_wrong(self.driver)
        try:
            assert self.logo.is_displayed(),"test case failed"
            print("test case passed : logo diaplayed")
            self.register.take_screenshot(self.name)
        except AssertionError:
            self.register.take_screenshot(self.name)
            raise
        self.driver.close()
    def test_click_signup(self,setup:webdriver):
        self.logger.info("*****************test_click_signup_page******************")
        self.driver = setup
        self.driver.get(self.url)
        self.register = Register_wrong(self.driver)
        self.register.sign_up1()
        self.verify = self.driver.find_element(By.XPATH,"//h2[normalize-space()='New User Signup!']")
        try:
            assert self.verify.is_displayed(),"signup page is not shown" 
            print("sign up page is displayed succesfully")
        except AssertionError:
            self.register.take_screenshot(self.name)
            raise
        self.register.enterNameEmail(self.name,self.email)
        self.register.click_signup()
        self.verify1 = self.driver.find_element(By.XPATH,"//p[normalize-space()='Email Address already exist!']")
        assert self.verify1.is_displayed(),"email is not registered"
        self.register.take_screenshot(self.name)

        print("Email already registered successfully")

