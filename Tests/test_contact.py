from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from Pages.contact import Contact_us
from Utlities.read_properties import Read_config
from Utlities.custom_logger import Log_maker
import time
class Test_contact:
    url = Read_config.get_url()
    name = Read_config.get_name()
    email  = Read_config.get_email()
    subject = Read_config.get_subject()
    messsage = Read_config.get_message()
    file = Read_config.get_file()
    logger = Log_maker.log_gen()
    def test_verify_homepage(self,setup:webdriver):
        self.logger.info("*****************test_verify_hompage******************")
        self.driver = setup
        self.driver.get(self.url)
        wait = WebDriverWait(self.driver,10)
        self.logo = wait.until(EC.visibility_of_element_located((By.XPATH,"//img[@alt='Website for automation practice']")))
        self.contact = Contact_us(self.driver)
        try:
            assert self.logo.is_displayed(),"test case failed"
            print("test case passed : logo diaplayed")
            self.contact.take_screenshot(self.name)
        except AssertionError:
            self.contact.take_screenshot(self.name)
            raise
        self.driver.close()
    def test_contactus(self,setup:webdriver):
        self.driver = setup
        self.driver.get(self.url)
        wait = WebDriverWait(self.driver,10)

        self.contact = Contact_us(self.driver)
        self.contact.contact_click()
        self.verify1 = wait.until(EC.visibility_of_element_located((By.XPATH,"//h2[normalize-space()='Get In Touch']")))
        try:
            assert self.verify1.is_displayed(),"not dispplayed"
            self.contact.take_screenshot(self.name)
            print("verified successfully")
        except AssertionError:
            self.contact.take_screenshot(self.name)
            raise
        self.logger.info("@@@@@@@@@@@@@@@@@@@@@@@@Test_contactus$$$$$$$$$$$$$$$$$$$$$")
    def test_enter_details(self,setup:webdriver):
        self.driver=setup
        self.driver.get(self.url)
        self.contact = Contact_us(self.driver)
        self.contact.contact_click()
        self.contact.enter_details(self.name,self.email,self.subject,self.messsage,self.file)
        self.logger.info("###############Test_verify_submit_button******************")
        self.contact.submit_bttn()
    def test_submit(self,setup:webdriver):
        self.driver =setup
        self.driver.get(self.url)
        wait = WebDriverWait(self.driver,10)
        self.contact = Contact_us(self.driver)
        self.contact.contact_click()

        self.contact.enter_details(self.name,self.email,self.subject,self.messsage,self.file)
        self.logger.info("###############Test_verify_submit_button******************")
        self.contact.submit_bttn()
        wait.until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()
        self.success = wait.until(EC.visibility_of_element_located((By.XPATH,"//span[normalize-space()='Home']")))
        try:
            assert self.success.is_displayed(),"not displayed"
            self.contact.take_screenshot(self.name)
            print("verified successfully")
        except AssertionError:
            self.contact.take_screenshot(self.name)
            raise
        self.contact.home_bttn()
        self.homepage_url = "https://automationexercise.com/"
        assert self.driver.current_url == self.homepage_url,"print not verified"
        print("verified")
        




        

    
        