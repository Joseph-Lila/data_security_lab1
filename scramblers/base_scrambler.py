class BaseScrambler:
    def __init__(self, group: str, title: str):
        self.__group = group

    @property
    def group(self):
        return self.__group

    def encode(self, text) -> str:
        raise Exception("Метод шифрования не реализован!")

    def decode(self, text) -> str:
        raise Exception("Метод дешифрования не реализован!")

    @staticmethod
    def save_in_file(text: str, file_name: str):
        try:
            # dir_path = filechooser.choose_dir()
            # full_path = os.path.join(dir_path[0], file_name + ".txt")
            # f = open(full_path, "w")
            f = open(f"{file_name}.txt", "w")
            f.write(text)
            f.close()
        except Exception:
            pass

    @staticmethod
    def read_from_file(file_name) -> str:
        try:
            # dir_path = filechooser.choose_dir()
            # full_path = os.path.join(dir_path[0], file_name + ".txt")
            # f = open(full_path, 'r')
            f = open(f"{file_name}.txt", "r")
            ans = f.read()
            f.close()
        except Exception:
            ans = ''
        return ans

