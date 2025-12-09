from AFND import FiniteAutomaton

path_file = "ejercicio3.txt"
automata= FiniteAutomaton.readAutomaton(path_file)

print("AUTÓMATA ORIGINAL")
print(automata)

# Obtener el autómata determinista minimal
minimal_automata = automata.minimalAutomaton()

print("\nAUTÓMATA MINIMAL")
print(minimal_automata)
