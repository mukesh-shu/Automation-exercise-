from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
class Product_search_page:
    Products = "//a[@href='/products']"
    view_product = "//a[@href='/product_details/2']"
    search_field = "//input[@id='search_product']"
    search_btn = "//button[@id='submit_search']"
    title = ".productinfo p"
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)
    def Click_products(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.Products))).click()
    def click_search(self,keyword):
        search_bar = self.wait.until(EC.visibility_of_element_located((By.XPATH,self.search_field)))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", search_bar)
        search_bar.clear()
        search_bar.send_keys(keyword)
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.search_btn))).click()
    def verify_search_products(self,keyword):
        product_names = self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,self.title)))
        assert len(product_names) > 0,"no result found"
        for idx, el in enumerate (product_names):
            text = el.text.strip()
            assert keyword.lower() in text.lower(),  \
            f"Result {idx} does not contain,'{keyword}':{text}"
            print("all search keywords contain the search keyword")
    def take_screenshot(self, name):
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        self.driver.save_screenshot(f"Screenshots/{name}_{timestamp}.png")
