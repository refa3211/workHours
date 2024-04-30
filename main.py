import os

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys



driver_path = r"C:\Users\Refael\AppData\Local\BraveSoftware\Brave-Browser\Application\brave.exe"


load_dotenv() 
username = os.getenv('USER')
password = os.getenv('PASS')
OTPCODE = os.getenv('OTPSECERT')