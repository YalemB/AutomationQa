from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# driver = webdriver.Firefox(executable_path=r"..\Drivers\drivers\geckodriver.exe")
# driver.get("https://www.python.org")

driver = webdriver.Firefox(executable_path=r"..\Drivers\drivers\geckodriver.exe")
driver.get("https://www.python.org")
driver.implicitly_wait(5)
ser = driver.find_element(By.NAME, "q")
ser.clear()
ser.send_keys("selenium")
ser.send_keys(Keys.RETURN)

def test_result():
    result = driver.find_elements(By.XPATH, "/html/body/div/div[3]/div/section/form/ul/li")

    assert len(result) > 0
    print("")
    print(f"There are {len(result)} results")
    # driver.quit()

