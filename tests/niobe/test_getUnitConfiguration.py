from lib.Niobe import Niobe
from config import APP_URL, LOG

# from bs4 import BeautifulSoup
# pytest tests\niobe\ --html=reports/restapi_test_report.html --self-contained-html -v -s


def test_get_unit_configuration(login_access_token):
    LOG.info("Get Unit Configuration")
    unit_address = '000-11422-02744'
    # bnc_dm = '10.11.99.117'
    response = Niobe().get_niobe_configuration(APP_URL, login_access_token, unit_address)
    assert response.ok
    assert response.status_code == 200
    print("Response: \n", response.text)

    # soup = BeautifulSoup(response.text, 'xml')
    # classResp = soup.find('getUnitConfig/unitAddress')
    # print(soup.getUnitConfig['unitAddress'])
    # assert soup.getUnitConfig['unitAddress'] == UA_Begin
    #
    # service = soup.find('service')
    # assert service['vcNumber'] == '22'

    # print(service['transcoderName'])
    # print(service['vcNumber'])
    # print(service['vcTable'])
    # print(service['passthruEnable'])
    # print(service['sdEnable'])


