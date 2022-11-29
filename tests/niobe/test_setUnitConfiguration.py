from lib.Niobe import Niobe
from config import APP_URL, LOG


# pytest tests\niobe\ --html=reports/restapi_test_report.html --self-contained-html -v -s


def test_set_unit_configuration(login_access_token):
    LOG.info("Set Unit Configuration")
    this_pc_ip = '10.45.77.193'
    unit_address = '000-11422-02744'
    response = Niobe().set_configuration_service(APP_URL, login_access_token, unit_address, this_pc_ip)

    assert response.status_code == 200
    print("\nResponse: \n", response.text)
