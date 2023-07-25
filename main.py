from bin.download_proxies import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
obj = Proxies(driver).get_proxies()
driver.close()