from enum import Enum


class SymbolType(Enum):
    TERMINAL = 1,
    NON_TERMINAL = 2


class Symbol:
    def __init__(self, symbol_type, string):
        self.__symbol_type = symbol_type
        self.string = string

    def is_terminal(self):
        return self.__symbol_type == SymbolType.TERMINAL

    def is_non_terminal(self):
        return self.__symbol_type == SymbolType.NON_TERMINAL

    def __str__(self):
        to_return = ""
        if self.is_terminal():
            to_return += "[" + self.string + "]"
        elif self.is_non_terminal():
            to_return += self.string

        return to_return


class ProductionRule:
    def __init__(self, left_symbol, right_symbols):
        self.left_side = left_symbol
        self.right_side = right_symbols

