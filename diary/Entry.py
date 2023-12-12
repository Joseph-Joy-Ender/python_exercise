from datetime import datetime


def date():
    return datetime.now()


class Entry:

    def __init__(self, id_num: int, title: str, body: str):
        self.__id = id_num
        self.__title = title
        self.__body = body

    def get_id(self):
        return self.__id

    def get_title(self):
        return self.__title

    def set_title(self, title: str):
        self.__title = title

    def set_body(self, body: str):
        self.__body = body

    def __str__(self):
        return f"""
          id: {self.__id}
          title: {self.__title}
          body: {self.__body}
          date: {date()}
           """
