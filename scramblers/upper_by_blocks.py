from scramblers.base_scrambler import BaseScrambler


class UpperByBlocks(BaseScrambler):
    BLOCK = 4

    def __init__(self, group="перестановочный", title='Большими буквами, по блокам одинаковой длины'):
        BaseScrambler.__init__(self, group, title)

    def encode(self, text) -> str:
        without_spaces = "".join(text.upper().split(" "))
        return " ".join([without_spaces[x:x+UpperByBlocks.BLOCK] for x in range(0, len(without_spaces), UpperByBlocks.BLOCK)])

    def decode(self, text) -> str:
        raise Exception("Точное восстановление проблематично!!!")
