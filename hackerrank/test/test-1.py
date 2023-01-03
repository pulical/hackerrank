from selenium.webdriver.common.by import By
import logging

logging.basicConfig(level=logging.DEBUG, filename="C:/Users/RCC/PycharmProjects/hackerrank/test.log")


def test_check(client):
    # Test login
    username = 'pulicalsreekanth@gmail.com'
    password = 'Qwerty!23456'
    logging.debug('Attempting login with username "%s" and password "%s"', username, password)


def test_login(browser):
    browser.get("https://www.hackerrank.com/login")

    username = browser.find_element(by=By.XPATH, value='//*[@id="input-1"]')
    username.send_keys('pulicalsreekanth@gmail.com')

    password = browser.find_element(by=By.XPATH, value='//*[@id="input-2"]')
    password.send_keys('Qwerty!23456')

    # driver.find_element_by_xpath("//button[.//span[text()='Log In']]").click()
    browser.find_element(by=By.XPATH, value="//button[.//span[text()='Log In']]").click()

    browser.get("https://www.hackerrank.com/my_account")
