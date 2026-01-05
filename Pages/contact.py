from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
class Contact_us:
    Click_contact ="//a[normalize-space()='Contact us']"
    name = "//input[@placeholder='Name']"
    email = "//input[@placeholder='Email']"
    subject = "//input[@placeholder='Subject']"
    message = "//textarea[@id='message']"
    file = "//input[@name='upload_file']"
    submit_btn = "//input[@name='submit']"
    home_btn = "//span[normalize-space()='Home']"
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)
    def contact_click(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.Click_contact))).click()
    def enter_details(self,name,email,subject,message,file):
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.name))).send_keys(name)
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.email))).send_keys(email)
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.subject))).send_keys(subject)
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.message))).send_keys(message)
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.file))).send_keys(file)
    def submit_bttn(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.submit_btn))).click()
    def home_bttn(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.home_btn))).click()
    def take_screenshot(self, name):
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        self.driver.save_screenshot(f"Screenshots/{name}_{timestamp}.png")
    





        

