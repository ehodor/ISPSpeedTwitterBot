import os
from dotenv import load_dotenv
load_dotenv()
from ISPSpeedBot import ISPSpeedBot
PROMISED_DOWNLOAD = 940
PROMISED_UPLOAD = 880

TWITTER_EMAIL = os.environ.get("TWITTER_EMAIL")
TWITTER_PASS = os.environ.get("TWITTER_PASS")
TWITTER_USER = os.environ.get("TWITTER_USER")

bot = ISPSpeedBot(exp_download=PROMISED_DOWNLOAD, exp_upload=PROMISED_UPLOAD, email=TWITTER_EMAIL, password=TWITTER_PASS, user=TWITTER_USER)

bot.get_speed()

bot.tweet_at_verizon()
