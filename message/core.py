import socket
import json
import asyncio

from config import SERVER_HOST, SERVER_IM_PORT, LISTEN_PORT

# 消息比特字符终结标识
MESSAGE_OVER_SIGN = b'xx@oo$n'


class MsgHandler:
    def __init__(self, s_host=SERVER_HOST, s_port=SERVER_IM_PORT):
        self._server_host = s_host
        self._server_port = s_port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, True)
        self.s.ioctl(socket.SIO_KEEPALIVE_VALS, (1, 5*1000, 10*1000))
        self.s.connect((self._server_host, self._server_port))

    def listening(self, window_obj):
        while True:
            raw_data = self.s.recv(2048)
            if raw_data:
                try:
                    data = json.loads(raw_data.decode("utf-8"))
                    content = data["content"]
                    window_obj.his_content.insertPlainText(content)
                except Exception as e:
                    print(e)

    def send(self, content):
        content = json.dumps(content)
        self.s.send(bytes(content, encoding="utf-8"))
