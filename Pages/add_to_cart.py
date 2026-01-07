from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
class Addto_cart:
    products = "//a[@href='/products']"
    atc_btn1 = "//div[@class='productinfo text-center']/a[@data-product-id='1' and text()='Add to cart']"
    atc_btn2 = "//div[@class='productinfo text-center']/a[@data-product-id='2' and text()='Add to cart']"
    Con_shp_btn = "//button[normalize-space()='Continue Shopping']"
    view_cart = "//u[normalize-space()='View Cart']"
    rows = "//tbody/tr"
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)
    def click_products(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.products))).click()
    def Hover_add_to_cart(self):
        hover_elemet = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.atc_btn1)))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",hover_elemet)
        ActionChains(self.driver).move_to_element(hover_elemet).click(hover_elemet).perform()
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.Con_shp_btn))).click()
        hover_elemet2 = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.atc_btn2)))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",hover_elemet2)
        ActionChains(self.driver).move_to_element(hover_elemet2).click(hover_elemet2).perform()
    def click_view_cart(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.view_cart))).click()
    def verify_cart_items(self):
        rows = self.wait.until(EC.visibility_of_all_elements_located((By.XPATH,self.rows)))
        assert len(rows) == 2 ,"two qantites are not added"
        print ("Both products are into the cart")
        for row in rows:
            price = int(row.find_element(By.CLASS_NAME,"cart_price").text.replace("Rs.",""))
            qty = int(row.find_element(By.CLASS_NAME,"cart_quantity").text)
            total = int(row.find_element(By.CLASS_NAME,"cart_total").text.replace("Rs.",""))
            assert price * qty == total,"Total price is not correct"
            print("Total price is Correct")
            print(price,qty,total)
    def take_screenshot(self,name):
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        self.driver.save_screenshot(f"Screenshots/{name}_{timestamp}.png")
