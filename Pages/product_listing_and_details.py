from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
class Product_list_detail:
    Products = "//a[@href='/products']"
    view_product = "//a[@href='/product_details/2']"
    fields = ["//h2[normalize-space()='Men Tshirt']","//p[normalize-space()='Category: Men > Tshirts']",
    "//span[normalize-space()='Rs. 400']","//b[normalize-space()='Availability:']","//b[normalize-space()='Condition:']","//b[normalize-space()='Brand:']"]
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)
    def Click_products(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.Products))).click()
    def click_viewproduct(self):
        product = self.wait.until(EC.visibility_of_element_located((By.XPATH,self.view_product)))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", product)
        product.click()

        for field in self.fields:
            element = self.wait.until(EC.visibility_of_element_located((By.XPATH,field)))
            assert element.is_displayed(),"all details are not shown"
            print("elements are displayed")
    def take_screenshot(self, name):
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        self.driver.save_screenshot(f"Screenshots/{name}_{timestamp}.png")

