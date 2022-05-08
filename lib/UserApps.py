from config import LOG, APP_URL
from lib.posts import Posts, generate_fake_post
from lib.users import Users, generate_fake_user
from lib.comments import generate_fake_comment
import random


def create_user_post_comments(login_access_token):
    """Create a post for each user and N comments"""
    LOG.info("create_user_post_comments")
    user = {}
    # Create new user
    new_user = generate_fake_user()
    response_user = Users().create_user(APP_URL, login_access_token, new_user)
    assert response_user.ok
    assert response_user.status_code == 201
    response_data = response_user.json()
    user_id = response_data["id"]
    user['user'] = response_data

    # Create new post
    new_post = generate_fake_post(user_id)
    response_post = Posts().create_post(APP_URL, login_access_token, new_post)
    assert response_post.ok
    assert response_post.status_code == 201
    response_data = response_post.json()
    post_id = response_data["id"]
    user['post'] = response_data

    # Create N comment for this post
    comments = []
    for i in range(random.randint(1, 4)):
        new_comment = generate_fake_comment(post_id)
        response_comment = Posts().create_post_comment(APP_URL, login_access_token, post_id, new_comment)
        comment = response_comment.json()
        assert response_comment.ok
        assert response_comment.status_code == 201
        comments.append(comment)

    user['post']['comments'] = comments
    return user
