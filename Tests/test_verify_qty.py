from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.verify_quantity import Verify_qty
from Utlities.custom_logger import Log_maker
from Utlities.read_properties import Read_config
import time
class Test_verify_QTY:
    url = Read_config.get_url()
    logger = Log_maker.log_gen()
    QTY = "4"
    def test_verify_homepage(self,setup:webdriver):
        self.logger.info("*****************test_home_page******************")
        self.driver = setup
        self.driver.get(self.url)
        self.logo = self.driver.find_element(By.XPATH,"//img[@alt='Website for automation practice']")
        self.vQTY= Verify_qty(self.driver)
        try:
            assert self.logo.is_displayed(),"test case failed"
            print("test case passed : logo diaplayed")
            self.vQTY.take_screenshot("QTY ")
        except AssertionError:
            self.vQTY.take_screenshot("QTY ")
            raise
        self.driver.close()
    def test_verify_qty(self,setup:webdriver):
        self.driver = setup
        self.driver.get(self.url)
        self.vQTY = Verify_qty(self.driver)
        self.vQTY.click_product()
        self.logger.info("*******************click_products************")
        self.vQTY.take_screenshot("VQTY")
        self.vQTY.click_view_product()
        self.vQTY.click_increase_qty(self.QTY)
        self.vQTY.click_add_to_cart()
        self.vQTY.click_view_cart(self.QTY)
        self.logger.info("****************verify cart_page***********")
        self.vQTY.take_screenshot("vQty")
