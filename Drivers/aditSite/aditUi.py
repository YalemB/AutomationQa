# from  atidSetUp import *
#
# def test_ui_a_top_page_contact_us():
#     driver = setUp("contact-us")
#     navbar = driver.find_element(By.ID, "primary-site-navigation").text.split("\n")
#     check_nav = ["HOME","STORE","MEN","WOMEN","ACCESSORIES", "ABOUT", "CONTACT US"]
#     assert navbar == check_nav
#     headlight = driver.find_element(By.TAG_NAME, "h1").text
#     assert headlight == "Contact Us"
#
#
#
#     driver.quit()
#
# def test_ui_b_left_side():
#     driver = setUp("contact-us")
#
#     form = driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]").text.split("\n")
#     data = ['You tell us. We listen.',
#             'hello@atid.store',
#             '972-52-1234567',
#             'Sunday to Thursday - 9:00 am to 7:00 pm',
#             'Friday - 8:00 am to 3:00 pm', 'Need Help? Call Us.',
#             '972-52-1234567']
#     assert form == data
#     driver.quit()
