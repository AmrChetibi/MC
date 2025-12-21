# ejercicio7.py
from AFND import FiniteAutomaton
from AFD_to_reg import dfaToRegex


def print_afd_diagram_text(automaton):
    states = automaton.getStatesSet()
    alphabet = automaton.getAlphabetSymbols()
    initial = automaton.getInitialState()
    finals = automaton.getFinalStates()
    transitions = automaton.getTransitionFunction()

    print("Q =", states)
    print("Σ =", alphabet)
    print("q0 =", initial)
    print("F =", finals)
    print("\nTabla de transiciones δ:")

    print(f"{'Estado':<10} {'0':<10} {'1':<10}")
    print("-" * 30)

    for s in states:
        shown = s
        if s == initial:
            shown = "→" + shown
        if s in finals:
            shown = "*" + shown

        d0 = d1 = "-"
        for t in transitions:
            if t.getInitialState() == s:
                if t.getInputSymbol() == "0":
                    d0 = t.getFinalStates()[0]
                elif t.getInputSymbol() == "1":
                    d1 = t.getFinalStates()[0]

        print(f"{shown:<10} {d0:<10} {d1:<10}")


def main():
    afd = FiniteAutomaton.readAutomaton("ejercicio7.txt")
    print("\n=== Expresión regular equivalente ===\n")
    regex = dfaToRegex(afd)
    print(regex)

if __name__ == "__main__":
    main()
