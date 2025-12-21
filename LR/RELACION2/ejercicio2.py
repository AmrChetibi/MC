from AFND import FiniteAutomaton
from automaton_linear_grammar import grammarLinearRight

ALPHABET = ["0", "1"]

def delta(automaton, state, symbol):
    """Devuelve el único estado destino (AFD) desde state con symbol."""
    for t in automaton.getTransitionFunction():
        if t.getInitialState() == state and t.getInputSymbol() == symbol:
            return t.getFinalStates()[0]
    return None  # si falta transición

def print_transition_table(automaton):
    states = automaton.getStatesSet()
    initial = automaton.getInitialState()
    finals = set(automaton.getFinalStates())

    print("Estados:", states)
    print("Inicial:", initial)
    print("Finales:", list(finals))
    print("\nTabla de transiciones δ(q,a):")
    print(f"{'Estado':<8} {'0':<8} {'1':<8}")
    print("-" * 26)
    for s in states:
        d0 = delta(automaton, s, "0")
        d1 = delta(automaton, s, "1")
        mark = ""
        if s == initial:
            mark += "→"
        if s in finals:
            mark += "*"
        print(f"{mark+s:<8} {str(d0):<8} {str(d1):<8}")
    print()

def test_words(automaton, accepted_examples, rejected_examples):
    print("Ejemplos ACEPTADAS (según wordBelongs):")
    for w in accepted_examples:
        ok = automaton.wordBelongs(w)
        print(f"  {repr(w):>8}  -> {ok}")
    print("\nEjemplos RECHAZADAS (según wordBelongs):")
    for w in rejected_examples:
        ok = automaton.wordBelongs(w)
        print(f"  {repr(w):>8}  -> {ok}")
    print()

def save_and_print_grammar(automaton, out_path):
    """Opcional: genera gramática lineal por la derecha y la guarda."""
    G = grammarLinearRight(automaton)
    G.writeGrammar(out_path)
    print(f"Gramática guardada en: {out_path}")
    print(open(out_path, "r", encoding="utf-8").read())

def run_case(name, path, accepted_examples, rejected_examples, make_grammar=True):
    print("=" * 70)
    print(f"AFD {name}  (leído desde {path})")
    print("=" * 70)

    automaton = FiniteAutomaton.readAutomaton(path)

    print_transition_table(automaton)

    test_words(automaton, accepted_examples, rejected_examples)

    if make_grammar:
        save_and_print_grammar(automaton, f"gram_{name}.txt")

def main():

    run_case(
        "a_vacio",
        "ejercicio2a.txt",
        accepted_examples=[],
        rejected_examples=["", "0", "1", "01", "1110"],
        make_grammar=True
    )

    
    run_case(
        "b_epsilon",
        "ejercicio2b.txt",
        accepted_examples=[""],
        rejected_examples=["0", "1", "01", "10", "111"],
        make_grammar=True
    )

    
    run_case(
        "c_01",
        "ejercicio2c.txt",
        accepted_examples=["01"],
        rejected_examples=["", "0", "1", "00", "011", "101", "010"],
        make_grammar=True
    )

    
    run_case(
        "d_00_11",
        "ejercicio2d.txt",
        accepted_examples=["00", "11"],
        rejected_examples=["", "0", "1", "01", "10", "000", "111", "0011"],
        make_grammar=True
    )

    
    run_case(
        "e_01_star",
        "ejercicio2e.txt",
        accepted_examples=["", "01", "0101", "010101"],
        rejected_examples=["0", "1", "10", "001", "011", "010"],
        make_grammar=True
    )

    
    run_case(
        "f_ones_mod3",
        "ejercicio2f.txt",
        accepted_examples=["", "0", "00", "111", "10101"],
        rejected_examples=["1", "11", "101", "1111"],
        make_grammar=True
    )

if __name__ == "__main__":
    main()
