from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
import time
import chromedriver_binary
def OrderIceCap():
    wd = wd.Chrome()
    wd.implicitly_wait(10)
    wd.get('https://www.timhortons.ca/')

    apply_button = wd.find_element('xpath','/html/body/reach-portal/div[3]/div/div/div/div/div/div/div[2]/button')
    apply_button.click()

    menu_button = wd.find_element('xpath','//*[@id="root"]/div/div/div/div/div[1]/div/nav/div/div[1]/a[2]')
    menu_button.click()
    address_button = wd.find_element('xpath', '//*[@id="downshift-0-input"]')
    address_button.click()
    address_button.send_keys('University of Ottawa, Laurier Avenue East, Ottawa, ON, Canada')
    address_button.send_keys(Keys.ESCAPE)
    store_location_button= wd.find_element('xpath', '//*[@id="tabpanel-0"]/div/div[1]/div/div')
    store_location_button.click()
    order_coffee_cup_button = wd.find_element('xpath','//*[@id="tabpanel-0"]/div/div[1]/div[2]/div/div/div[2]')
    order_coffee_cup_button.click()
    cold_beverages_button= wd.find_element('xpath', '//*[@id="main"]/div/div/div/div/a[4]')
    cold_beverages_button.click()
    redeye_icecapp_button = wd.find_element('xpath','//*[@id="main"]/div/div/span/div/div[2]/div/a[3]')
    redeye_icecapp_button.click()
    size_button=wd.find_element('xpath','//*[@id="main"]/div/div/span/div[2]/div[2]/div/div[3]/div/fieldset[1]')
    size_button.click()
    large_size_button=wd.find_element('xpath','//*[@id="Size-selection-content"]/form/label[3]/div[2]/div/div')
    large_size_button.click()
    add_to_cart_button=wd.find_element('xpath','//*[@id="main"]/div/div/span/div[2]/div[2]/div/div[3]/button')
    add_to_cart_button.click()
    #incomplete
    
    
time.sleep(100)