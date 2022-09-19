from scramblers.base_scrambler import BaseScrambler


class UpperWithoutSpaces(BaseScrambler):
    def __init__(self, group="перестановочный", title="Большими буквами, без пробелов"):
        BaseScrambler.__init__(self, group, title)

    def encode(self, text) -> str:
        return "".join(text.upper().split(" "))

    def decode(self, text) -> str:
        raise Exception("Точное восстановление проблематично!!!")
