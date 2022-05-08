from lib import UserApps
from lib.posts import Posts
from lib.users import Users, generate_fake_user, generate_fake_todo
from config import APP_URL, LOG

users_list = []


def test_crud_users(login_access_token):
    LOG.info("test_crud_user")

    # Create new user
    new_user = generate_fake_user()
    response_user = Users().create_user(APP_URL, login_access_token, new_user)
    assert response_user.ok
    assert response_user.status_code == 201
    user_id = response_user.json()["id"]
    LOG.info("User Created: " + str(response_user.json()))

    # Get user
    response_user = Users().read_user(APP_URL, login_access_token, user_id)
    LOG.debug(response_user.json())
    assert response_user.status_code == 200
    assert response_user.ok
    LOG.info("Get User Info: " + str(response_user.json()))

    updated_profile = generate_fake_user()
    response = Users().update_user(APP_URL, login_access_token, user_id,
                                   name=updated_profile['name'],
                                   email=updated_profile['email'])
    assert response.ok
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["name"] == updated_profile['name']
    assert response_data["email"] == updated_profile['email']
    LOG.info("User Updated: " + str(response_data))

    # Delete user
    response = Users().delete_user(APP_URL, login_access_token, user_id)
    assert response.ok
    assert response.status_code == 204
    assert response.text == ''
    LOG.info("User deleted: " + str(user_id))


def test_create_many_users_post_comments(login_access_token, n_users):
    LOG.info("test_create_many_users_post_comments")
    LOG.info("Num. of Users to create: " + str(n_users))
    # Create post for N users and its comments
    for x in range(int(n_users)):
        item = UserApps.create_user_post_comments(login_access_token)

        # Get comments from endpoint
        response_comments = Posts().get_post_comments(APP_URL, login_access_token, item['post']['id'])
        post_comments = response_comments.json()

        comments_str = ""
        # print in logs posts, and its comments
        for i, c in enumerate(post_comments):
            str1 = f"\t\t\tComments #{i + 1} Author: {c['name']}  Comment: {c['body']}\n"
            comments_str += str1

        report = f"\nUSERS POST & COMMENTS\n\t\tPost #{x + 1:^1} | Post Title: {item['post']['title']:60}  " \
                 f"| Author: {item['user']['name']:60}" \
                 f" \n\t\tPost body: {item['post']['body']:120} \n{comments_str:100} "
        users_list.append(item)
        LOG.info(report)


def test_create_user_todo(login_access_token):
    LOG.info("test_create_user_todo")

    # Create Users Todos
    for i, item in enumerate(users_list):
        user_id = item['user']['id']
        todo = generate_fake_todo(user_id)
        response_todo = Users().create_user_todo(APP_URL, login_access_token, user_id, todo)
        assert response_todo.ok
        users_list[i]['todos'] = todo

    for item in users_list:
        str_user = f"New User To Do\n\tUser To Do: {item['user']['name']:30} | E-mail: {item['user']['email']:30} |" \
                   f"Gender: {item['user']['gender']:30} | Status: {item['user']['status']:30}\n"
        str_todo = f"\tTodos:  {item['todos']['title']:50} | Due: {item['todos']['due_on']:30}"
        LOG.info(str_user + str_todo)
