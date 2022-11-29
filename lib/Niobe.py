import datetime

from config import LOG, CONTENT_TYPE_URLENCODED, SESSION
from lib.utils import build_request_headers


class Niobe:
    def __init__(self):
        self.dm_url = "/DecMgrCmd"

    def set_configuration_service(self, app_url, access_token, unit_address, this_pc_ip):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%dT%TZ")

        request_headers = build_request_headers(
            access_token, content_type=CONTENT_TYPE_URLENCODED)

        payload = f'data=<?xml version="1.0" encoding="UTF-8"?>' \
                  f'<Message UtcTime="{timestamp}" Version="1.0">' \
                  f'<Request TransId="{this_pc_ip}-123457">' \
                  f'<setUnitConfig unitAddress="{unit_address}">' \
                  f'<serviceList>' \
                  f'<service transcoderID="1" ' \
                  f'vcTable="1" ' \
                  f'vcNumber="1" ' \
                  f'hdEnable="true" ' \
                  f'sdEnable="true" ' \
                  f'passthruEnable="true" />' \
                  f'</serviceList></setUnitConfig></Request></Message>'

        print("Payload:\n", payload)

        return SESSION.post(f"{app_url}{self.dm_url}",
                            headers=request_headers, params=payload)

    def get_niobe_configuration(self, app_url, access_token, unit_address):
        """Get the Niobe configuration"""

        timestamp = datetime.datetime.now().strftime("%Y-%m-%dT%TZ")

        request_headers = build_request_headers(
            access_token, content_type=CONTENT_TYPE_URLENCODED)

        payload = f'data=<?xml version="1.0" encoding="UTF-8"?>' \
                  f'<Message UtcTime="{timestamp}" Version="1.0">' \
                  f'<Request TransId="168.84.56.24-123457">' \
                  f'<getUnitConfig unitAddress="{unit_address}"/>' \
                  f'</Request>' \
                  f'</Message>'

        print("Payload:\n", payload)

        return SESSION.post(f"{app_url}{self.dm_url}",
                            headers=request_headers, params=payload)
