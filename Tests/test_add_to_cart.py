from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utlities.read_properties import Read_config
from Pages.add_to_cart import Addto_cart
from Utlities.custom_logger import Log_maker
import time
class Test_addto_cart:
    url = Read_config.get_url()
    logger = Log_maker.log_gen()
    def test_verify_homepage(self,setup:webdriver):
        self.logger.info("*****************test_home_page******************")
        self.driver = setup
        self.driver.get(self.url)
        self.logo = self.driver.find_element(By.XPATH,"//img[@alt='Website for automation practice']")
        self.ATC= Addto_cart(self.driver)
        try:
            assert self.logo.is_displayed(),"test case failed"
            print("test case passed : logo diaplayed")
            self.ATC.take_screenshot("ATC ")
        except AssertionError:
            self.ATC.take_screenshot("ATC ")
            raise
        time.sleep(4)
        self.ATC.click_products()
        self.ATC.take_screenshot("ATC")
        self.logger.info("*****************test_verify_click_products******************")

        self.ATC.Hover_add_to_cart()
        self.ATC.take_screenshot("ATC ")
        self.logger.info("*****************test_verify_add to cart******************")

        self.ATC.click_view_cart()
        self.ATC.take_screenshot("ATC ")
        self.logger.info("*****************test_verify_view_cart_page******************")

        self.ATC.verify_cart_items()
        self.logger.info("*****************test_verify_cart_items******************")

        self.ATC.take_screenshot("ATC ")

