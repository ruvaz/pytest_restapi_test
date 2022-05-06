import requests
from lib.utils import build_request_headers
from config import SESSION, LOG


class Users:

    def __init__(self):
        self.user_url = "/users"

    def get_all_users(self, app_url, access_token):
        LOG.info("get_all_users")
        request_headers = build_request_headers(access_token)
        response = SESSION.get(f"{app_url}{self.user_url}", headers=request_headers)
        return response

    def create_user(self, app_url, access_token, user):
        LOG.info("create_user")
        request_headers = build_request_headers(access_token, content_type="application/json")
        payload = user
        LOG.debug(f"Request payload: {payload}")
        response = SESSION.post(f"{app_url}{self.user_url}/",
                                headers=request_headers, params=payload)
        return response

    def read_user(self, app_url, access_token, user_id):
        LOG.info("read_user")
        request_headers = build_request_headers(access_token,
                                                content_type="application/json")
        response = SESSION.get(f"{app_url}{self.user_url}/{user_id}",
                               headers=request_headers)
        return response

    def update_user(self, app_url, access_token, user_id, **kwargs):
        LOG.info("update_user")
        request_headers = build_request_headers(access_token,
                                                content_type="application/json")
        payload = {}

        if "name" in kwargs:
            payload["name"] = kwargs["name"]
        if "email" in kwargs:
            payload["email"] = kwargs["email"]

        LOG.debug(f"Request payload: {payload}")
        response = SESSION.put(f"{app_url}{self.user_url}/{user_id}",
                               headers=request_headers, json=payload)
        return response

    def delete_user(self, app_url, access_token, user_id):
        LOG.info("delete_user")
        request_headers = build_request_headers(access_token)
        response = SESSION.delete(f"{app_url}{self.user_url}/{user_id}",
                                  headers=request_headers)
        return response
