from scramblers.base_scrambler import BaseScrambler


class AffineTransformation(BaseScrambler):
    ALPHABET = [
        "А", "Б", "В", "Г", "Д", "Е", "Ё", "Ж", "З", "И", "Й", "К", "Л", "М",
        "Н", "О", "П", "Р","С", "Т", "У", "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Э",
        "Ю", "Я", "а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к",
        "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш",
        "щ", "ъ", "ы", "ь", "э", "ю", "я", ".", ",", " ", "!", "?", ":", "-",
    ]

    def __init__(self, group = 'подстановочный', title = "Аффинное преобразование", k1=151, k2=7, k1_reversed=51):
        super().__init__(group, title)
        """
        Количество символов алфавита = 70
        Поэтому взят ключ к1 = 151 (они имеют НОД = 1)
        """
        self.__k1 = k1
        self.__k2 = k2
        self.__k1_reversed = k1_reversed

    def __get_ci(self, symbol: str):
        return self.ALPHABET[(self.__k1 * self.ALPHABET.index(symbol) + self.__k2) % len(self.ALPHABET)]

    def __get_ai(self, symbol: str):
        return self.ALPHABET[self.__k1_reversed * (self.ALPHABET.index(symbol) + len(self.ALPHABET) - self.__k2) % len(self.ALPHABET)]

    def encode(self, text) -> str:
        for symbol in text:
            if symbol not in self.ALPHABET:
                raise Exception("Сообщение содержит недопустимые символы!")
        return "".join([self.__get_ci(symbol) for symbol in text])

    def decode(self, text) -> str:
        return "".join([self.__get_ai(symbol) for symbol in text])
