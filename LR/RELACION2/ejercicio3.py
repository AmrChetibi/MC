# ejercicio3.py
from grammar import GenerativeGrammar
from automaton_linear_grammar import computeAssociatedAFNDLinearRight

def print_automaton_diagram_text(automaton):
    states = automaton.getStatesSet()
    alphabet = automaton.getAlphabetSymbols()
    initial = automaton.getInitialState()
    finals = automaton.getFinalStates()
    transitions = automaton.getTransitionFunction()

    print("Q =", states)
    print("A =", alphabet)
    print("q0 =", initial)
    print("F =", finals)
    print("\nTransiciones (incluye ε como símbolo vacío):")

    grouped = {}
    for t in transitions:
        p = t.getInitialState()
        a = t.getInputSymbol()      
        for q in t.getFinalStates():
            grouped.setdefault((p, a), [])
            if q not in grouped[(p, a)]:
                grouped[(p, a)].append(q)

    def sym_key(a):
        return (-1 if a == "" else 0, a)

    for (p, a) in sorted(grouped.keys(), key=lambda x: (x[0], sym_key(x[1]))):
        label = "ε" if a == "" else a
        dests = ",".join(grouped[(p, a)])
        print(f"  δ({p}, {label}) -> {{{dests}}}")

def main():
    G = GenerativeGrammar.readGrammar("ejercicio3.txt")

    M = computeAssociatedAFNDLinearRight(G)

    print_automaton_diagram_text(M)

if __name__ == "__main__":
    main()
