from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.tcase_page import Case_page
from Utlities.read_properties import Read_config
from Utlities.custom_logger import Log_maker
class Test_case_page1:
    url = Read_config.get_url()
    logger = Log_maker.log_gen()
    def test_verify_homepage(self,setup:webdriver):
        self.logger.info("*****************test_verify_hompage******************")
        self.driver = setup
        self.driver.get(self.url)
        wait = WebDriverWait(self.driver,10)
        self.logo = wait.until(EC.visibility_of_element_located((By.XPATH,"//img[@alt='Website for automation practice']")))
        self.clickt =Case_page(self.driver)
        try:
            assert self.logo.is_displayed(),"test case failed"
            print("test case passed : logo diaplayed")
            self.clickt.take_screenshot("testcase")
        except AssertionError:
            self.clickt.take_screenshot("testcase")
            raise
    def test_clicktbtn(self,setup:webdriver):
        self.driver = setup
        self.driver.get(self.url)
        self.clickt = Case_page(self.driver)
        self.clickt.click_testcases()
        self.excepted_url = "https://automationexercise.com/test_cases"
        assert self.driver.current_url == self.excepted_url,"not opened "
        print("Test case page open successfully")
