import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.close()


def test_login(browser):
    browser.get("https://www.hackerrank.com/login")

    username = browser.find_element(by=By.XPATH, value='//*[@id="input-1"]')
    username.send_keys('pulicalsreekanth@gmail.com')

    password = browser.find_element(by=By.XPATH, value='//*[@id="input-2"]')
    password.send_keys('Qwerty!23456')

    # driver.find_element_by_xpath("//button[.//span[text()='Log In']]").click()
    browser.find_element(by=By.XPATH, value="//button[.//span[text()='Log In']]").click()
