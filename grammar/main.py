from Grammar import Grammar


def menu():
    print("1.Multimea neterminalelor")
    print("2.Multimea terminalelor")
    print("3.Multimea regulior de productie")
    print("4.Multimea regulilor de productie pentru un anumit terminal")
    print("0.Exit")
    print("menu.Meniu")


def run():
    grammar = Grammar("parse.txt")
    grammar.populate_grammar()
    command = "1"
    menu()
    while command != "0":
        to_print = []
        command = input(">>")
        if command == "1":
            to_print = grammar.set_non_terminal()
        elif command == "2":
            to_print = grammar.set_terminal()
        elif command == "3":
            to_print = grammar.set_production_rules()
        elif command == "4":
            terminal = input("Terminal: ")
            to_print = grammar.set_production_rules_terminal(terminal)
        elif command == "menu":
            menu()

        if command == "1" or command == "2" or command == "3" or command == "4":
            for el in to_print:
                print(el)


run()
