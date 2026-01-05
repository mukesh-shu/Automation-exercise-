from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
class Register_wrong:
    signup_btn = "//a[normalize-space()='Signup / Login']"
    name_id = "//input[@placeholder='Name']"
    email_id = "//input[@data-qa='signup-email']"
    signup_submit_btn = "//button[normalize-space()='Signup']"
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)
    def sign_up1(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.signup_btn))).click()
    def enterNameEmail(self,name,email):
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.name_id))).send_keys(name)
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.email_id))).send_keys(email)
    def click_signup(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.signup_submit_btn))).click()
    def take_screenshot(self, name):
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        self.driver.save_screenshot(f"Screenshots/{name}_{timestamp}.png")
         
        
