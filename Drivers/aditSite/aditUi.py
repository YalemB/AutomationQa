from aditTeatcontctUs import setUp
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_ui_a_top_page_contact_us():
    driver = setUp()
    navbar = driver.find_element(By.ID, "primary-site-navigation").text.split("\n")
    check_nav = ["HOME","STORE","MEN","WOMEN","ACCESSORIES", "ABOUT", "CONTACT US"]
    assert navbar == check_nav
    headlight = driver.find_element(By.TAG_NAME, "h1").text
    assert headlight == "Contact Us"



    driver.quit()

def test_ui_b_left_side():
    driver = setUp()

    form = driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]").text.split("\n")
    data = ['You tell us. We listen.',
            'hello@atid.store',
            '972-52-1234567',
            'Sunday to Thursday - 9:00 am to 7:00 pm',
            'Friday - 8:00 am to 3:00 pm', 'Need Help? Call Us.',
            '972-52-1234567']
    assert form == data
    driver.quit()
