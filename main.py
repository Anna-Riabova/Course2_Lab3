class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.__name = name
        self.__author = author

    def __str__(self):
        return f"Книга {self.__name}. Автор {self.__author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.__name!r}, author={self.__author!r})"

class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        self.__name = name
        self.__author = author
        self.pages = pages
        if not isinstance(pages, (int)):
            raise TypeError("Количество страниц должно быть целым числом")
        if pages < 0:
            raise ValueError("Количество страниц не может быть отрицательным числом")

    def __str__(self):
        return f"Книга {self.__name}. Автор {self.__author}. Страниц {self.pages}"

class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        """
        super().__init__(name, author)

        Я попробовала инициализировать унаследованные поля с помощью метода super,
        но Python не пропускал приватные поля
        """
        self.__name = name
        self.__author = author
        self.duration = duration
        if not isinstance(duration, (float)):
            raise TypeError("Продолжительность должна быть вещественым числом")
        if duration < 0:
            raise ValueError("Продолжительность не может быть отрицательным числом")

    def __str__(self):
        return f"Книга {self.__name}. Автор {self.__author}. Продолжительность {self.duration}"


if __name__ == "__main__":
    book1 = Book('Преступление', 'Достоевский')
    book1.__name = 'Пушкин'
    print(book1.__str__())

    book2 = PaperBook('Преступление', 'Достоевский',400)
    print(book2.__str__())

    book3 = AudioBook('Преступление', 'Достоевский',40.5)
    print(book3.__str__())
