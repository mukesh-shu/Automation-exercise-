from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
class Verify_qty:
    products = "//a[@href='/products']"
    view_product  = "//div[@class='choose']/ul/li/a[@href='/product_details/43']"
    qty = "//input[@id='quantity']"
    ATC = "//button[normalize-space()='Add to cart']"
    view_cart = "//u[normalize-space()='View Cart']"
    qty_cart = "//td[contains(@class, 'cart_quantity')]/button"


    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)
    def click_product(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.products))).click()
    def click_view_product(self):
        element = self.wait.until(EC.visibility_of_element_located((By.XPATH,self.view_product)))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",element)
        element.click()
        expected_url = "https://automationexercise.com/product_details/43"
        try:
            assert self.driver.current_url == expected_url,"detail page is not opened"
            print("detail page is opened")
        except AssertionError:
            raise
    def click_increase_qty(self,QTY):
        increase_qty = self.wait.until(EC.visibility_of_element_located((By.XPATH,self.qty)))
        increase_qty.clear()
        increase_qty.send_keys(str(QTY))
    def click_add_to_cart(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.ATC))).click()
    def click_view_cart(self,QTY):
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.view_cart))).click()
        Verify_qty_cart = self.wait.until(EC.visibility_of_element_located((By.XPATH,self.qty_cart))).text.strip()
        print(Verify_qty_cart)
        assert Verify_qty_cart == str(QTY) ,"added quantity are not correct"
        print("desired quantity added into cart")
        print(Verify_qty_cart)
    def take_screenshot(self, name):
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        self.driver.save_screenshot(f"Screenshots/{name}_{timestamp}.png")



    

        

