import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class ISPSpeedBot:
    def __init__(self, exp_download, exp_upload, email, password, user):
        self.upload = None
        self.download = None
        service = Service()
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=service, options=options)
        self.exp_download = exp_download
        self.exp_upload = exp_upload
        self.email = email
        self.password = password
        self.user = user

    def get_speed(self):
        self.driver.get(url="https://www.speedtest.net")
        go_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'start-text')))
        print(go_button.text)
        go_button.click()
        time.sleep(45)
        download_speed = self.driver.find_element(By.CLASS_NAME, value='download-speed')
        upload_speed = self.driver.find_element(By.CLASS_NAME, value='upload-speed')
        if download_speed.text == "—":
            time.sleep(30)
        else:
            download_speed = download_speed.text

        if upload_speed.text == "—":
            time.sleep(30)
            upload_speed = upload_speed.text
        else:
            upload_speed = upload_speed.text
        self.download = download_speed
        self.upload = upload_speed


    def tweet_at_verizon(self):
        self.driver.get(url='https://twitter.com/i/flow/login')
        user_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, 'text')))
        time.sleep(2)
        user_input.send_keys(self.email)
        user_input.send_keys(Keys.ENTER)
        try:
            user_enter = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input[autocomplete='on'")))
            user_enter.send_keys(self.user)
            time.sleep(2)
            user_enter.send_keys(Keys.ENTER)
        except NoSuchElementException:
            pass
        pass_enter = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[autocomplete='current-password'")))
        pass_enter.send_keys(self.password)
        time.sleep(2)
        pass_enter.send_keys(Keys.ENTER)

        tweet_box = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "public-DraftStyleDefault-block")))
        time.sleep(2)
        tweet_box.click()
        tweet_box.send_keys(f'Hey @Verizon, why is my internet download speed {self.download} Mbps and my upload speed {self.upload} Mbps when I was promised around {self.exp_download}Mbps/{self.exp_upload}Mbps?')
        while True:
            pass


