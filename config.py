import os

SERVER_IM_HOST = '127.0.0.1'
SERVER_IM_PORT = 5000
SERVER_HTTP_HOST = '127.0.0.1'
SERVER_HTTP_PORT = 5001
LISTEN_PORT = 8080
VERSION = '1.0'


ab_path = os.path.abspath(__file__)
dir_path = os.path.dirname(ab_path)
PROJECT_PATH = dir_path
CACHE_PATH = dir_path + '/static/cache'
