from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.subscription_cart import Sub_cart
from Utlities.read_properties import Read_config
from Utlities.custom_logger import Log_maker
class Test_sub_cart:
    url = Read_config.get_url()
    logger = Log_maker.log_gen()
    email = Read_config.get_email()
    def test_verify_homepage(self,setup:webdriver):
        self.logger.info("*****************test_verify_hompage******************")
        self.driver = setup
        self.driver.get(self.url)
        self.logo = self.driver.find_element(By.XPATH,"//img[@alt='Website for automation practice']")
        self.subscription= Sub_cart(self.driver)
        try:
            assert self.logo.is_displayed(),"test case failed"
            print("test case passed : logo diaplayed")
            self.subscription.take_screenshot("testverifyhomepage ")
        except AssertionError:
            self.subscription.take_screenshot("verifyhomepage ")
            raise
        self.driver.close()
    def test_verify_subscritpion(self,setup:webdriver):
        self.driver = setup
        self.driver.get(self.url)
        self.subscription = Sub_cart(self.driver)
        self.subscription.click_cart1()
        self.subscription.scrolltofooter()
        self.subscription.enter_email(self.email)
        alert_Success  = self.driver.find_element(By.CSS_SELECTOR,".alert-success.alert")
        assert alert_Success.is_displayed(),"not displayed"
        self.subscription.take_screenshot("subscription")
        print("verified successfully")