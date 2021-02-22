import datetime


class Message:
    """
    聊天的单条消息对象
    """
    def __init__(self, text):
        cur_time = datetime.datetime.now()
        self.datetime = cur_time.strftime("%Y/%m/%d %H:%M:%S")
        self.text = text


class HistoryMessage:
    """
    历史消息
    """
    def __init__(self):
        self.his = []

    def addText(self, text):
        self.his.append(text)

    def toText(self):
        return "\n".join(self.his)
