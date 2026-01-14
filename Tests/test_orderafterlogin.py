from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.add_to_cart import Addto_cart
from Pages.checkout1 import Checkout
from Pages.Login1 import Login_correct
from Pages.register import Register
from Utlities.custom_logger import Log_maker
from Utlities.read_properties import Read_config
import time
class Test_success_order2:
    url = Read_config.get_url()
    email = Read_config.get_email()
    name = Read_config.get_name()
    password = Read_config.get_password1()
    c_number = Read_config.get_cnumber()
    cvv = Read_config.get_cvv()
    expm = Read_config.get_expiry_month()
    expy = Read_config.get_expiry_year()
    key = Read_config.get_text_area()
    logger = Log_maker.log_gen()
    def test_verify_homepage(self,setup:webdriver):
        self.logger.info("*****************test_verify_hompage******************")
        self.driver = setup
        self.driver.get(self.url)
        self.logo = self.driver.find_element(By.XPATH,"//img[@alt='Website for automation practice']")
        self.register = Register(self.driver)
        try:
            assert self.logo.is_displayed(),"test case failed"
            print("test case passed : logo diaplayed")
            #self.register.take_screenshot(self.name)
        except AssertionError:
            #self.register.take_screenshot(self.name)
            raise
    def test_success_order(self,setup:webdriver):
        self.driver = setup
        self.driver.get(self.url)
        self.login5 = Login_correct(self.driver)
        self.login5.loginbtn()
        self.login5.EnterLogindetails(self.email,self.password)
        self.login5.clicklogin()
        self.cart = Addto_cart(self.driver)
        self.cart.click_products()
        self.cart.Hover_add_to_cart()
        self.cart.click_view_cart()
        self.cart.verify_cart_items()
        self.checkout = Checkout(self.driver)
        self.checkout.click_checkout_btn()
        delivery_raw = self.driver.find_element(By.XPATH,"//ul[@id='address_delivery']").text
        billing_raw = self.driver.find_element(By.XPATH,"//ul[@id='address_invoice']").text
        print("RAW DELIVERY:", repr(delivery_raw))
        print("RAW BILLING:", repr(billing_raw))
        delivery_address = self.checkout.normalize_address(delivery_raw)
        billing_address = self.checkout.normalize_address(billing_raw)
        print("CLEAN DELIVERY:", delivery_address)
        print("CLEAN BILLING:", billing_address)
        assert delivery_address == billing_address,"delivery address and billing address not verified"
        print("verified succesfullly")
        #verification of review your order 
        self.checkout.Verify_review_order()
        self.checkout.click_place_order(self.key)
        self.checkout.enter_card_details(self.name,self.c_number,self.cvv,self.expm,self.expy)
        self.checkout.click_confirm_order()
        time.sleep(2)
        self.del_account = Login_correct(self.driver)
        self.del_account.clickdeleteacc()
        
        

    

