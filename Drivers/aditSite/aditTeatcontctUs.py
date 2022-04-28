# from  atidSetUp import *
#
# def test_a_fill_contact_us_form():
#     driver = setUp("contact-us")
#     name = driver.find_element(By.CSS_SELECTOR, "#wpforms-15-field_0").send_keys("yalem")
#     subject = driver.find_element(By.CSS_SELECTOR, "#wpforms-15-field_5").send_keys("dalivery")
#     email = driver.find_element(By.CSS_SELECTOR, "#wpforms-15-field_4").send_keys("y@mail.com")
#     massage = driver.find_element(By.CSS_SELECTOR, "#wpforms-15-field_2").send_keys("hello how are you guys")
#
#     driver.find_element(By.CSS_SELECTOR, "#wpforms-submit-15").click()
#
#     value = driver.find_element(By.XPATH,
#                                 "//p[contains(text(),'Thanks for contacting us! We will be in touch with')]").text
#
#     assert value == "Thanks for contacting us! We will be in touch with you shortly."
#
#     driver.quit()
#
#
#
#
# def test_b_fill_contact_us_form_unvalid_email():
#     driver = setUp("contact-us")
#     name = driver.find_element(By.CSS_SELECTOR, "#wpforms-15-field_0").send_keys("yalem")
#     subject = driver.find_element(By.CSS_SELECTOR, "#wpforms-15-field_5").send_keys("dalivery")
#     email = driver.find_element(By.CSS_SELECTOR, "#wpforms-15-field_4").send_keys("ygmail.com")
#     massage = driver.find_element(By.CSS_SELECTOR, "#wpforms-15-field_2").send_keys("hello how are you guys")
#
#     driver.find_element(By.CSS_SELECTOR, "#wpforms-submit-15").click()
#
#     value = driver.find_element(By.CSS_SELECTOR, "#wpforms-15-field_4-error").text
#
#     assert value == "Please enter a valid email address."
#
#     driver.quit()

