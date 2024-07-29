class Cliente:
    def __init__(self, name) -> None:
        self.__name = name

    @property
    def name(self) -> str:
        return self.__name.title()

    @name.setter
    def name(self, name):
        self.__name = name
