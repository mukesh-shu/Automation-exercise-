from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.serach_product import Product_search_page
from Pages.add_to_cart import Addto_cart
from Pages.Login1 import Login_correct
from Pages.subscription_cart import Sub_cart
from Utlities.read_properties import Read_config
from Utlities.custom_logger import Log_maker
import time
class Test_search_cart:
    url = Read_config.get_url()
    email = Read_config.get_email()
    password = Read_config.get_password1()
    keyword  = "jeans"
    logger = Log_maker.log_gen()
    def test_verify_search_cart(self,setup:webdriver):
        self.driver = setup
        self.driver.get(self.url)
        #click on products and verify search
        self.product = Product_search_page(self.driver)
        self.product.Click_products()
        self.product.take_screenshot("search_products")
        self.product.click_search(self.keyword)
        self.product.verify_search_products(self.keyword)
        self.product.take_screenshot("search_products")

        #add products into cart
        self.ATC = Addto_cart(self.driver)
        self.ATC.Hover_add_to_cart()
        self.ATC.click_view_cart()
        self.ATC.verify_cart_items()
        self.ATC.take_screenshot("ATC")

        #Click on login
        self.login = Login_correct(self.driver)
        self.login.loginbtn()
        self.login.EnterLogindetails(self.email,self.password)
        self.login.clicklogin()
        self.login.take_screenshot("login")

        time.sleep(2)

        self.ATC2 = Sub_cart(self.driver)
        self.ATC2.click_cart1()
        self.ATC.verify_cart_items()
        self.ATC.take_screenshot("ATC2")







