class DictionarySymbolTable:
    class Element:
        def __init__(self, cod_atom, poz_ts):
            self._cod_atom = cod_atom
            self._poz_ts = poz_ts

        @property
        def cod_atom(self):
            return self._cod_atom

        @cod_atom.setter
        def cod_atom(self, cod_atom):
            self._cod_atom = cod_atom

        @property
        def poz_ts(self):
            return self._poz_ts

        @poz_ts.setter
        def poz_ts(self, poz_ts):
            self._poz_ts = poz_ts

        def __repr__(self) -> str:
            return 'Element(Cod atom, Pozitie in TS): {0}, {1}'.format(self._cod_atom, self._poz_ts)

    list_elements = []

    @staticmethod
    def add_element(element):
        DictionarySymbolTable.list_elements.append(element)


def main():
    element = DictionarySymbolTable.Element(11, 13)
    DictionarySymbolTable.add_element(element)
    print(DictionarySymbolTable.list_elements)
