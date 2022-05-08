from lib.utils import build_request_headers
from config import SESSION, LOG, FAKER, CONTENT_TYPE_JSON


def generate_fake_user():
    """Generate infor for a user"""
    profile = FAKER.simple_profile()
    return {
        "name": profile['name'],
        "gender": profile['sex'],
        "email": profile['mail'],
        "status": 'active'
    }


def generate_fake_todo(user_id):
    """Generate info for a new To Do"""
    return {
        "user_id": user_id,
        "title": FAKER.sentence(),
        "due_on": FAKER.date_time_between(start_date="now", end_date="+1y"),
        "status": "pending"
    }


class Users:

    def __init__(self):
        self.user_url = "/users"

    def get_all_users(self, app_url, access_token):
        """Get all the users from server"""
        LOG.info("get_all_users")
        request_headers = build_request_headers(access_token)
        response = SESSION.get(
            f"{app_url}{self.user_url}", headers=request_headers)
        LOG.debug("All users: " + str(response.json()))
        return response

    def create_user(self, app_url, access_token, user):
        """Create a new user on server"""
        LOG.info("create_user")
        request_headers = build_request_headers(
            access_token, content_type=CONTENT_TYPE_JSON)
        if user['gender'] == 'f':
            user['gender'] = 'female'
        else:
            user['gender'] = 'male'
        payload = user
        response = SESSION.post(f"{app_url}{self.user_url}/",
                                headers=request_headers, params=payload)
        LOG.debug("User created: " + str(response.json()))
        return response

    def read_user(self, app_url, access_token, user_id):
        """Get user info from server"""
        LOG.info("read_user")
        request_headers = build_request_headers(access_token,
                                                content_type=CONTENT_TYPE_JSON)
        response = SESSION.get(f"{app_url}{self.user_url}/{user_id}",
                               headers=request_headers)
        LOG.debug("Get user info: " + str(response.json()))
        return response

    def update_user(self, app_url, access_token, user_id, **kwargs):
        """Update user info on server"""
        LOG.info("update_user")
        request_headers = build_request_headers(access_token,
                                                content_type=CONTENT_TYPE_JSON)
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
        LOG.debug("User updated: " + str(response.json()))
        return response

    def delete_user(self, app_url, access_token, user_id):
        """Delete user from server"""
        LOG.info("delete_user")
        request_headers = build_request_headers(access_token)
        response = SESSION.delete(f"{app_url}{self.user_url}/{user_id}",
                                  headers=request_headers)
        LOG.debug("Users deleted: " + str(user_id))
        return response

    def create_user_todo(self, app_url, access_token, user_id, todo):
        """Create a new To Do for a user on the server"""
        LOG.info("create_user_todo")
        request_headers = build_request_headers(
            access_token, content_type=CONTENT_TYPE_JSON)
        payload = todo
        response = SESSION.post(f"{app_url}{self.user_url}/{user_id}/todos",
                                headers=request_headers, params=payload)
        LOG.debug("Todo new: " + str(response.json()))
        return response
