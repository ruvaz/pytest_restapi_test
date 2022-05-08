from lib.utils import build_request_headers
from config import SESSION, LOG, FAKER


def generate_fake_comment(post_id):
    """Generate comment for a post"""
    profile = FAKER.simple_profile()
    return {
        "post_id": post_id,
        "name": profile['name'],
        "email": profile['mail'],
        "body": FAKER.sentence()
    }


class Comments:

    def __init__(self):
        self.comment_url = "/comments"

    def get_all_comments(self, app_url, access_token):
        """Get all comments from server"""
        LOG.info("get_all_comments")
        request_headers = build_request_headers(access_token)
        response = SESSION.get(f"{app_url}{self.comment_url}", headers=request_headers)
        LOG.debug("All comments: " + str(response.json()))
        return response
