from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

chrome_drive_path = "C:\\Users\\Pichau\\Desktop\\JAVASCRIPT\\chromedriver"
PROMISE_DOWN = 200
PROMISE_UP = 60

TT_EMAIL = "xx"
TT_PASSW = "xxxx"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_drive_path)
        self.PROMISE_download = PROMISE_DOWN
        self.PROMISE_upload = PROMISE_UP
        self.download_get = 0
        self.upload_get = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(10)
        self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a').click()
        time.sleep(90)
        self.download_get = float(self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
        self.upload_get = float(self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text)

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(5)
        self.login = self.driver.find_element(By.NAME, "text")
        self.login.send_keys(f"{TT_EMAIL}")
        self.login.send_keys(Keys.ENTER)
        time.sleep(3)
        self.password = self.driver.find_element(By.NAME, "password")
        self.password.send_keys(f"{TT_PASSW}")
        self.password.send_keys(Keys.ENTER)
        # writing the message
        time.sleep(5)
        self.tweet_box = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        self.tweet_message = f"Olá HE-NET , por que minha internet está " \
                             f"{self.download_get}mb down/{self.upload_get}mb up se o contratado é 200mb down/ 60mb up?"
        self.tweet_box.click()
        time.sleep(1)
        self.tweet_box.send_keys(f"{self.tweet_message}")
        self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]').click()
