from time import sleep
from threading import Thread
import ps_settings as patreon
import ps_loading as progress
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


def wait():
    sleep(0.5)


def scrollToBottom(driver):
    html = driver.find_element(By.TAG_NAME, "html")
    html.send_keys(Keys.END)
    html.send_keys(Keys.END)
    wait()


def bypassCookies(driver):
    progress.bypass = True
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="transcend-consent-manager"]')
        )
    )
    driver.execute_script(
        """var element=document.querySelector("#transcend-consent-manager");element&&element.parentNode.removeChild(element);"""
    )
    wait()


def removeBanner(driver):
    driver.execute_script(
        """var element=document.querySelector(".sc-lvssun-0");element&&element.parentNode.removeChild(element);"""
    )
    wait()


def filterByImagesOnly(condition, driver):
    if condition:
        progress.bytype = True
        driver.find_element(By.CSS_SELECTOR, patreon.post).click()
        driver.find_element(By.XPATH, patreon.images).click()
        wait()


def filterByPublicTier(condition, driver):
    if condition:
        progress.bytier = True
        driver.find_element(By.CSS_SELECTOR, patreon.tier).click()
        driver.find_element(By.XPATH, patreon.public).click()
        wait()


def startThread(target):
    t = Thread(target=target)
    t.start()


def scrollToFilters(driver):
    actions = ActionChains(driver)
    filters = driver.find_element(By.CSS_SELECTOR, patreon.post)
    actions.move_to_element(filters).perform()


def loadAllPosts(driver):
    progress.load = True
    waitFor = WebDriverWait(driver, 5)
    try:
        elem = driver.find_element(By.XPATH, patreon.more)
        elem.click()
    except NoSuchElementException:
        pass

    while True:
        try:
            wait()
            scrollToBottom(driver)
            elem = waitFor.until(EC.element_to_be_clickable((By.XPATH, patreon.more)))
            elem.click()
        except TimeoutException:
            break