import wget
import ssl
import os
import tempfile

from config import CACHE_PATH


class FileDownloader:
    """
    用于文件下载
    """
    @staticmethod
    def download(url, target_dir):
        """
        使用wget下载图片
        :param path: 图片地址
        :param target_dir: 保存至目标文件夹
        :return:
        """
        try:
            file_name = os.path.basename(url)
            file_path = target_dir + '\%s' % file_name
            wget.download(url, file_path)
            return file_path
        except Exception as e:
            return ''


class FileUploader:
    """
    用于文件上传
    """
    pass
