from scramblers.base_scrambler import BaseScrambler


class UpperReversed(BaseScrambler):
    def __init__(self, group="перестановочный", title="Большими буквами, слова наоборот"):
        BaseScrambler.__init__(self, group, title)

    def encode(self, text) -> str:
        return " ".join([word[::-1] for word in text.upper().split(" ")])

    def decode(self, text) -> str:
        raise Exception("Точное восстановление проблематично!!!")
