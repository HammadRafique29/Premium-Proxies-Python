from bin.download_proxies import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
options = webdriver.ChromeOptions()

options.add_argument('--headless')
options.add_argument('--log-level=3')
driver = webdriver.Chrome(options=options)

obj = Proxies(driver).get_proxies()
driver.close()