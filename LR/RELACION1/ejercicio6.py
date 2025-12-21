from AFND import FiniteAutomaton

not2 = FiniteAutomaton.readAutomaton("ejercicio6-div2.txt")
not3 = FiniteAutomaton.readAutomaton("ejercicio6-div3.txt")

print("AUTÓMATA no divisible por 2")
print(not2)

print("AUTÓMATA no divisible por 3")
print(not3)

# 2) Intersección → NO divisible por 2 Y NO divisible por 3
prod = not2.intersectionAutomaton(not3)

print("\nAFD RESULTANTE (antes de minimizar)")
print(prod)

# 3) Minimización
mini = prod.minimalAutomaton()

print("\nAFD MINIMAL")
print(mini)
