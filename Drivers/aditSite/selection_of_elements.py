import random
import time

from atidSetUp import *


def select_item(d):
    # random item from the list of items
    selected = {}
    cart = {}
    #number of items in page
    choice = list(range(len(d.find_elements(By.XPATH, "//main[1]/div[1]/ul[1]/li"))))
    #loop for choice of to items
    for i in range(2):

        items = d.find_elements(By.XPATH, "//main[1]/div[1]/ul[1]/li")
        c = random.choice(choice)
        items[c].click()

        choice.remove(c)
        name = d.find_element(By.TAG_NAME, "h1").get_attribute("innerText")
        price = d.find_element(By.XPATH, "//main[1]/div[1]/div[2]/div[2]/p[1]").get_attribute("innerText")

        if len(price) > 8:
            price = price.split(" ")
            price = price[1]

        selected[name] = price


        add_to_cart = "//button[contains(text(),'Add to cart')]"
        WebDriverWait(d, 10).until(
            EC.element_to_be_clickable((By.XPATH, add_to_cart))
        )
        d.find_element(By.XPATH, add_to_cart).click()

        if i == 0:
            d.back()
            d.back()
        else:
            view_crat = "//main[1]/div[1]/div[1]/div[1]/a[1]"
            WebDriverWait(d,10).until(
                EC.element_to_be_clickable((By.XPATH,view_crat))
            )
            d.find_element(By.XPATH,view_crat).click()
            for j in range(2):
                d.implicitly_wait(3)
                cart_item =d.find_element(By.XPATH, f"//tbody/tr[{1 + j}]/td[3]").get_attribute("innerText")
                cart_price = d.find_element(By.XPATH, f"//tbody/tr[{1 + j}]/td[4]").get_attribute("innerText")
                cart[cart_item] = cart_price
    # verify names and prices are me
    assert list(selected.keys())[0] in list(cart.keys())[0]
    assert list(selected.keys())[1] in list(cart.keys())[1]

    # varift sum price is correct
    sum_total = d.find_element(By.XPATH,"//tbody[1]/tr[3]/td[1]/strong[1]/span[1]/bdi[1]").get_attribute("innerText")
    y = list(selected.values())
    x = list(cart.values())
    sum_selcted = 0

    print("")
    print("total price in cars page = ",sum_total)
    print("sum selected items = ",x[0],x[1])





def test_item_1_Acc():
    driver = setUp("store")
    # CLICK TO ACCESSORIES Categories
    Accessories = driver.find_element(By.XPATH,
                                      "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/ul[1]/li[1]/a[1]")
    Accessories.click()
    select_item(driver)

    driver.quit()


def test_item_2_Men():
    driver = setUp("store")
    # CLICK TO Men Categories
    Men = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/ul[1]/li[2]/a[1]")
    Men.click()
    select_item(driver)

    driver.quit()



def test_item_3_Women():
    driver = setUp("store")
    # CLICK TO Women Categories
    Women = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/ul[1]/li[3]/a[1]")
    Women.click()
    select_item(driver)

    driver.quit()
