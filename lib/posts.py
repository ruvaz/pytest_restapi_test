from lib.utils import build_request_headers
from config import SESSION, LOG, FAKER, CONTENT_TYPE_JSON


def generate_fake_post(user_id):
    """Generate content for a post"""
    return {
        "user_id": user_id,
        "title": FAKER.sentence(),
        "body": FAKER.paragraph(nb_sentences=7)
    }


class Posts:
    def __init__(self):
        self.post_url = "/posts"

    def get_all_posts(self, app_url, access_token):
        """Get all the posts from server"""
        LOG.info("get_all_posts")
        request_headers = build_request_headers(access_token)
        response = SESSION.get(f"{app_url}{self.post_url}", headers=request_headers)
        LOG.debug("All posts: " + str(response.json()))
        return response

    def create_post(self, app_url, access_token, post):
        """Create new post from a user"""
        LOG.info("create_post")
        request_headers = build_request_headers(access_token, content_type=CONTENT_TYPE_JSON)
        payload = post
        LOG.debug(f"Request payload: {payload}")
        response = SESSION.post(f"{app_url}{self.post_url}/",
                                headers=request_headers, params=payload)
        LOG.debug("Post created: " + str(response.json()))
        return response

    def create_post_comment(self, app_url, access_token, post_id, comment):
        """Create a new comment on a post"""
        LOG.info("get_post_comments")
        request_headers = build_request_headers(access_token, content_type=CONTENT_TYPE_JSON)
        payload = comment
        response = SESSION.post(f"{app_url}{self.post_url}/{post_id}/comments/",
                                headers=request_headers, params=payload)
        LOG.debug("Comment created in post: " + str(response.json()))
        return response

    def get_post_comments(self, app_url, access_token, post_id):
        """Get the comments of a post"""
        LOG.info("get_post_comments")
        request_headers = build_request_headers(access_token, content_type=CONTENT_TYPE_JSON)
        response = SESSION.get(f"{app_url}{self.post_url}/{post_id}/comments/",
                               headers=request_headers)
        LOG.debug("Get comments in post: " + str(response.json()))
        return response
