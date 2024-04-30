import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

driver_path = r"C:\Users\Refael\AppData\Local\BraveSoftware\Brave-Browser\Application\brave.exe"

load_dotenv() 
user_id = os.getenv('ID')
password = os.getenv('PASSWORD')
company_id = os.getenv('COMPANY_ID')

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)  # Assuming you have Chrome WebDriver installed
driver.get("https://portal.malam-payroll.com/Salprd2Root/faces/login.jspx")

def login():
    """login and enter nochchut page
    """
    
    time.sleep(1)
    
    
    company_input = driver.find_element(By.ID, "indexNumInput::content")
    company_input.send_keys(company_id)
    time.sleep(1)
    
    #username
    user_id_input = driver.find_element(By.ID, "useridInput::content")
    user_id_input .send_keys(user_id)
    time.sleep(1)
    
    #password
    password_input = driver.find_element(By.ID, "it2::content")
    password_input.send_keys(password) # type: ignore
    time.sleep(1)
    #enter
    password_input.send_keys(Keys.RETURN)
    time.sleep(1.5)
    
    #after login
    report = driver.find_element(By.ID, "pt1:j_id7")  # Replace "dropdown_id" with the actual ID of the dropdown
    ActionChains(driver).click(report).perform()
    time.sleep(1)
    
    xpath_nochchut = "/html/body/div[1]/form/div[3]/div[2]/div/div/div/table/tbody/tr/td/table/tbody/tr[2]/td/div/table/tbody/tr[1]/td[2]"
    nochchut = driver.find_element(By.XPATH, xpath_nochchut)
    ActionChains(driver).click(nochchut).perform()
    time.sleep(10)



def sethour():
    timeset = driver.find_element(By.ID, "pt1:dataTable:30:clockOutTime::content")
    timeset.send_keys("1700")
    print("time set to 1700")
    
def savedata():
    savebtn = driver.find_element(By.ID, "pt1:saveButton")
    ActionChains(driver).click(savebtn).perform()
    print("save the data")
if __name__ == "__main__":
    login()
    sethour()
    savedata()
