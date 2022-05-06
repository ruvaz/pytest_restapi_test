from lib.comments import Comments
from config import APP_URL, LOG


def test_get_all_comments(login_access_token):
    LOG.info("test_get_all_comments")
    response = Comments().get_all_comments(APP_URL, login_access_token)
    LOG.debug(response)
    assert response.ok

# pytest -v -s tests\comments\test_comments.py
# pytest --html=reports/restapi_fwk_report.html --self-contained-html tests\comments\test_comments.py




#
# def test_cud_comment(login_as_admin):
#     LOG.info("test_cud_comment")
#     response = Comments().create_comment(APP_URL, login_as_admin, "first post")
#     assert response.ok
#     response_data = response.json()
#     comment_id = response_data["id"]
#     LOG.debug(response_data)
#     assert response_data["comment_text"] == "first post"
#
#     response = Comments().update_comment(APP_URL, login_as_admin, comment_id,
#                                          message="updated to second post",
#                                          likes=3
#                                          )
#     assert response.ok
#     response_data = response.json()
#     LOG.debug(response_data)
#     assert response_data["comment_text"] == "updated to second post"
#     assert response_data["likes"] == 3
#
#     response = Comments().delete_comment(APP_URL, login_as_admin, comment_id)
#     assert response.ok
#     response_data = response.json()
#     LOG.debug(response_data)
#     assert response_data["detail"] == f"Deleted comment {comment_id}"
