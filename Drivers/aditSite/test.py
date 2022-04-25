from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://atid.store/contact-us")

try:

    form = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH,"//body/div[@id='page']/div[@id='content']/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]"))
    )
    fileds = form.find_elements(By.TAG_NAME, "div")
    data = ["yalem", "dlivery","yalem8@gmail.com", "hello how are you guys"]



    for fild in fileds:
        fild.send_keys(data[i])

    # send_massage = driver.find_element(By.CSS_SELECTOR, "#wpforms-submit-15").click()
    #
    # value = driver.find_element(By.XPATH,"//p[contains(text(),'Thanks for contacting us! We will be in touch with')]" ).text
    # print(value)

except:
    driver.quit()

