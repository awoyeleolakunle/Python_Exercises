class Entry:

    def __init__(self, title, body, id):
        self.__title: str = title
        self.__body: str = body
        self.__id: int = id

    def set_my_entry_title(self, title: str) -> None:
        self.__title = title

    def get_my_entry_title(self) -> str:
        return self.__title

    def set_my_entry_body(self, body) -> None:
        self.__body = body

    def get_my_entry_body(self) -> str:
        return self.__body

    def set_my_entry_id(self, id: int) -> None:
        self.__id = id

    def get_my_id(self) -> int:
        return self.__id

    def __str__(self):
        return f"""
                        Title: {self.get_my_entry_title()}
                        Body: {self.get_my_entry_body()}
                        Id: {self.get_my_id()}
                """


