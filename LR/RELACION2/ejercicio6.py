# ejercicio6.py
from AFND_nullable import FiniteAutomatonNullable

def print_automaton(automaton, title):
    print(f"\n=== {title} ===\n")
    print("Q =", automaton.getStatesSet())
    print("Σ =", automaton.getAlphabetSymbols())
    print("q0 =", automaton.getInitialState())
    print("F =", automaton.getFinalStates())
    print("\nTransiciones:")

    for t in automaton.getTransitionFunction():
        a = t.getInputSymbol()
        label = "ε" if a == "" else a
        for q in t.getFinalStates():
            print(f"  δ({t.getInitialState()}, {label}) -> {q}")

def test_words(automaton, accepted, rejected):
    print("\nCadenas ACEPTADAS:")
    for w in accepted:
        print(f"  {repr(w):<8} -> {automaton.wordBelongs(w)}")

    print("\nCadenas RECHAZADAS:")
    for w in rejected:
        print(f"  {repr(w):<8} -> {automaton.wordBelongs(w)}")

def main():

    afnd = FiniteAutomatonNullable.readAutomaton("ejercicio6.txt")

    print_automaton(afnd, "AFND con ε")

    afd = afnd.transformDeterministic()

    print_automaton(afd, "AFD equivalente")

    accepted = [
        "",
        "a",
        "b",
        "bb",
        "bbb",
        "ab",
        "abb",
        "abbb"
    ]

    rejected = [
        "aa",
        "ba",
        "aba",
        "bab",
        "aab"
    ]

    test_words(afd, accepted, rejected)

if __name__ == "__main__":
    main()
