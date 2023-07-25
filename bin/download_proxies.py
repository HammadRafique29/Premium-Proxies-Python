from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Proxies():
    def __init__(self, driver):
        self.url = ["https://free-proxy-list.net/", "https://spys.one/en/https-ssl-proxy/", "https://advanced.name/freeproxy?"]
        self.webdriver = driver
        self.PROXIES = []

    def website_1(self):
        try:
            self.webdriver.get(self.url[0])
            rows = self.webdriver.find_elements(By.XPATH, "//table[contains(@class, 'table')]")[0].find_elements(By.TAG_NAME, "tr")[1:]
            proxies = []
            for row in rows:
                proxy = row.find_elements(By.TAG_NAME, "td")[0:2]
                proxy = proxy[0].text + ":" + proxy[1].text
                proxies.append(proxy)

            self.PROXIES = self.PROXIES + proxies
            self.save_proxies(proxies)
            print(f"\tWEB 1: TOTAL PROXIES FETCHED - {len(proxies)}") 

        except Exception as e:
            print(f"\tWEB 1: TOTAL PROXIES FETCHED - {len(proxies)}") 
            return 0

        
    
    def website_2(self):
        try:
            self.webdriver.get(self.url[1])
            proxies = [] 
            for anonymity in [1,3,4]:
                set_spy = self.webdriver.find_elements(By.XPATH, "//font[@class='spy1']")[0].find_elements(By.TAG_NAME, 'select')[1].find_elements(By.TAG_NAME, "option")[anonymity].click()
                time.sleep(3)
                rows = self.webdriver.find_elements(By.XPATH, "//table")[2].find_elements(By.TAG_NAME, "tr")[2:] 
                
                for row in rows[0:len(rows)-2]:                                                             
                    proxy = str(row.find_elements(By.TAG_NAME, "td")[0].text)                                         
                    if proxy == '':
                        continue
                    if "*NOA" in proxy:
                        continue
                    else:
                        proxies.append(proxy)                                                              
                print(f"\tWEB 2: {len(proxies)}")

            self.PROXIES = self.PROXIES + proxies
            self.save_proxies(proxies)
            print(f"\tWEB 2: TOTAL PROXIES FETCHED - {len(proxies)}")
        except Exception as e:
            print(f"\tWEB 2: TOTAL PROXIES FETCHED - {len(proxies)}")
            return 0

    
    def website_3(self):
        proxies = []
        try:
            for page in range(1, 10):
                self.webdriver.get(self.url[2] + f"page={page}")
                self.webdriver.implicitly_wait(10)
                rows = self.webdriver.find_elements(By.XPATH, "//table[@id='table_proxies']//tbody/tr")
                if len(rows) <= 0:
                    self.save_proxies(proxies)
                    self.PROXIES = self.PROXIES + proxies
                    print(f"\tWEB 3: TOTAL PROXIES FETCHED - {len(proxies)}")
                    return 1

                else:
                    for row in rows:
                        proxy = row.find_elements(By.TAG_NAME, "td")[1:3]
                        proxy = proxy[0].text + ":" + proxy[1].text
                        proxies.append(proxy)
                    print(f"\tWEB 3: {len(proxies)}")

        except Exception as e:
            print(e)
            return 0
        

    def save_proxies(self, proxies):
        with open("bin/proxies.txt", 'a') as file:
            for proxy in proxies:
                file.write(proxy + "\n")

        

    def get_proxies(self):
        print(f"#"*100) 
        print("\t############### DOWNLOADING PROXIES! PLEASE WAIT (MAX 5 MIN) ... ###############")
        self.website_1()
        self.website_2()
        self.website_3()
        print(f"\t############### PROXIES DOWNLOADED SUCCESSFULLY (PROXIES.TXT-- {len(self.PROXIES)} ###############") 
        print(f"#"*100) 
        


# CREATE BY CODING MAGICIAN (HAMMAD RAFIQUE -- https://github.com/HammadRafique29)
# NEED YOUR SUPPORT! FOLLOW MY PROFILE