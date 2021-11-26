import socket
import json
import asyncio

from config import SERVER_IM_HOST, SERVER_IM_PORT, LISTEN_PORT

# 消息比特字符终结标识
MESSAGE_OVER_FLAG = b'2xx@oo$n'


class MsgHandler:
    def __init__(self, s_host=SERVER_IM_HOST, s_port=SERVER_IM_PORT):
        self._server_host = s_host
        self._server_port = s_port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, True)
        self.s.ioctl(socket.SIO_KEEPALIVE_VALS, (1, 5*1000, 10*1000))
        self.s.connect((self._server_host, self._server_port))

    def listening(self, window_obj):
        try:
            bytes_queue = b''
            while True:
                new_bytes = self.s.recv(2048)
                if new_bytes:
                    bytes_queue += new_bytes
                    byte_split = bytes_queue.split(MESSAGE_OVER_FLAG)
                    if len(byte_split) == 2:
                        byte_content, bytes_queue = byte_split
                        data = json.loads(byte_content.decode("utf-8"))
                        content = data["content"]
                        window_obj.his_content.insertPlainText(content)
        except:
            self.s.close()

    def send(self, content):
        content = json.dumps(content)
        self.s.send(bytes(content, encoding="utf-8") + MESSAGE_OVER_FLAG)

    def close(self):
        self.s.close()
