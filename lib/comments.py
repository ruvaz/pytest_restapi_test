import requests
from lib.utils import build_request_headers
from config import SESSION, LOG


class Comments:

    def __init__(self):
        self.comment_url = "/comments"

    def get_all_comments(self, app_url, access_token):
        LOG.info("get_all_comments")
        request_headers = build_request_headers(access_token)
        response = SESSION.get(f"{app_url}{self.comment_url}", headers=request_headers)
        return response
