import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.register import Register
from Utlities.read_properties import Read_config
class Testregister:
    url = Read_config.get_url()
    name = Read_config.get_name()
    def test_verify_homepage(self,setup:webdriver):
        self.driver = setup
        self.driver.get(self.url)
        self.logo = self.driver.find_element(By.XPATH,"//img[@alt='Website for automation practice']")
        assert self.logo.is_displayed(),"test case failed"
        print("test case passed : logo diaplayed")
        self.driver.close()
    def test_click_signup(self,setup:webdriver):
        self.driver = setup
        self.driver.get(self.url)
        self.register = Register(self.driver)
        self.register.sign_up1()
        self.verify = self.driver.find_element(By.XPATH,"//h2[normalize-space()='New User Signup!']")
        assert self.verify.is_displayed(),"signup page is not shown"
        print("sign up page is displayed succesfully")
        email = Read_config.get_random_email()
        self.register.enterNameEmail(self.name,email)
        self.register.click_signup()
        self.verify1 = self.driver.find_element(By.XPATH,"//b[normalize-space()='Enter Account Information']")
        assert self.verify1.is_displayed(),"not opened"
        print("Opened successfully")
        self.driver.close()



