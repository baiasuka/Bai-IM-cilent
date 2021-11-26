import requests
import json

import config


class HttpRequestSender:
    """
    封装的请求类
    """
    def __init__(self):
        self._host = config.SERVER_HTTP_HOST
        self._port = config.SERVER_HTTP_PORT
        self._root_url = '%s:%s' % (self._host, self._port)
        self._headers = {
            "auth-version": config.VERSION
        }

    def add_headers_key(self, key, value):
        """
        请求头增加键值
        :param key:
        :param value:
        :return:
        """
        self._headers[key] = value
        return True

    def delete_header_key(self, key):
        """
        请求头删除键值
        :param key:
        :return:
        """
        return self._headers.pop(key, None)

    def login(self, account, password):
        """
        请求登录接口
        :param account:
        :param password:
        :return:
        """
        url = self._root_url + '/auth/login/account'
        data = {
            "account": account,
            "password": password
        }
        response = requests.post(url, data=data, timeout=5, headers=self._headers)
        return json.loads(response.text)

    def signup(self, account, password, email):
        """
        请求注册接口
        :param account:
        :param password:
        :return:
        """
        url = self._root_url + '/auth/signup/account'
        data = {
            "account": account,
            "password": password,
            "email": email
        }
        response = requests.post(url, data=data, timeout=5)
        return json.loads(response.text)

    def get_room_list(self):
        """
        获取大厅房间列表
        :return:
        """
        url = self._root_url + '/hall/room_list'
        response = requests.get(url, timeout=5, headers=self._headers)
        return json.loads(response.text)

    def create_room(self):
        """
        创建房间
        :return:
        """
        pass
