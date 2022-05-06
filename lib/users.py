import requests
from lib.utils import build_request_headers
from config import SESSION, LOG, FAKER


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

    def create_random_user_post_comment(login_access_token):
        LOG.info("create_user_post_comment")
        # Create new user
        profile = FAKER.simple_profile()
        new_user = {
            "name": profile['name'],
            "gender": profile['sex'],
            "email": profile['mail'],
            "status": 'active'
        }
        response = Users().create_user(APP_URL, login_access_token, new_user)
        assert response.ok
        assert response.status_code == 201
        LOG.debug(response.json())
        response_data = response.json()
        user_id = response_data["id"]

        # Create new post
        new_post = {
            "user_id": user_id,
            "title": FAKER.sentence(),
            "body": FAKER.text(max_nb_chars=160)
        }
        response = Posts().create_post(APP_URL, login_access_token, new_post)
        assert response.ok
        assert response.status_code == 201
        response_data = response.json()
        post_id = response_data["id"]
        LOG.debug(response_data)

        # Create new comment
        visit = FAKER.simple_profile()
        new_comment = {
            "post_id": post_id,
            "name": visit['name'],
            "email": visit['mail'],
            "body": FAKER.sentence()
        }
        response = Posts().create_post_comment(APP_URL, login_access_token, post_id, new_comment)
        assert response.ok
        assert response.status_code == 201
        response_data = response.json()
        LOG.debug(response_data)
