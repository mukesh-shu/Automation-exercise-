from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
class Case_page:
    test_case_btn ="//div[@class='item active']//button[@type='button'][normalize-space()='Test Cases']"
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)
    def click_testcases(self):
        element = self.wait.until(EC.visibility_of_element_located((By.XPATH,self.test_case_btn)))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        element.click()

    def take_screenshot(self, name):
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        self.driver.save_screenshot(f"Screenshots/{name}_{timestamp}.png")