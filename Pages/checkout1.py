from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import re
class Checkout:
    Checkout_btn = "//a[normalize-space()='Proceed To Checkout']"
    register_btn = "//u[normalize-space()='Register / Login']"
    deliver_address = "//ul[@id='address_delivery']"
    billing_address = "//ul[@id='address_invoice']"
    text_area = "//textarea[@name='message']"
    place_order = "//a[normalize-space()='Place Order']"
    name = "//input[@name='name_on_card']"
    card_no = "//input[@name='card_number']"
    CV = "//input[@placeholder='ex. 311']"
    expiry_date = "//input[@placeholder='MM']"
    expiry_year = "//input[@placeholder='YYYY']"
    pay_confirm_order = "//button[@id='submit']"
    confirm_order = "//b[normalize-space()='Order Placed!']"
    continue_btn = "//a[normalize-space()='Continue']"
    row ="//div[@id='cart_info']//tr[td]"
    download_invoice = "//a[normalize-space()='Download Invoice']"

    Total_amount = "//tbody/tr/td[4]/p[1]"
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)
    def click_checkout_btn(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.Checkout_btn))).click()
    def click_register_btn(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.register_btn))).click()
    
    def normalize_address(self,text):
        lines = text.split("\n")
        address_lines = lines[1:]   # skip "YOUR DELIVERY ADDRESS" / "YOUR BILLING ADDRESS"
        cleaned = [line.strip() for line in address_lines if line.strip()]
        return "\n".join(cleaned)
    def click_place_order(self,key):
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.text_area))).send_keys(key)
        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.place_order))).click()
    def enter_card_details(self, name,c_number,cvv,expm,expy):
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.name))).send_keys(name)
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.card_no))).send_keys(c_number)
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.CV))).send_keys(cvv)
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.expiry_date))).send_keys(expm)
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.expiry_year))).send_keys(expy)
    def click_confirm_order(self):
        success_order = self.wait.until(EC.visibility_of_element_located((By.XPATH,self.pay_confirm_order)))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",success_order)
        success_order.click()
        invoice = self.wait.until(EC.visibility_of_element_located((By.XPATH,self.download_invoice)))
        self.driver.execute_script("argu,ments[0].scrollIntoView({block: 'center'});",invoice)
        invoice.click()
        confirm_order = self.wait.until(EC.visibility_of_element_located((By.XPATH,self.confirm_order)))
        assert confirm_order.is_displayed(),"order is not placed"
        print("order placed succesfully")
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.continue_btn))).click()
    def Verify_review_order(self):
        rows = self.wait.until(
            EC.visibility_of_all_elements_located((By.XPATH, self.row))
        )

        Total = int(
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self.Total_amount))
            ).text.replace("Rs.", "").strip()
        )

        calculated_total = 0

        for row in rows:
            tds = row.find_elements(By.TAG_NAME, "td")
            if len(tds) < 5:
                continue

            price_text = tds[2].text.strip()

            # 🚨 THIS IS THE KEY LINE
            if not re.search(r"\d", price_text):
                continue   # skips "Price" header row forever

            title = tds[1].text
            price = int(re.sub(r"\D", "", price_text))
            qty = int(re.sub(r"\D", "", tds[3].text))
            total = int(re.sub(r"\D", "", tds[4].text))

            calculated_total += price * qty
            print(title, price, qty, total)

        assert calculated_total == Total, \
            f"Expected total {calculated_total}, but found {Total}"

        print(f"Total amount verified successfully: Rs. {Total}")

    def continue_btnn(self):
       Con_btn =  self.wait.until(EC.element_to_be_clickable((By.XPATH,self.continue_btn)))
       self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",Con_btn)
       Con_btn.click()
    def take_screenshot(self, name):
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        self.driver.save_screenshot(f"Screenshots/{name}_{timestamp}.png")


    



        



        