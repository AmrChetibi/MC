from grammar import GenerativeGrammar

# 1) Leer la gramática original desde fichero
g5 = GenerativeGrammar.readGrammar("ejercicio5.txt")

original_rules = g5.getProductionRules()
for i, r in enumerate(original_rules):
    print(i, ":", r)

# 2) Eliminar símbolos y producciones inútiles
g5.deleteUselessSymbolsProductions(True)   # True para que muestre los pasos

print("\n=== REGLAS DESPUÉS DE ELIMINAR SÍMBOLOS INÚTILES ===\n")
rules_after = g5.getProductionRules()
for i, r in enumerate(rules_after):
    print(i, ":", r)

# 3) Escribir la gramática resultante en otro fichero
g5.writeGrammar("ejercicio5-inutilesout.txt")