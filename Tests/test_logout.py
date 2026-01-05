from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.Logout import Logout
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
        self.logout = Logout(self.driver)
        try:
            assert self.logo.is_displayed(),"test case failed"
            print("test case passed : logo diaplayed")
            self.logout.take_screenshot("test_logout")
        except AssertionError:
            self.logout.take_screenshot("test_login")
            raise
        self.driver.close()
    def test_login(self,setup:webdriver):
        self.driver = setup
        self.driver.get(self.url)
        self.logout = Logout(self.driver)
        self.logout.loginbtn()
        self.logger.info("*****************test_verify_logout******************")
        self.verify_login_message = self.driver.find_element(By.XPATH,"//h2[normalize-space()='Login to your account']")
        try:
            assert self.verify_login_message.is_displayed(),"test case failed"
            self.logout.take_screenshot("test_logout")
        except AssertionError:
            self.logout.take_screenshot("test_logintt")
            raise
        self.driver.close()     
    def test_enter_details(self,setup:webdriver):
        self.driver =setup
        self.driver.get(self.url)
        self.logout = Logout(self.driver)
        self.logout.loginbtn()
        self.logout.EnterLogindetails(self.email,self.password)
        self.logout.clicklogin()
        self.logger.info("*****************test_verify_logout******************")
        self.loginas = self.driver.find_element(By.XPATH,"//li[10]//a[1]")
        try:
            assert self.loginas.is_displayed(),"test case failed"
            self.logout.take_screenshot("test_logout")

        except AssertionError:
            self.logout.take_screenshot("test_loginttt")
            raise
        self.driver.close()
    def test_logout(self,setup:webdriver):
        self.driver = setup
        self.driver.get(self.url)
        self.logout =Logout(self.driver)
        self.logout.loginbtn()
        self.logout.EnterLogindetails(self.email,self.password)
        self.logout.clicklogin()
        self.logger.info("*****************test_verify_login******************")
        self.logout.click_logout()
        self.logger.info("*****************test_verify_login******************")

        self.verify_Url = "https://automationexercise.com/login"
        try:
            assert self.driver.current_url == self.verify_Url, "logout page not verified"
            self.logout.take_screenshot("test_logouttt")
            print("Logout page is verified")
        except AssertionError:
            print("Logout page is verified")
            self.logout.take_screenshot("test_logouttt")
            raise
        self.driver.close()
    



