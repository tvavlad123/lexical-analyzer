from anlex.file_io import *


class Tokenize:
    def __init__(self):
        self._pattern = ['\t', '\n', ',', ';', '(', ')', '{', '}', '[', ']', '#', '<', '>'] + \
                       ['+', '-', '*', '/', '%', '=', '!', ".", "+=", "++"]

    def parse(self, string):
        for token in self._pattern:
            string = self.splitter(string, token)
        return string

    @staticmethod
    def splitter(string, token):
        if token in string:
            helper = string.split(token)
            string = (" " + token + " ").join(helper)
        return string


def test():
    tok = Tokenize()
    file = FileIO()
    file.read_lines("program.txt")
    for line in file.lines:
        print(tok.parse(line).strip())

