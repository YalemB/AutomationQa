from selenium import webdriver

PATH = "..\Drivers\drivers\msedgedriver.exe"

driver = webdriver.Edge(PATH)
driver.get("https://www.google.co.il")