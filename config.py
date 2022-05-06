import requests
import logging
import os
from faker import Faker

# get sensitive info from secrets.ini
APP_URL = os.getenv("APP_URL", "")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN", "")
if not APP_URL or not ACCESS_TOKEN:
    raise ValueError("Environment not defined.")

FAKER = Faker('en_US')
SESSION = requests.Session()
LOG = logging.getLogger()
logging.getLogger('faker.factory').setLevel(logging.ERROR)