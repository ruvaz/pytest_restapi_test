import requests
from lib.utils import build_request_headers
from config import SESSION, LOG, FAKER


def generate_fake_user():
    profile = FAKER.simple_profile()
    return {
        "name": profile['name'],
        "gender": profile['sex'],
        "email": profile['mail'],
        "status": 'active'
    }


def generate_fake_todo(user_id):
    return {
        "user_id": user_id,
        "title": FAKER.sentence(),
        # "due_on": FAKER.date_time_this_month(after_now=True),
        "due_on": FAKER.date_time_between(start_date="now", end_date="+1y"),
        "status": "pending"
    }


class Users:

    def __init__(self):
        self.user_url = "/users"

    def get_all_users(self, app_url, access_token):
        LOG.info("get_all_users")
        request_headers = build_request_headers(access_token)
        response = SESSION.get(
            f"{app_url}{self.user_url}", headers=request_headers)
        return response

    def create_user(self, app_url, access_token, user):
        LOG.info("create_user")
        request_headers = build_request_headers(
            access_token, content_type="application/json")
        if user['gender'] == 'f':
            user['gender'] = 'female'
        else:
            user['gender'] = 'male'
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
        if "gender" in kwargs:
            payload["gender"] = kwargs["gender"]
        if "status" in kwargs:
            payload["status"] = kwargs["status"]

        response = SESSION.put(f"{app_url}{self.user_url}/{user_id}",
                               headers=request_headers, json=payload)
        return response

    def delete_user(self, app_url, access_token, user_id):
        LOG.info("delete_user")
        request_headers = build_request_headers(access_token)
        response = SESSION.delete(f"{app_url}{self.user_url}/{user_id}",
                                  headers=request_headers)
        return response

    def create_todo(self, app_url, access_token, user_id, todo):
        LOG.info("create_todo")
        request_headers = build_request_headers(
            access_token, content_type="application/json")
        payload = todo
        LOG.debug(f"Request payload: {payload}")
        response = SESSION.post(f"{app_url}{self.user_url}/{user_id}/todos",
                                headers=request_headers, params=payload)
        return response
