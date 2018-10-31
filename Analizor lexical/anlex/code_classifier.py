from collections import OrderedDict
from anlex.file_io import *


class Classifier:
    def __init__(self):
        self._ordered_dict = OrderedDict()

    def build(self):
        file = FileIO()
        file.read_lines("codification.txt")
        codes_list = []
        for string in file.lines:
            codes_list.append(string.split())
        for key, value in codes_list:
            self._ordered_dict[key] = value

    @property
    def ordered_dict(self):
        return self._ordered_dict

    @ordered_dict.setter
    def ordered_dict(self, ordered_dict):
        self._ordered_dict = ordered_dict


def main():
    classifier = Classifier()
    classifier.build()
    print(classifier.ordered_dict)
