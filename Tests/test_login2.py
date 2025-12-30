from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.Login2 import Login_Incorrect
from Utlities.read_properties import Read_config
from Utlities.custom_logger import Log_maker
class Test_login1:
    url = Read_config.get_url()
    email = Read_config.get_email()
    password = Read_config.get_password1()
    logger = Log_maker.log_gen()
    name = Read_config.get_name()
    def test_verify_homepage(self,setup:webdriver):
        self.logger.info("*****************test_verify_hompage******************")
        self.driver = setup
        self.driver.get(self.url)
        self.logo = self.driver.find_element(By.XPATH,"//img[@alt='Website for automation practice']")
        self.login5 = Login_Incorrect(self.driver)
        try:
            assert self.logo.is_displayed(),"test case failed"
            print("test case passed : logo diaplayed")
            self.login5.take_screenshot("test_login")
        except AssertionError:
            self.login5.take_screenshot("test_login")
            raise
        self.driver.close()
    def test_login(self,setup:webdriver):
        self.driver = setup
        self.driver.get(self.url)
        self.login5 = Login_Incorrect(self.driver)
        self.login5.loginbtn()
        self.logger.info("*****************test_verify_login******************")
        self.verify_login_message = self.driver.find_element(By.XPATH,"//h2[normalize-space()='Login to your account']")
        try:
            assert self.verify_login_message.is_displayed(),"test case failed"
            self.login5.take_screenshot("test_login")
        except AssertionError:
            self.login5.take_screenshot("test_login")
            raise
        self.driver.close()     
    def test_enter_details(self,setup:webdriver):
        self.driver =setup
        self.driver.get(self.url)
        self.login5 = Login_Incorrect(self.driver)
        self.login5.loginbtn()
        self.login5.EnterLogindetails(self.email,self.password)
        self.login5.clicklogin()
        self.logger.info("*****************test_verify_login******************")
        self.loginas = self.driver.find_element(By.XPATH,"//p[normalize-space()='Your email or password is incorrect!']")
        try:
            assert self.loginas.is_displayed(),"test case failed"
        except AssertionError:
            self.login5.take_screenshot("test_logout")
            raise
        self.driver.close()
    



