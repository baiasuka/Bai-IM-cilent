import os

from config import CACHE_PATH
from common.file_loader import FileDownloader
from common.utils import check_file_existed


def replace_remote_pic_to_local(soup_obj):
    """
    替换消息框中的远程图片为本地图片
    :param soup_obj:
    :return:
    """
    for image in soup_obj.find_all('img'):
        url = image["src"]
        file_name = os.path.basename(url)
        file_path = CACHE_PATH + '\%s' % file_name
        if check_file_existed(file_path):
            image["src"] = file_path
        else:
            image["src"] = FileDownloader.download(url, CACHE_PATH)
    return soup_obj
