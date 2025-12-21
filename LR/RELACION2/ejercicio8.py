# ejercicio8.py
from AFND import FiniteAutomaton
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

    # asumimos alfabeto {a,b}
    print(f"{'Estado':<8} {'a':<8} {'b':<8}")
    print("-" * 26)
    for s in states:
        shown = s
        if s == initial:
            shown = "→" + shown
        if s in finals:
            shown = "*" + shown
        print(f"{shown:<8} {delta(s,'a'):<8} {delta(s,'b'):<8}")

def test_words(automaton):
    accepted = ["", "b", "bbabbb", "aaaa", "abbb", "aabbaa", "abba", "baaaab"]
    rejected = ["aba", "ababa", "aaba", "baba", "x"]  # 'x' no está en el alfabeto (debe rechazar)

    print("\nEjemplos ACEPTADAS:")
    for w in accepted:
        print(f"  {repr(w):<10} -> {automaton.wordBelongs(w)}")

    print("\nEjemplos RECHAZADAS:")
    for w in rejected:
        print(f"  {repr(w):<10} -> {automaton.wordBelongs(w)}")

def main():
    afd = FiniteAutomaton.readAutomaton("ejercicio8.txt")

    print("\n=== AFD que NO contiene 'aba' ===\n")
    print_afd_table(afd)

    test_words(afd)

    print("\n=== Expresión regular equivalente (por eliminación de estados) ===\n")
    regex = dfaToRegex(afd)
    print(regex)

if __name__ == "__main__":
    main()
