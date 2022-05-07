from lib.utils import build_request_headers
from config import SESSION, LOG


class Todos:
    def __init__(self):
        self.todo_url = "/todos"

    def get_all_todos(self, app_url, access_token):
        LOG.info("get_all_todos")
        request_headers = build_request_headers(access_token)
        response = SESSION.get(f"{app_url}{self.todo_url}", headers=request_headers)
        return response
