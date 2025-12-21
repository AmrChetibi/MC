# ejercicio10.py
from AFND import FiniteAutomaton
from grammar import GenerativeGrammar
from production_rule import ProductionRule

def print_afd_table(automaton):
    states = automaton.getStatesSet()
    initial = automaton.getInitialState()
    finals = set(automaton.getFinalStates())
    transitions = automaton.getTransitionFunction()

    def delta(s, a):
        for t in transitions:
            if t.getInitialState() == s and t.getInputSymbol() == a:
                return t.getFinalStates()[0]
        return "-"

    print("Q =", states)
    print("Σ =", automaton.getAlphabetSymbols())
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

def grammarLinearLeft_general(automaton):
    # Variables = estados + S
    states = automaton.getStatesSet()
    V = states + ["S"] if "S" not in states else states + ["S0"]
    Ssym = "S" if "S" in V else "S0"

    T = automaton.getAlphabetSymbols()
    q0 = automaton.getInitialState()
    finals = automaton.getFinalStates()
    trans = automaton.getTransitionFunction()

    P = []

    # Para cada transición δ(p,a)=q, añadir q -> p a
    for t in trans:
        p = t.getInitialState()
        a = t.getInputSymbol()
        q = t.getFinalStates()[0]
        P.append(ProductionRule(q, [p, a]))

    # Para cada final f, añadir S -> f
    for f in finals:
        P.append(ProductionRule(Ssym, [f]))

    # Para el inicial, añadir q0 -> ε
    P.append(ProductionRule(q0, [""]))

    return GenerativeGrammar(V, T, Ssym, P)

def print_grammar(grammar):
    grammar.writeGrammar("_tmp_ej10.txt")
    # convertir el '|' final (ε vacío) en 'ε' SOLO para imprimir bonito
    lines = open("_tmp_ej10.txt", encoding="utf-8").read().splitlines()
    pretty = []
    for line in lines:
        if "->" in line and line.strip().endswith("|"):
            pretty.append(line + "ε")
        else:
            pretty.append(line)
    print("\n".join(pretty))

def main():
    afd = FiniteAutomaton.readAutomaton("ejercicio10.txt")

    print("\n=== AFD que NO contiene '001' ===\n")
    print_afd_table(afd)

    print("\n=== Gramática lineal por la IZQUIERDA (equivalente) ===\n")
    G_left = grammarLinearLeft_general(afd)
    print_grammar(G_left)

if __name__ == "__main__":
    main()
