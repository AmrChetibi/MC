from AFND import FiniteAutomaton

a1 = FiniteAutomaton.readAutomaton("ejercicio2-1.txt")
a2 = FiniteAutomaton.readAutomaton("ejercicio2-2.txt")

print("AUTÓMATA que reconoce 010")
print(a1)

print("AUTÓMATA que reconoce 110")
print(a2)

# Unión (lenguaje que contiene 010 o 110)
union = a1.unionAutomaton(a2)

print("AUTÓMATA UNION (010 ∪ 110)")
print(union)
