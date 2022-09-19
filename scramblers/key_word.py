from scramblers.base_scrambler import BaseScrambler


class KeyWord(BaseScrambler):
    def __init__(self, group: str="перестановочный", title: str="Ключевое слово или фраза", key_word="Lollipop"):
        super().__init__(group, title)
        self.__key_word = key_word

    @staticmethod
    def sort_func(value):
        return ord(value[0])

    def encode(self, text) -> str:
        # разделим текст на блоки, имеющие длину ключевой строки
        text_blocks = [text[x:x+len(self.__key_word)] for x in range(0, len(text), len(self.__key_word))]
        # сформируем пары (символ, индекс символа в ключевой строке) и отсортируем эти пары по коду символа в ASCII
        columns_queue = [(symbol, i) for i, symbol in enumerate(self.__key_word, 0)]
        columns_queue.sort(key=KeyWord.sort_func)
        ans = []
        # в порядке сортировки столбцов сформируем результирующий текст
        for value in columns_queue:
            ind = value[1]
            for text_block in text_blocks:
                if len(text_block) > ind:
                    ans.append(text_block[ind])
        return "".join(ans)

    def decode(self, text) -> str:
        rows_quantity = len([x for x in range(0, len(text), len(self.__key_word))])
        columns_items_quantities = [
            rows_quantity if (rows_quantity - 1) * len(self.__key_word) + i + 1 <= len(text)
            else rows_quantity - 1
            for i in range(len(self.__key_word))
        ]
        # сформируем пары (символ, индекс символа в ключевой строке) и отсортируем эти пары по коду символа в ASCII
        columns_queue = [(symbol, i, columns_items_quantities[i]) for i, symbol in enumerate(self.__key_word, 0)]
        columns_queue.sort(key=KeyWord.sort_func)
        # оставим лишь порядок столбцов (на данный момент) и число элементов в столбце
        columns_queue = [(value[1], value[2]) for value in columns_queue]
        # соберем столбцы
        for i in range(len(columns_queue)):
            col_ind, items_quantity = columns_queue[i]
            columns_queue[i] = (col_ind, text[:items_quantity])
            text = text[items_quantity:]
        # сортируем столбцы в правильном порядке
        columns_queue.sort(key=lambda x: x[0])
        columns_queue = [col_str for col_ind, col_str in columns_queue]
        last_row_items_quantity = len([string for string in columns_queue if len(string) == rows_quantity])
        # сформируем блоки текста (которые останется соединить для получения исходного текста)
        last_row = "".join([columns_queue[i][-1] for i in range(last_row_items_quantity)])
        columns_queue = [column_queue[:rows_quantity - 1] for column_queue in columns_queue]
        rows = list(zip(*columns_queue))
        for i in range(len(rows)):
            rows[i] = "".join(rows[i])
        rows.append(last_row)
        return "".join(rows)
