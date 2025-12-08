from grammar import GenerativeGrammar

# Leer la gramática desde fichero
g4 = GenerativeGrammar.readGrammar("ejercicio4.txt")

rules = g4.getProductionRules()
for i, r in enumerate(rules):
    print(i, ":", r)

#lineal por la izquierda
print("\n¿Es lineal por la izquierda?:", g4.linearLeft())


# Escribir la gramática en otro fichero
g4.writeGrammar("ejercicio4-1.txt")

