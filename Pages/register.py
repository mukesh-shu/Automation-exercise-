from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

class Register:
    signup_btn = "//a[normalize-space()='Signup / Login']"
    name_id = "//input[@placeholder='Name']"
    email_id = "//input[@data-qa='signup-email']"
    signup_submit_btn = "//button[normalize-space()='Signup']"
    gender = "//input[@id='id_gender1']"
    password = "//input[@id='password']"
    day = "//select[@id='days']"
    month = "//select[@id='months']"
    year = "//select[@id='years']"
    newsletter = "//input[@id='newsletter']"
    offer = "//input[@id='optin']"
    firstname = "//input[@id='first_name']"
    Last_name = "//input[@id='last_name']"
    Company = "//input[@id='company']"
    Address1 = "//input[@id='address1']"
    Address2 = "//input[@id='address2']"
    country = "//select[@id='country']"
    cit = "//input[@id='city']"
    State = "//input[@id='state']"
    Zipcode = "//input[@id='zipcode']"
    mobile_number = "//input[@id='mobile_number']"
    create_btn  = "//button[normalize-space()='Create Account']"
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
    def enter_details(self,password):
        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.gender))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.password))).send_keys(password)
    def enter_dob(self):
        Select(self.wait.until(EC.visibility_of_element_located((By.XPATH, self.day)))).select_by_visible_text("10")
        Select(self.wait.until(EC.visibility_of_element_located((By.XPATH, self.month)))).select_by_visible_text("June")
        Select(self.wait.until(EC.visibility_of_element_located((By.XPATH, self.year)))).select_by_visible_text("2002")
    def check_box(self):
       check_box1 = self.wait.until(EC.visibility_of_element_located((By.XPATH,self.newsletter)))
       self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});",check_box1)
       self.wait.until(EC.visibility_of_element_located((By.XPATH,self.offer))).click()
    def Enter_personal_info(self,first,last,company,Add1,Add2,state,city,Zip,number):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.firstname))).send_keys(first)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.Last_name))).send_keys(last)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.Company))).send_keys(company)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.Address1))).send_keys(Add1)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.Address2))).send_keys(Add2)
        Select(self.wait.until(EC.visibility_of_element_located((By.XPATH,self.country)))).select_by_visible_text("India")
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.State))).send_keys(state)
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.cit))).send_keys(city)
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.Zipcode))).send_keys(Zip)
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.mobile_number))).send_keys(number)
    def click_creatbtn(self):
        element = self.wait.until(EC.visibility_of_element_located((By.XPATH,self.create_btn)))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",element)
        element.click()


    def take_screenshot(self, name):
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        self.driver.save_screenshot(f"Screenshots/{name}_{timestamp}.png")

        
        
        
        
        