class FileIO:
    def __init__(self):
        self._lines = None

    def read_lines(self, path):
        with open(path) as file:
            self._lines = file.readlines()

    @property
    def lines(self):
        return self._lines

    @lines.setter
    def lines(self, lines):
        self._lines = lines

    @staticmethod
    def write_to_file(string, path):
        with open(path, "a") as file:
            file.write(string)


def main():
    f = FileIO()
    f.read_lines("codification.txt")
    for string in f.lines:
        s = string.split()
        print(s[0], s[1])