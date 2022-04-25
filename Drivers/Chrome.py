from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# def setUp():
#     PATH = "..\Drivers\drivers\chromedriver.exe"
#     driver = webdriver.Chrome(PATH)
#     driver.get("https://atid.store")
#     return driver
#
#
#
# def store():
#     return setUp().find_element(By.LINK_TEXT, "STORE").click()
#
# def search_result():
#     store()
#     search = setUp().find_element(By.ID, "wc-block-search__input-1")
#     search.send_keys("test")
#     search.send_keys(Keys.RETURN)
#
# search_result()
#
# def test_is_there_result():
#     value = setUp().find_element(By.CLASS_NAME, "woocommerce-info").get_attribute("innerText")
#     assert value == "No products were found matching your selection."


def setUp():
    PATH = "..\Drivers\drivers\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://atid.store")
    return driver


#
# def test_search_result():
#     driver = setUp()
#     driver.find_element(By.LINK_TEXT, "STORE").click()
#     search = driver.find_element(By.ID, "wc-block-search__input-1")
#     search.send_keys("anchor bracelet")
#     search.send_keys(Keys.RETURN)
#
#     name = driver.find_element(By.XPATH, "// h1[contains(text(), 'Anchor Bracelet')]").get_attribute("innerText")
#     price = driver.find_element(By.XPATH,
#                                 "//body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[2]/div[2]/p[1]/span[1]/bdi[1]").get_attribute(
#         "innerText").split(".")
#     det = driver.find_element(By.XPATH,
#                               "//body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[2]/div[2]/div[2]/p[1]").get_attribute(
#         "innerText")
#     assert name == "Anchor Bracelet"
#     assert price[0] == "250"
#     assert det == "Nam nec tellus a odio tincidunt auctor a ornare odio. Sed non mauris vitae erat consequat auctor eu in elit. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Mauris in erat justo. Nullam ac urna eu felis dapibus condimentum sit amet a augue. Sed non neque elit sed."
#



# try:
#
#     fp = WebDriverWait(driver, 5).until(
#         EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'שכחת את הסיסמה?')]"))
#     )
#     fp.click()
#     fp.back()
#
# except:
#     driver.quit()


# try:
#
#     nc = WebDriverWait(driver, 15).until(
#         EC.presence_of_element_located((By.XPATH, "//body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[5]/a[1]"))
#     )
#     nc.click()
#
#
#
# except:
#     driver.quit()
