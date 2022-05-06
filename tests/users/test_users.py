from lib.users import Users
from config import APP_URL, LOG, FAKER


def test_get_all_users(login_access_token):
    LOG.info("test_get_all_users")
    response = Users().get_all_users(APP_URL, login_access_token)
    LOG.debug(response)
    assert response.ok


def test_crud_users(login_access_token):
    LOG.info("test_crud_user")
    profile = FAKER.simple_profile()
    if profile['sex'] == 'f':
        gender = 'female'
    else:
        gender = 'male'
    new_user = {"name": profile['name'],
                "gender": gender,
                "email": profile['mail'],
                "status": 'active'}

    LOG.info("Create new user")
    response = Users().create_user(APP_URL, login_access_token, new_user)
    assert response.ok
    response_data = response.json()
    user_id = response_data["id"]

    new_profile = FAKER.simple_profile()

    LOG.info("Get user")
    response = Users().read_user(APP_URL, login_access_token, user_id)
    LOG.debug(response.json())
    assert response.status_code == 200
    assert response.ok

    LOG.info("Update user")
    response = Users().update_user(APP_URL, login_access_token, user_id,
                                   name=new_profile['name'],
                                   email=new_profile['mail'])
    assert response.ok
    response_data = response.json()
    assert response_data["name"] == new_profile['name']
    assert response_data["email"] == new_profile['mail']

    LOG.info("Delete user")
    response = Users().delete_user(APP_URL, login_access_token, user_id)
    assert response.ok
    assert response.status_code == 204
    assert response.text == ''

