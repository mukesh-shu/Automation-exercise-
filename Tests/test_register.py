import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ECs
from Pages.register import Register
from Utlities.read_properties import Read_config
from Utlities.custom_logger import Log_maker
class Testregister:
    url = Read_config.get_url()
    name = Read_config.get_name()
    password = Read_config.get_password()
    first = Read_config.get_firstname()
    last = Read_config.get_Last_name()
    company = Read_config.get_company()
    Add1 = Read_config.get_Address1()
    Add2 = Read_config.get_Address2()
    state = Read_config.get_state()
    zip = Read_config.get_Zipcode()
    number = Read_config.get_mobilenumber()
    logger = Log_maker.log_gen()
    
    def test_verify_homepage(self,setup:webdriver):
        self.logger.info("*****************test_verify_hompage******************")
        self.driver = setup
        self.driver.get(self.url)
        self.logo = self.driver.find_element(By.XPATH,"//img[@alt='Website for automation practice']")
        assert self.logo.is_displayed(),"test case failed"
        print("test case passed : logo diaplayed")
        self.driver.close()
    def test_click_signup(self,setup:webdriver):
        self.logger.info("*****************test_click_signup_page******************")
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
    def test_enter_user_detail(self, setup):
        self.logger.info("*****************test_enter user details******************")
        self.driver = setup
        self.driver.get(self.url)

        self.register = Register(self.driver)

    # ✅ MUST HAVE ()
        self.register.sign_up1()

        email = Read_config.get_random_email()
        self.register.enterNameEmail(self.name, email)

        self.register.click_signup()
        self.register.enter_details(self.password)
        self.register.enter_dob()
        self.register.check_box()

        self.register.Enter_personal_info(
            self.first,
            self.last,
            self.company,
            self.Add1,
            self.Add2,
            self.state,
            self.zip,
            self.number
        )

        self.register.click_creatbtn()

    
    
        




