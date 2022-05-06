import pytest
from config import ACCESS_TOKEN, LOG


@pytest.fixture()
def login_access_token():
    # step 1: authenticate
    # step 2: get token from login
    LOG.info("login_access_token")
    access_token = ACCESS_TOKEN
    LOG.debug(access_token)
    yield access_token
