# common utils
from config import LOG, CONTENT_TYPE_URLENCODED


# require to have a previous token
def build_request_headers(access_token, accept_type=CONTENT_TYPE_URLENCODED, **kwargs):

    LOG.info("build_request_headers")
    headers = {
        "Authorization": f"Basic {access_token}",
        # "accept": accept_type
    }
    if "content_type" in kwargs:
        headers["Content-Type"] = kwargs["content_type"]
    print(f"Request headers: {headers}")
    return headers
