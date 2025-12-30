from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
class Login_correct:
    Login_btn = "//a[normalize-space()='Signup / Login']"
    Email_id = "//input[@data-qa='login-email']"
    password = "//input[@placeholder='Password']"
    Login_btn2 = "//button[normalize-space()='Login']"
    delete_btn = "//a[normalize-space()='Delete Account']"
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)
    def loginbtn(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.Login_btn))).click()
    def EnterLogindetails(self,email,password1):
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.Email_id))).send_keys(email)
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.password))).send_keys(password1)
    def clicklogin(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.Login_btn2))).click()
    def clickdeleteacc(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.delete_btn))).click()
    def take_screenshot(self, name):
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        self.driver.save_screenshot(f"Screenshots/{name}_{timestamp}.png")

