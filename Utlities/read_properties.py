import configparser
import time
import os
config = configparser.RawConfigParser()
config_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "Configuration",
    "config.ini"
)
if not config.read(config_path):
    raise FileNotFoundError(f"Config file not found at {config_path}")
config.read(config_path)
class Read_config:
    @staticmethod
    def get_url():
        return config.get("Register",'url')
    staticmethod
    def get_name():
        return config.get("Register",'name')
    @staticmethod
    def get_random_email():
           base_email = config.get("Register", "base_email")
           domain = config.get("Register", "domain")

           unique_value = int(time.time())   # always unique
           return f"{base_email}{unique_value}{domain}"
    @staticmethod
    def get_password():
        return config.get("Register",'password')
    @staticmethod
    def get_firstname():
        return config.get("Register",'firstname')
    @staticmethod
    def get_Last_name():
         return config.get("Register",'Last_name')
    @staticmethod
    def get_company():
        return config.get("Register",'company')
    @staticmethod
    def get_Address1():
        return config.get("Register",'Address1')
    @staticmethod
    def get_Address2():
         return config.get("Register",'Address2')
    @staticmethod
    def get_state():
         return config.get("Register",'state')
    @staticmethod
    def get_Zipcode():
         return config.get("Register",'Zipcode')
    @staticmethod
    def get_mobilenumber():
         return config.get("Register",'mobile_number')
    ##password = Testing@123'''
'''stname = tuka Ram bhide
Last_name =  bhide
Company = e commerce
Address1 = laptop street
Address2 = pc street
State = jaipur
Zipcode = 302022
mobile_number = 94513864 '''
              