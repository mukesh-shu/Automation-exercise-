from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.serach_product import Product_search_page
from Utlities.read_properties import Read_config
from Utlities.custom_logger import Log_maker
class Test_list_search:
    url = Read_config.get_url()
    logger = Log_maker.log_gen()
    keyword = "jeans"
    def test_verify_homepage(self,setup:webdriver):
        self.logger.info("*****************test_verify_hompage******************")
        self.driver = setup
        self.driver.get(self.url)
        self.logo = self.driver.find_element(By.XPATH,"//img[@alt='Website for automation practice']")
        self.prosearch= Product_search_page(self.driver)
        try:
            assert self.logo.is_displayed(),"test case failed"
            print("test case passed : logo diaplayed")
            self.prosearch.take_screenshot("testverifyhomepage ")
        except AssertionError:
            self.prosearch.take_screenshot("verifyhomepage ")
            raise
        self.driver.close()
    def test_product_list_detail(self,setup:webdriver):
        self.driver =setup
        self.driver.get(self.url)
        wait = WebDriverWait(self.driver,10)
        self.prosearch = Product_search_page (self.driver)
        self.prosearch.Click_products()
        self.logger.info("###################verify click products############")
        verify_allproducts = wait.until(EC.visibility_of_element_located((By.XPATH,"//h2[normalize-space()='All Products']")))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", verify_allproducts)
        assert verify_allproducts.is_displayed(),"all products are not shown"
        self.prosearch.take_screenshot("list page")
        print("all products shown successfully")
        self.prosearch.click_search(self.keyword)
        verify_search = wait.until(EC.visibility_of_element_located((By.XPATH,"//h2[normalize-space()='Searched Products']")))
        assert verify_search.is_displayed(),"search keyword have not verifed"
        self.logger.info("%%%%%%%%%%%%%%%%search results%%%%%%%%%%%%%%%%%%%%%")
        self.prosearch.take_screenshot(self.keyword)
        print("verified")
        self.prosearch.verify_search_products(self.keyword)
    