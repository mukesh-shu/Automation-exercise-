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