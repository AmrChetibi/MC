from AFND import FiniteAutomaton

# Leer autómatas
L1 = FiniteAutomaton.readAutomaton("ejercicio8-L1.txt")
L2 = FiniteAutomaton.readAutomaton("ejercicio8-L2.txt")

# Complementario de L2
L2c = L2.complementaryAutomaton()

# Intersección: L1 ∩ ¬L2
diff = L1.intersectionAutomaton(L2c)

# Minimización
mini = diff.minimalAutomaton()
print("\nAFD MINIMAL PARA L1 \\ L2")
print(mini)
