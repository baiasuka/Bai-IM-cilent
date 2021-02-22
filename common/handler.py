import re


def check_username(username):
    """
    检查用户名格式
    :param username:
    :return:
    """
    pattern = "^[a-zA-Z0-9][a-zA-Z0-9\_]{7,31}$"
    r = re.match(pattern, username)
    if r:
        return True
    else:
        return False


def check_password(password):
    """
    检查密码格式
    :param password:
    :return:
    """
    pattern = "^[a-zA-Z0-9]{8,32}$"
    r = re.match(pattern, password)
    if r:
        return True
    else:
        return False

