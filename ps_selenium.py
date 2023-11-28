from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def webDriver():
    options = Options()
    options.add_argument("--lang=en")
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--log-level=3")
    options.add_argument("--blink-settings=imagesEnabled=false")
    return webdriver.Chrome(options=options)


def findElements(selector, driver):
    return driver.find_elements(By.CSS_SELECTOR, selector)


def findComments(i, results):
    elem = i.find_element(By.TAG_NAME, "p")
    results.append(int(elem.text))


def findHrefs(i, results):
    elem = i.find_element(By.TAG_NAME, "a")
    results.append(elem.get_attribute("href"))


def findLikes(i, selector, results):
    elem = i.find_element(By.CSS_SELECTOR, selector)
    results.append(int(elem.text))