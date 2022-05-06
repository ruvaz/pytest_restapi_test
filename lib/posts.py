import requests
from lib.utils import build_request_headers
from config import SESSION, LOG


class Posts:
    def __init__(self):
        self.post_url = "/posts"

    def get_all_posts(self, app_url, access_token):
        LOG.info("get_all_posts")
        request_headers = build_request_headers(access_token)
        response = SESSION.get(f"{app_url}{self.post_url}", headers=request_headers)
        return response

    def create_post(self, app_url, access_token, post):
        LOG.info("create_post")
        request_headers = build_request_headers(access_token, content_type="application/json")
        payload = post
        LOG.debug(f"Request payload: {payload}")
        response = SESSION.post(f"{app_url}{self.post_url}/",
                                headers=request_headers, params=payload)
        return response

    def create_post_comment(self, app_url, access_token, post_id, comment):
        LOG.info("get_post_comments")
        request_headers = build_request_headers(access_token, content_type="application/json")
        payload = comment
        response = SESSION.post(f"{app_url}{self.post_url}/{post_id}/comments/",
                                headers=request_headers, params=payload)
        return response

    def get_post_comments(self, app_url, access_token, post_id):
        LOG.info("get_post_comments")
        request_headers = build_request_headers(access_token, content_type="application/json")
        response = SESSION.get(f"{app_url}{self.post_url}/{post_id}/comments/",
                               headers=request_headers)
        return response
