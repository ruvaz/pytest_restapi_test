from lib import UserApps
from lib.posts import Posts
from lib.users import Users, generate_fake_user, generate_fake_todo
from config import APP_URL, LOG, FAKER


#  source C:/Users/rv1066/.virtualenvs/test_api/Scripts/activate
# pytest --html=reports/restapi_fwk_report.html --self-contained-html --users 10 tests\users\test_users.py

def test_get_all_users(login_access_token):
    LOG.info("test_get_all_users")
    response = Users().get_all_users(APP_URL, login_access_token)
    LOG.debug(response)
    assert response.ok


def test_crud_users(login_access_token):
    LOG.info("test_crud_user")

    # Create new user
    new_user = generate_fake_user()
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


def test_create_many_user_post_comment_todo(login_access_token, n_users):
    LOG.info("test_create_many_user_post_comment_todo")
    list_users = []
    num_users = int(n_users)

    # Create post for N users and its comments
    for x in range(num_users):
        item = UserApps.create_user_post_comment(login_access_token)

        # Get comments from endpoint
        response_comments = Posts().get_post_comments(APP_URL, login_access_token, item['post']['id'])
        post_comments = response_comments.json()

        comments_str = ""
        # print in logs posts, and its comments
        for i, c in enumerate(post_comments):
            str1 = f"Comments #{i + 1} Comment author: {c['name']}  Comment: {c['body']}\n"
            comments_str += str1

        linea = f"USERS POST  & COMMENTS\nPost #{x + 1:<10} | Post Title: {item['post']['title']:60}  | Author: {item['user']['name']:60}" \
                f" \nPost body: {item['post']['body']:120} \n{comments_str:100} "
        list_users.append(item)
        LOG.info(linea)

    # Create Users Todos
    for i, item in enumerate(list_users):
        user_id = item['user']['id']
        todo = generate_fake_todo(user_id)
        response_todo = Users().create_todo(APP_URL, login_access_token, user_id, todo)
        assert response_todo.ok
        list_users[i]['todos'] = todo

    for item in list_users:
        str_user = f"TODOS USERS\nUser: {item['user']['name']:30} | E-mail: {item['user']['email']:30} |" \
                   f"Gender: {item['user']['gender']:30} | Status: {item['user']['status']:30}\n"
        str_todo = f"Todos:  {item['todos']['title']:60} |  Due: {item['todos']['due_on']:30}"
        LOG.info(str_user + str_todo)
