from time import sleep
import lib.selenium as sele
from threading import Thread
import lib.settings as patreon
import lib.progress as progress
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC


def wait():
    sleep(0.5)


def scrollToBottom():
    html = sele.driver.find_element(By.TAG_NAME, "html")
    html.send_keys(Keys.END)
    wait()


def bypassCookies():
    progress.bypass = True
    WebDriverWait(sele.driver, 10).until(
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
    sele.driver.execute_script(
        "[...document.querySelectorAll('"
        + selector
        + "')].map(el => el.parentNode.removeChild(el))"
    )


def filterByImagesOnly(condition):
    if condition:
        progress.bytype = True
        sele.driver.find_element(By.CSS_SELECTOR, patreon.post).click()
        sele.driver.find_element(By.XPATH, patreon.images).click()
        wait()


def filterByPublicTier(condition):
    if condition:
        progress.bytier = True
        sele.driver.find_element(By.CSS_SELECTOR, patreon.tier).click()
        sele.driver.find_element(By.XPATH, patreon.public).click()
        wait()


def startThread():
    progress.first = True
    t = Thread(target=progress.loading)
    t.start()


def scrollToFilters():
    filters = WebDriverWait(sele.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, patreon.post))
    )
    sele.driver.execute_script("arguments[0].scrollIntoView();", filters)


def loadAllPosts():
    scrollToBottom()
    removeBottom()
    progress.load = True
    continueLoading = True
    waitFor = WebDriverWait(sele.driver, 5)

    try:
        elem = sele.driver.find_element(By.XPATH, patreon.more)
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
            sele.findLikes(x, patreon.count, destination)
        except NoSuchElementException:
            destination.append(0)


def appendHrefs(source, destination):
    for x in source:
        try:
            sele.findHrefs(x, destination)
        except NoSuchElementException:
            destination.append(x.text)


def appendComms(source, destination):
    for x in source:
        try:
            sele.findComments(x, destination)
        except NoSuchElementException:
            destination.append(0)


def filterPosts(x, y):
    scrollToFilters()
    filterByImagesOnly(x)
    filterByPublicTier(y)