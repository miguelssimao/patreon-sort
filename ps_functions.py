from time import sleep
import ps_selenium as sel
from threading import Thread
import ps_settings as patreon
import ps_loading as progress
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC


def wait():
    sleep(0.5)


def scrollToBottom():
    html = sel.driver.find_element(By.TAG_NAME, "html")
    html.send_keys(Keys.END)
    wait()


def bypassCookies():
    progress.bypass = True
    WebDriverWait(sel.driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="transcend-consent-manager"]')
        )
    )
    removeElement("#transcend-consent-manager")
    wait()


def removeBottom():
    removeElement(".sc-lvssun-0")
    removeElement("footer")
    wait()


def removeElement(selector):
    sel.driver.execute_script(
        "[...document.querySelectorAll('"
        + selector
        + "')].map(el => el.parentNode.removeChild(el))"
    )


def filterByImagesOnly(condition):
    if condition:
        progress.bytype = True
        sel.driver.find_element(By.CSS_SELECTOR, patreon.post).click()
        sel.driver.find_element(By.XPATH, patreon.images).click()
        wait()


def filterByPublicTier(condition):
    if condition:
        progress.bytier = True
        sel.driver.find_element(By.CSS_SELECTOR, patreon.tier).click()
        sel.driver.find_element(By.XPATH, patreon.public).click()
        wait()


def startThread(target):
    progress.first = True
    t = Thread(target=target)
    t.start()


def scrollToFilters():
    filters = WebDriverWait(sel.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, patreon.post))
    )
    sel.driver.execute_script("arguments[0].scrollIntoView();", filters)


def loadAllPosts():
    progress.load = True
    continueLoading = True
    waitFor = WebDriverWait(sel.driver, 5)

    try:
        elem = sel.driver.find_element(By.XPATH, patreon.more)
        elem.click()
    except NoSuchElementException:
        continueLoading = False
        pass

    while continueLoading:
        try:
            wait()
            scrollToBottom()
            elem = waitFor.until(EC.element_to_be_clickable((By.XPATH, patreon.more)))
            elem.click()
        except TimeoutException:
            break

    progress.final = True


def appendLikes(source, destination):
    for x in source:
        try:
            sel.findLikes(x, patreon.count, destination)
        except NoSuchElementException:
            destination.append(0)


def appendHrefs(source, destination):
    for x in source:
        try:
            sel.findHrefs(x, destination)
        except NoSuchElementException:
            destination.append(x.text)


def appendComments(source, destination):
    for x in source:
        try:
            sel.findComments(x, destination)
        except NoSuchElementException:
            destination.append(0)
