from scramblers.base_scrambler import BaseScrambler
from prettytable import PrettyTable


class ScramblersMaster:
    def __init__(self, scramblers_collection: list):
        self.__scramblers_collection = scramblers_collection

    def process_all(self, text):
        ans_table = PrettyTable(
            ["№", "Name", "Type", "Input string", "encoding result", "successfully encoded", "encoding logs", "decoding result", "successfully decoded", "decoding logs"])
        for i, scrambler in enumerate(self.__scramblers_collection, start=1):
            class_name = type(scrambler).__name__
            encoding_result = ""
            successfully_encoded = True
            encodin_logs = []
            decoding_result = ""
            successfully_decoded = True
            decodin_logs = []
            try:
                encoding_result = scrambler.encode(text)
            except Exception as e:
                successfully_encoded = False
                encodin_logs.append(str(e))
                encoding_result = ""
            try:
                decoding_result = scrambler.decode(encoding_result) if successfully_encoded else ""
            except Exception as e:
                successfully_decoded = False
                decodin_logs.append(str(e))
            BaseScrambler.save_in_file(encoding_result, class_name)
            ans_table.add_row([str(i), class_name, scrambler.group, text, encoding_result, str(successfully_encoded), "\n".join(encodin_logs), decoding_result, str(successfully_decoded), "\n".join(decodin_logs)])
        return ans_table
