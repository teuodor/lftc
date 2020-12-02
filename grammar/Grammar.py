from ProductionRule import ProductionRule
from ProductionRule import Symbol
from ProductionRule import SymbolType


class Grammar:
    def __init__(self, file_name):
        self.__production_rules = []
        self.__file_name = file_name

    def populate_grammar(self):
        f = open(self.__file_name, "r")
        content = f.readlines()
        for line in content:
            line = line.strip("\n")
            line = line.split(" -> ")
            if len(line) == 2:
                before_left_side = line[0]
                before_right_side = line[1]
                before_right_side = before_right_side.split(" ")
                right_side = []
                for i in range(len(before_right_side)):
                    if before_right_side[i][len(before_right_side[i]) - 1] == ";" and len(before_right_side[i]) > 1:
                        to_push = before_right_side[i][:len(before_right_side[i]) - 1]
                        if to_push[0] == "<" and to_push[len(to_push) - 1] == ">":
                            right_side.append(Symbol(SymbolType.NON_TERMINAL, to_push))
                        else:
                            right_side.append(Symbol(SymbolType.TERMINAL, to_push))
                        right_side.append(Symbol(SymbolType.TERMINAL, ";"))
                    else:
                        if before_right_side[i][0] == "<" and before_right_side[i][len(before_right_side[i]) - 1] == ">":
                            right_side.append(Symbol(SymbolType.NON_TERMINAL, before_right_side[i]))
                        else:
                            right_side.append(Symbol(SymbolType.TERMINAL, before_right_side[i]))

                left_side = Symbol(SymbolType.NON_TERMINAL, before_left_side)

                production_rule = ProductionRule(left_side, right_side)
                self.__production_rules.append(production_rule)

    def set_non_terminal(self):
        to_return = set()
        for rule in self.__production_rules:
            to_return.add(rule.left_side.string)
            for symbol in rule.right_side:
                if symbol.is_non_terminal():
                    to_return.add(symbol.string)
        return to_return

    def set_terminal(self):
        to_return = set()
        for rule in self.__production_rules:
            for symbol in rule.right_side:
                if symbol.is_terminal():
                    to_return.add(symbol.string)
        return to_return

    def set_production_rules(self):
        to_return = []
        for rule in self.__production_rules:
            right_side = ""
            for el in rule.right_side:
                right_side += str(el) + " "
            to_return.append(str(rule.left_side) + " -> " + right_side)
        return to_return

    def set_production_rules_terminal(self, terminal):
        to_return = []
        for rule in self.__production_rules:
            for eli in rule.right_side:
                if terminal == eli.string:
                    right_side = ""
                    for el in rule.right_side:
                        right_side += str(el) + " "
                    to_return.append(str(rule.left_side) + " -> " + right_side)
                    break
        return to_return
