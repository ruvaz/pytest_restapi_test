import requests
import logging
import os

from dotenv import load_dotenv

load_dotenv(dotenv_path='secrets.env')

CONTENT_TYPE_JSON = "application/json"
CONTENT_TYPE_URLENCODED = "application/x-www-form-urlencoded"
CONTENT_TYPE_XML = "text/xml;charset=utf-8"

# get sensitive info from secrets.env
APP_URL = os.environ.get("APP_URL", "")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "")

if not APP_URL or not ACCESS_TOKEN:
    raise ValueError("Environment not defined.")

SESSION = requests.Session()
LOG = logging.getLogger()

logging.getLogger('faker.factory').setLevel(logging.ERROR)
LOG.info("APP_URL: " + APP_URL)
LOG.info("ACCESS_TOKEN: " + ACCESS_TOKEN)

print("APP_URL: " + APP_URL)
print("ACCESS_TOKEN: " + ACCESS_TOKEN)
