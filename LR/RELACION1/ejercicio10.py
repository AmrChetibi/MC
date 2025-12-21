from AFND import FiniteAutomaton

# Leer los dos autómatas del ejercicio 10
print("Leyendo A1...")
A1 = FiniteAutomaton.readAutomaton("ejercicio10-A1.txt")
print("A1 leído.\n")

print("Leyendo A2...")
A2 = FiniteAutomaton.readAutomaton("ejercicio10-A2.txt")
print("A2 leído.\n")

print("AUTÓMATA 1")
print(A1)
print("\nAUTÓMATA 2")
print(A2)

# Complementarios
print("\nCalculando complementario de A1...")
A1c = A1.complementaryAutomaton()
print("Complementario de A1 listo.")

print("Calculando complementario de A2...")
A2c = A2.complementaryAutomaton()
print("Complementario de A2 listo.")

# Diferencias:
print("\nCalculando A1 \\ A2...")
A1_minus_A2 = A1.intersectionAutomaton(A2c)
print("A1 \\ A2 calculado.")

print("Calculando A2 \\ A1...")
A2_minus_A1 = A2.intersectionAutomaton(A1c)
print("A2 \\ A1 calculado.")

# Diferencia simétrica:
print("\nCalculando unión de las diferencias (diferencia simétrica)...")
symdiff = A1_minus_A2.unionAutomaton(A2_minus_A1)
print("Unión calculada.")

# Minimizar
print("\nMinimizando la diferencia simétrica...")
symdiff_min = symdiff.minimalAutomaton()
print("Minimización terminada.")

print("\nAUTÓMATA MINIMAL DE LA DIFERENCIA SIMÉTRICA")
print(symdiff_min)

# Comprobación rápida: ¿tiene estados finales?
try:
    finals = symdiff_min.final_states_set
except AttributeError:
    finals = []

print("\nEstados finales del autómata de la diferencia simétrica:")
print(finals)

if len(finals) == 0:
    print("\n➡ Conclusión: L(A1) y L(A2) ACEPTAN EL MISMO LENGUAJE.")
else:
    print("\n➡ Conclusión: L(A1) y L(A2) NO aceptan el mismo lenguaje.")
