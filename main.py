import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException

from random import randint
from time import sleep

delay = 3

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option(name="useAutomationExtension", value=False)

driver = webdriver.Chrome(
    executable_path="C:\\bin\\chromedriver.exe",
    chrome_options=chrome_options)


#No appointments available
def check_appointments_availability():
    driver.get("https://waitwhile.com/welcome/gtaapassoffice")
    count = 0
    max_count = 3

    while True:
        try:
            #EC.presence_of_element_located((By.ID, "schedule-booking-1"))
            WebDriverWait(driver, delay).until(
                EC.presence_of_element_located((By.CLASS_NAME, "mt-3"))
            )
            print("Page is ready!")
            element_container = driver.find_element(By.CLASS_NAME, "mt-3")

            if element_container.text != 'No appointments available':
                from playsound import playsound
                while True:
                    playsound("C:\\Windows\\Media\\Alarm01.wav")
                    sleep(1)
                break # it will break from the loop once the specific element will be present.
            else:
                s = get_sleep_time()
                print(element_container.text, " sleep ", s, " sec!")
                sleep(s)

                count = 0
                driver.get("https://waitwhile.com/welcome/gtaapassoffice")
        except TimeoutException:
            count = count + 1
            import datetime
            print("Loading took too much time!-Try again", " ", datetime.datetime.now())

            if count > max_count:
                from playsound import playsound
                while True:
                    playsound("C:\\Windows\\Media\\Alarm01.wav")
                    sleep(1)


def get_sleep_time():
    t = time.localtime(time.time())
    base = 5

    if t.tm_hour in [3, 4, 5, 6, 7]:
        return randint(10*base, 20*base)
    else:
        t = (23-t.tm_hour) * base + (60-t.tm_min) + (60-t.tm_sec)
        t = t if t > base else base

        return randint(base, t)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    check_appointments_availability()



