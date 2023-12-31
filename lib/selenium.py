from selenium import webdriver
from subprocess import CREATE_NO_WINDOW
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


def setupDriver():
    global driver
    options = Options()
    service = Service()
    options.add_argument("--lang=en")
    options.add_argument("--headless")
    options.page_load_strategy = "none"
    options.add_argument("--disable-gpu")
    options.add_argument("--log-level=3")
    service.creation_flags = CREATE_NO_WINDOW
    options.add_argument("--blink-settings=imagesEnabled=false")
    driver = webdriver.Chrome(options=options, service=service)


def openProfile(username):
    driver.get("https://www.patreon.com/" + username + "/posts")


def findElements(selector):
    return driver.find_elements(By.CSS_SELECTOR, selector)


def findComments(x, results):
    elem = x.find_element(By.TAG_NAME, "p")
    results.append(int(elem.text))


def findHrefs(x, results):
    elem = x.find_element(By.TAG_NAME, "a")
    results.append(elem.get_attribute("href"))


def findLikes(x, selector, results):
    elem = x.find_element(By.CSS_SELECTOR, selector)
    results.append(int(elem.text))