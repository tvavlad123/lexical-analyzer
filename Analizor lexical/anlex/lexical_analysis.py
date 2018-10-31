from anlex.code_classifier import *
from anlex.binary_tree import *
from anlex.dict_symbol_table import *
from anlex.parse import *
import re


class LexicalAnalysis:
    def __init__(self):
        classifier = Classifier()
        classifier.build()
        self.ordered_dict = classifier.ordered_dict

    def classify(self, string):
        if string in self.ordered_dict:  # operator, separator sau cuvant rezervat
            return 1
        if re.match(r"[a-zA-z]\w*", string):  # idenfitifactor
            return 2
        if string == "0" or re.match(r"[1-9]\d*.?\d+", string) or re.match(r"[1-9]\d*", string):  # constanta
            return 3
        if len(string) > 8:
            return -1
        return -1

    def lexical_analysis(self):
        identifiers_constants = AVLTree()
        fip = DictionarySymbolTable()
        file = FileIO()
        file.read_lines("program.txt")
        checker = True
        tokenizer = Tokenize()
        for line in file.lines:
            line = tokenizer.parse(line).strip()
            print(line)
            for string in line.split():
                if self.classify(string) == -1:
                    print("EROARE LEXICALA LA ", string)
                    checker = False
                    break
                if not self.classify(string) == 1:
                    identifiers_constants.insert(string)

        for line in file.lines:
            line = tokenizer.parse(line).strip()
            for string in line.split():
                if self.classify(string) == 1:
                    fip.add_element(DictionarySymbolTable.Element(self.ordered_dict[string], -1))
                if self.classify(string) == 2:
                    index = 0
                    for node in identifiers_constants.inorder(identifiers_constants.rootNode):
                        if node.key == string:
                            index = identifiers_constants.inorder(identifiers_constants.rootNode).index(node) + 1
                    fip.add_element(DictionarySymbolTable.Element(0, index))
                if self.classify(string) == 3:
                    index = 0
                    for node in identifiers_constants.inorder(identifiers_constants.rootNode):
                        if node.key == string:
                            index = identifiers_constants.inorder(identifiers_constants.rootNode).index(node) + 1
                    fip.add_element(DictionarySymbolTable.Element(1, index))
        if checker is True:
            output = FileIO()
            for element in fip.list_elements:
                print(str(element.cod_atom) + " | " + str(element.poz_ts))
            output.write_to_file("IDENTIFICATORI SI CONSTANTE \n", "output.txt")
            output.write_to_file("ID          |          Pozitie \n", "output.txt")
            for i in identifiers_constants.inorder(identifiers_constants.rootNode):
                output.write_to_file(str(i.key) + "          |          " +
                                     str(identifiers_constants.inorder(identifiers_constants.rootNode).index(i) + 1)
                                     + "\n", "output.txt")


def main():
    lex = LexicalAnalysis()
    lex.lexical_analysis()


main()
