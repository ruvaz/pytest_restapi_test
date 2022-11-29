import pytest
from config import ACCESS_TOKEN, LOG

# Get access token from ENV variables
@pytest.fixture()
def login_access_token():
    # step 1: authenticate
    # step 2: get token from login
    LOG.info("login_access_token")
    access_token = ACCESS_TOKEN
    LOG.debug(access_token)
    yield access_token


#add a parameter by command line
def pytest_addoption(parser):
    parser.addoption("--users", action="store", default="1")

#part of the parameter by command line
def pytest_generate_tests(metafunc):
    option_value = metafunc.config.option.users
    if 'n_users' in metafunc.fixturenames and option_value is not None:
        metafunc.parametrize("n_users", [option_value])
