from AFND import FiniteAutomaton
from automaton_linear_grammar import grammarLinearRight

# 1) Leer el autómata desde fichero
M = FiniteAutomaton.readAutomaton("ejercicio1.txt")  # :contentReference[oaicite:3]{index=3}

# 2) Pasar a gramática lineal por la derecha
G = grammarLinearRight(M)  # :contentReference[oaicite:4]{index=4}

# 3) Guardar la gramática en fichero (y así la “muestras” en el entregable)
G.writeGrammar("gramatica_ej1.txt")  # :contentReference[oaicite:5]{index=5}

# 4) Si quieres “mostrarla” por consola:
print(open("gramatica_ej1.txt", "r", encoding="utf-8").read())
