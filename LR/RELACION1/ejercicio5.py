from AFND import FiniteAutomaton

print("=== EJERCICIO 5: L1 \\ L2 ===")

# 1) Leer autómatas que reconocen L1 y L2
L1 = FiniteAutomaton.readAutomaton("ejercicio5-L1.txt")
L2 = FiniteAutomaton.readAutomaton("ejercicio5-L2.txt")

print("\nAUTÓMATA L1  = (01 + 1)*00")
print(L1)

print("\nAUTÓMATA L2  = 01(01 + 1)*")
print(L2)

# 2) Complemento de L2
L2_comp = L2.complementaryAutomaton()
print("\nAUTÓMATA COMPLEMENTARIO DE L2 (¬L2)")
print(L2_comp)

# 3) Diferencia L1 \\ L2 = L1 ∩ ¬L2
L1_minus_L2 = L1.intersectionAutomaton(L2_comp)
print("\nAUTÓMATA PARA L1 \\ L2 (antes de minimizar)")
print(L1_minus_L2)

# 4) Minimización
L1_minus_L2_min = L1_minus_L2.minimalAutomaton()
print("\nAUTÓMATA MINIMAL PARA L1 \\ L2")
print(L1_minus_L2_min)
