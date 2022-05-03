from typing import TextIO


class File:
    def __init__(self, name: str, mode: str) -> None:
        self.__name = name
        self.__mode = mode

    def __enter__(self) -> TextIO:
        try:
            self.file = open(self.__name, self.__mode)
        except FileNotFoundError:
            self.file = open(self.__name, 'w').close()
            self.file = open(self.__name, self.__mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with File('txt.txt', 'r') as file:
    print(file.read())
