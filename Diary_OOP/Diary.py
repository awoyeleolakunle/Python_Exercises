from Diary_OOP.Entry import Entry


class Diary:

    def __init__(self):
        self.__my_entry = []

    def create_an_entry_for(self, title: str, body: str):
        id: int = len(self.__my_entry) + 1
        entry: Entry = Entry(title, body, id)
        self.__my_entry.append(entry)

    def get_total_of_my_entries(self) -> int:
        return len(self.__my_entry)

    def view_my_entry(self, id: int) -> str:
        return self.__my_entry.__getitem__(id - 1)

    def delete_my_entry(self, id: int) -> None:
        for entry in self.__my_entry:
            self.__my_entry.pop(id - 1)

    def edit_my_entry_title(self, id: int, title: str):
        for entry in self.__my_entry:
            if entry.get_my_id() == id:
                entry.set_my_entry_title(title)

    def edit_my_entry_body(self, id: int, body: str) -> None:
        for entry in self.__my_entry:
            if entry.get_my_id() == id:
                entry.set_my_entry_body(body)

    def validate_id(self, id: int):
        if id < 1 or id > len(self.__my_entry):
            raise ValueError
