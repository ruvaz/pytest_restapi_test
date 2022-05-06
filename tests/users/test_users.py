from lib.users import Users
from lib.posts import Posts
from config import APP_URL, LOG, FAKER


#  source C:/Users/rv1066/.virtualenvs/test_api/Scripts/activate
# pytest --html=reports/restapi_fwk_report.html --self-contained-html tests\users\test_users.py

def test_get_all_users(login_access_token):
    LOG.info("test_get_all_users")
    response = Users().get_all_users(APP_URL, login_access_token)
    LOG.debug(response)
    assert response.ok


def test_crud_users(login_access_token):
    LOG.info("test_crud_user")

    # Create new user
    profile = FAKER.simple_profile()
    new_user = {"name": profile['name'],
                "gender": profile['sex'],
                "email": profile['mail'],
                "status": 'active'}
    response = Users().create_user(APP_URL, login_access_token, new_user)
    assert response.ok
    assert response.status_code == 201
    response_data = response.json()
    user_id = response_data["id"]

    # Get user
    response = Users().read_user(APP_URL, login_access_token, user_id)
    LOG.debug(response.json())
    assert response.status_code == 200
    assert response.ok

    LOG.info("Update user")
    new_profile = FAKER.simple_profile()
    response = Users().update_user(APP_URL, login_access_token, user_id,
                                   name=new_profile['name'],
                                   email=new_profile['mail'])
    assert response.ok
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["name"] == new_profile['name']
    assert response_data["email"] == new_profile['mail']

    # Delete user
    response = Users().delete_user(APP_URL, login_access_token, user_id)
    assert response.ok
    assert response.status_code == 204
    assert response.text == ''


def test_create_user_post_comment(login_access_token):
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
