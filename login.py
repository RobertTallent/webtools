from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from credentials import Credentials

option = webdriver.FirefoxOptions()
option.binary_location = r'C:\Users\tallent_robert\AppData\Local\Mozilla Firefox\firefox.exe'
driverService = Service(r'C:\Users\tallent_robert\AppData\Local\Programs\Python\Python310\geckodriver.exe')
#settings = ("download.default_directory": "C:", 'safebrowsing.enabled': 'false')
#option.add_experimental_option('prefs',down)
driver = webdriver.Firefox(service=driverService, options=option)
standby = WebDriverWait(driver,10)

class Login:
    def __init__(self, login_url, username_element, password_element):
        Credentials()
        self.login_url = login_url
        self.username_element = username_element
        self.password_element = password_element
        #self.submit_button = submit_button
        self.username = Credentials.usrnm
        self.password = Credentials.pw
        driver.get(self.login_url)
        type_username = driver.find_element(By.ID,self.username_element)
        type_username.send_keys(self.username)
        type_password = driver.find_element(By.ID,self.password_element)
        type_password.send_keys(self.password)
        type_password.submit()
        standby.until(EC.url_changes(self.login_url))