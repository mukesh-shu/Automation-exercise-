from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Scroll_up:
    bottom = "//div[@class='footer-widget']"
    Subscription  = "//h2[normalize-space()='Subscription']"
    arrow = "//i[@class='fa fa-angle-up']"
    title = "//div[@class='item active']//h2[contains(text(),'Full-Fledged practice website for Automation Engin')]"
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)
    def scroll_bottom(self):
        bottom = self.wait.until(EC.visibility_of_element_located((By.XPATH,self.bottom)))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",bottom)
    def verify_subscription(self):
        sub  = self.wait.until(EC.visibility_of_element_located((By.XPATH,self.Subscription)))
        assert sub.is_displayed(),"subscription is not displayed"
        print("subscripiton displayed succesfully")
    def Click_scroll_up(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.arrow))).click()
        title = self.wait.until(EC.presence_of_element_located((By.XPATH,self.title)))
        assert title.is_displayed(),"page scroll up not succesfully"
        print("page scroll up successfully")

