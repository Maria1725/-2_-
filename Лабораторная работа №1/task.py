import doctest


class Box:
    def __init__(self, volume: int, material: str):
        """"
        Создание и подготовка к работе объекта "Шкатулка"
        :param volume: Свободный объем в шкатулке
        :param material: Материал украшений в шкатулке
        Пример:
        >>> box = Box(200, "Золото")
        """

        if not isinstance(volume, int):
            raise TypeError("Свободный объем в шкатулке должен быть типа int")
        if not volume > 0:
            raise ValueError("Свободный объем в шкатулке должен быть положительным числом")
        self.volume = volume

        if not isinstance(material, str):
            raise TypeError("Материал украшений в шкатулке должен быть типа str")
        self.material = material

    def free_volume(self, volume_of_chain: int) -> None:
        """
        Функция которая проверяет войдет ли цепочка в шкатулку
        :param volume_of_chain: Объем цепочки

        :raise ValueError: Если объем цепочки превышает свобоный объем в шкатулке,
        то возвращается ошибка

        Примеры:
        >>> box = Box(200, "Золото")
        >>> box.free_volume(5)
        """
        ...

        if not isinstance(volume_of_chain, int):
            raise TypeError("Объем цепочки должен быть типа int")
        if not volume_of_chain > 0:
            raise ValueError("Объем цепочки должен быть положительным числом")

    def material_chain(self) -> bool:
        """
        Функция которая проверяет совместимость материала цепочки с материалом других украшений в шкатулке

        :return: Совместимость материала цепочки с материалом других украшений в шкатулке

        Примеры:
        >>> box = Box(200, "Золото")
        >>> box.material_chain()
        """
        ...


class Wardrobe:
    def __init__(self, shelves: int, number_of_occupied_shelves: int):
        """"
        Создание и подготовка к работе объекта "Шкаф"
        :param shelves: Количество полок шкафа
        :param number_of_occupied_shelves: Количество занятых полок шкафа
        Пример:
        >>> wardrobe = Wardrobe(6, 1)
        """

        if not isinstance(shelves, int):
            raise TypeError("Количество полок шкафа должно быть типа int")
        if not shelves > 0:
            raise ValueError("Количество полок шкафа должно быть положительным числом")
        self.shelves = shelves

        if not isinstance(number_of_occupied_shelves, int):
            raise TypeError("Количество занятых полок шкафа должно быть типа int")
        if number_of_occupied_shelves < 0:
            raise ValueError("Количество занятых полок шкафа должно не должно быть отрицательным числом")
        self.number_of_occupied_shelves = number_of_occupied_shelves

    def free_shelves(self) -> bool:
        """
        Функция которая проверяет есть ли свободные полки в шкафу

        :return: Является ли шкаф пустым

        Примеры:
        >>> wardrobe = Wardrobe(6, 0)
        >>> wardrobe.free_shelves()
        """
        ...

    def occupied_shelves(self, add_occupied_shelves: int) -> None:
        """
        Функция которая добавляет количество занятых полок в шкафу
        :param add_occupied_shelves: Количество добавляемых занятых полок в шкафу

        :raise ValueError: Если количество добавляемых занятых полок превышает количество свободных полок,
        то возвращается ошибка

        Примеры:
        >>> wardrobe = Wardrobe(6, 1)
        >>> wardrobe.occupied_shelves(2)
        """
        if not isinstance(add_occupied_shelves, int):
            raise TypeError("Количество добавляемых занятых полок шкафа должно быть типа int")
        if not add_occupied_shelves > 0:
            raise ValueError("Количество добавляемых занятых полок шкафа должно быть положительным числом")
        ...


class Picture:
    def __init__(self, genre: str, color: str):
        """"
        Создание и подготовка к работе объекта "Картина"
        :param genre: Жанр картины
        :param color: Преобладающий цвет картины

        Пример:
        >>> picture = Picture("Пейзаж", "Зеленый")
        """

        if not isinstance(genre, str):
            raise TypeError("Жанр картины должен быть типа str")
        self.genre = genre

        if not isinstance(color, str):
            raise TypeError("Преобладающий цвет картины должен быть типа str")
        self.color = color

    def style_genre(self) -> bool:
        """
        Функция которая проверяет подходит ли жанр картины к стилю интерьера

        :return: Подходит ли жанр картины к стилю интерьера

        Примеры:
        >>> picture = Picture("Пейзаж", "Зеленый")
        >>> picture.style_genre()
        """
        ...

    def style_color(self) -> bool:
        """
        Функция которая проверяет подходит ли преобладающий цвет картины к стилю интерьера

        :return: Подходит ли преобладающий цвет картины к стилю интерьера

        Примеры:
        >>> picture = Picture("Пейзаж", "Зеленый")
        >>> picture.style_color()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
