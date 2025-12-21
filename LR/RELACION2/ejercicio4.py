# ejercicio4.py
from grammar import GenerativeGrammar
from automaton_linear_grammar import computeAssociatedAFNDLinearRight

def print_afd_diagram_text(automaton):
    states = automaton.getStatesSet()
    alphabet = automaton.getAlphabetSymbols()
    initial = automaton.getInitialState()
    finals = set(automaton.getFinalStates())
    transitions = automaton.getTransitionFunction()

    print("Q =", states)
    print("Σ =", alphabet)
    print("q0 =", initial)
    print("F =", finals)
    print("\nTabla de transiciones δ:")

    print(f"{'Estado':<25} {'0':<15} {'1':<15}")
    print("-" * 55)

    for s in states:
        shown = s
        if s == initial:
            shown = "→" + shown
        if s in finals:
            shown = "*" + shown

        dest = {"0": "-", "1": "-"}
        for t in transitions:
            if t.getInitialState() == s and t.getInputSymbol() in ("0", "1"):
                dest[t.getInputSymbol()] = t.getFinalStates()[0]

        print(f"{shown:<25} {dest['0']:<15} {dest['1']:<15}")

def test_words(automaton, accepted, rejected):
    print("\nCadenas ACEPTADAS:")
    for w in accepted:
        print(f"  {repr(w):<10} -> {automaton.wordBelongs(w)}")

    print("\nCadenas RECHAZADAS:")
    for w in rejected:
        print(f"  {repr(w):<10} -> {automaton.wordBelongs(w)}")

def main():
    # 1) Leer gramática equivalente (lineal por la derecha)
    G = GenerativeGrammar.readGrammar("ejercicio4.txt")

    # 2) Gramática -> AFND (ε)
    afnd = computeAssociatedAFNDLinearRight(G)
    if afnd is None:
        print("La gramática no es lineal por la derecha.")
        return

    # 3) AFND -> AFD
    afd = afnd.transformDeterministic()

    # 4) Mostrar “diagrama” en texto (tabla δ)
    print("\n=== AFD obtenido ===\n")
    print_afd_diagram_text(afd)

    # 5) Ejemplos: lenguaje 0(10)^*
    accepted = ["0", "010", "01010", "0101010"]
    rejected = ["", "1", "10", "00", "0101", "1010", "0110"]

    test_words(afd, accepted, rejected)

if __name__ == "__main__":
    main()
