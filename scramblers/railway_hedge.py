from scramblers.base_scrambler import BaseScrambler


class RailwayHedge(BaseScrambler):
    def __init__(self, group="перестановочный", title="Железнодорожная изгородь", height=3):
        super().__init__(group, title)
        self.__height = height

    def encode(self, text) -> str:
        # Выделим n слоев (n равно высоте изгороди)
        ans = [[] for i in range(self.__height)]
        vector = "down"
        symb_ind = 0
        row = 0
        # будем двигаться зиг-загом, меняя направление и добавляя в каждый слой попутно символы
        while symb_ind < len(text):
            ans[row].append(text[symb_ind])
            if vector == "down":
                row += 1
            else:
                row -= 1
            if row == self.__height - 1:
                vector = "up"
            elif row == 0:
                vector = "down"
            symb_ind += 1
        # сделаем строки из каждого слоя
        for i in range(self.__height):
            ans[i] = "".join(ans[i])
        return "".join(ans)

    def decode(self, text) -> str:
        # layer_step - число элементов до очередного элемента на текущем уровне
        layers_steps = ([(1 + 2 * (i - 1)) for i in range(self.__height - 1, 0, -1)] * 2)[:self.__height]
        substrings_lens = []
        for i, layers_step in enumerate(layers_steps, 0):
            substrings_lens.append(len(text[i::layers_step + 1]))
        # substrings_lens - количество элементов на каждом уровне - важная характеристика для восстановления текста
        substrings = []
        # т.к. текст представляет из себя конкатенацию слоев исходного текста, разобьем его на слои
        for substring_len in substrings_lens:
            substrings.append(text[:substring_len])
            text = text[substring_len:]
        ans = []
        vector = "down"
        row = 0
        # теперь остается двигаясь по зиг-загу "отрезать" по символу из каждого слоя
        for i in range(sum(substrings_lens)):
            ans.append(substrings[row][0])
            substrings[row] = substrings[row][1:]
            if vector == "down":
                row += 1
            else:
                row -= 1
            if row == self.__height - 1:
                vector = "up"
            elif row == 0:
                vector = "down"
        return "".join(ans)
