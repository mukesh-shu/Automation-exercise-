from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
class Sub_home:
    footer = "//div[@class='footer-widget']"
    email = "//input[@id='susbscribe_email']"
    sub_btn ="//button[@id='subscribe']"
    def __init__(self,driver):
        self.driver  = driver
        self.wait = WebDriverWait(driver,10)
    def scrolltofooter(self):
        footer = self.wait.until(EC.visibility_of_element_located((By.XPATH,self.footer)))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",footer)
    def enter_email(self,email):
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.email))).send_keys(email)
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.sub_btn))).click()
    def take_screenshot(self, name):
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        self.driver.save_screenshot(f"Screenshots/{name}_{timestamp}.png")