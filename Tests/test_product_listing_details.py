from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.product_listing_and_details import Product_list_detail
from Utlities.read_properties import Read_config
from Utlities.custom_logger import Log_maker
class Test_list_detail:
    url = Read_config.get_url()
    logger = Log_maker.log_gen()
    def test_verify_homepage(self,setup:webdriver):
        self.logger.info("*****************test_verify_hompage******************")
        self.driver = setup
        self.driver.get(self.url)
        self.logo = self.driver.find_element(By.XPATH,"//img[@alt='Website for automation practice']")
        self.prodet= Product_list_detail(self.driver)
        try:
            assert self.logo.is_displayed(),"test case failed"
            print("test case passed : logo diaplayed")
            self.prodet.take_screenshot("testverifyhomepage ")
        except AssertionError:
            self.prodet.take_screenshot("verifyhomepage ")
            raise
        self.driver.close()
    def test_product_list_detail(self,setup:webdriver):
        self.driver =setup
        self.driver.get(self.url)
        wait = WebDriverWait(self.driver,10)
        self.prodet= Product_list_detail(self.driver)
        self.prodet.Click_products()
        self.logger.info("###################verify click products############")
        verify_allproducts = wait.until(EC.visibility_of_element_located((By.XPATH,"//h2[normalize-space()='All Products']")))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", verify_allproducts)
        assert verify_allproducts.is_displayed(),"all products are not shown"
        self.prodet.take_screenshot("list page")
        print("all products shown successfully")
        self.prodet.Click_products()
        self.logger.info("#################click products $$$$$$$$$$$$$$$")
        self.prodet.click_viewproduct()
        self.expected_url = "https://automationexercise.com/product_details/2"
        assert self.driver.current_url == self.expected_url,"print not opened "
        print("detail page opened successfully")
        self.logger.info("#################verify detail $$$$$$$$$$$$$$$")

        self.prodet.take_screenshot("detail page")






    