from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

#driver set-up to atid-store
# pages = [home, store, man, women, accessories, about, contact]
def setUp(page=""):
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    if page in ("accessories", "about", "contact-us","store"):
        driver.get(f"https://atid.store/{page}")
        return driver
    elif page in ("men", "women"):
        driver.get(f"https://atid.store/product-category/{page}")
        return driver
    else:
        print("page not exist")








