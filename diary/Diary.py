from Banking.InvalidPinException import InvalidPinException
from diary.Entry import Entry


class Diary:
    def __init__(self, username: str, password: str):
        self.__username = username
        self.__password = password
        self.entries: list = []
        self.__isLocked = True
        self.__total_number_of_entry = 0

    def unlocked_diary(self, password: str):
        self.__validate(password)
        self.__isLocked = False

    def is_locked(self):
        return self.__isLocked

    def __validate(self, password: str):
        if self.__password != password:
            raise InvalidPinException("Incorrect password")

    def lock_diary(self):
        self.__isLocked = False

    def create_entry(self, title: str, body: str) -> Entry:
        self.__total_number_of_entry += 1
        entry: Entry = Entry(self.__total_number_of_entry, title, body)
        self.entries.append(entry)
        return entry

    def get_total_number_of_entry(self):
        return len(self.entries)

    def delete_entry(self, id_num: int):
        entry: Entry = self.find_entry_by_id(id_num)
        self.entries.remove(entry)
        self.__total_number_of_entry -= 1

    def find_entry_by_id(self, id_num: int) -> Entry:
        for entry in self.entries:
            if entry.get_id() == id_num:
                return entry

