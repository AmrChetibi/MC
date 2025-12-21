# ejercicio9.py
from AFND import FiniteAutomaton
from automaton_linear_grammar import (
    grammarLinearRight,
    grammarLinearLeft
)
from AFD_to_reg import dfaToRegex


def print_afd_table(automaton):
    states = automaton.getStatesSet()
    alphabet = automaton.getAlphabetSymbols()
    initial = automaton.getInitialState()
    finals = set(automaton.getFinalStates())
    transitions = automaton.getTransitionFunction()

    def delta(s, a):
        for t in transitions:
            if t.getInitialState() == s and t.getInputSymbol() == a:
                return t.getFinalStates()[0]
        return "-"

    print("Q =", states)
    print("Σ =", alphabet)
    print("q0 =", initial)
    print("F =", list(finals))
    print("\nTabla de transiciones δ:")
    print(f"{'Estado':<8} {'0':<8} {'1':<8}")
    print("-" * 26)

    for s in states:
        shown = s
        if s == initial:
            shown = "→" + shown
        if s in finals:
            shown = "*" + shown
        print(f"{shown:<8} {delta(s,'0'):<8} {delta(s,'1'):<8}")


def print_grammar(title, grammar):
    print(f"\n=== {title} ===\n")
    grammar.writeGrammar("_tmp.txt")
    print(open("_tmp.txt").read())


def main():
    # 1) Leer AFD
    afd = FiniteAutomaton.readAutomaton("ejercicio9.txt")

    print("\n=== AFD (termina en 110) ===\n")
    print_afd_table(afd)

    # 2) Gramática lineal por la derecha
    G_right = grammarLinearRight(afd)
    print_grammar("Gramática lineal por la DERECHA", G_right)

    # 3) Gramática lineal por la izquierda
    G_left = grammarLinearLeft(afd)
    print_grammar("Gramática lineal por la IZQUIERDA", G_left)

    # 4) Expresión regular
    print("\n=== Expresión regular equivalente ===\n")
    regex = dfaToRegex(afd)
    print(regex)


if __name__ == "__main__":
    main()
