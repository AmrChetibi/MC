# ejercicio5.py
from AFND_nullable import FiniteAutomatonNullable
from AFND import FiniteAutomaton

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
        print(f"  {repr(w):<10} -> {automaton.wordBelongs(w)}")

    print("\nCadenas RECHAZADAS:")
    for w in rejected:
        print(f"  {repr(w):<10} -> {automaton.wordBelongs(w)}")

def main():
    afnd = FiniteAutomatonNullable.readAutomaton("ejercicio5.txt")

    print_automaton(afnd, "AFND con ε")

    afd = afnd.transformDeterministic()

    print_automaton(afd, "AFD equivalente")

   
    accepted = [
        "011",
        "010",
        "10110",
        "0001011",
        "11010",
        "00101100",
        "001100",   
        "10101"     
    ]

    rejected = [
        "",
        "0",
        "1",
        "00",
        "111",
        "1100",      
    ]

    test_words(afd, accepted, rejected)

if __name__ == "__main__":
    main()
