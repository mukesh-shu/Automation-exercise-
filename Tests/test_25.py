from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.arrow import Scroll_up
from Utlities.read_properties import Read_config
from Utlities.custom_logger import Log_maker
import time
class Test_scroll_up:
    url = Read_config.get_url()
    logger = Log_maker.log_gen()
    def test_verify_homepage(self,setup:webdriver):
        self.logger.info("*****************test_verify_hompage******************")
        self.driver = setup
        self.driver.get(self.url)
        self.logo = self.driver.find_element(By.XPATH,"//img[@alt='Website for automation practice']")
      
        assert self.logo.is_displayed(),"test case failed"
        print("test case passed : logo diaplayed")
           
        self.Up = Scroll_up(self.driver)
        self.Up.scroll_bottom()
        time.sleep(2)
        self.Up.verify_subscription()
        time.sleep(2)
        self.Up.Click_scroll_up()
        time.sleep(5)

    

    