from grammar import GenerativeGrammar

# 1) Leer la gramática desde fichero
path_1 = "ejercicio1.txt"
g1 = GenerativeGrammar.readGrammar(path_1)

# 2) Mirar las reglas y sus índices
rules = g1.getProductionRules()
for i, r in enumerate(rules):
    print(i, ":", r)

# 3) Derivación paso a paso:
# Sustituye los índices rule_i por los que correspondan en tu impresión.
word = g1.getInitialSymbol()
print("Paso 0:", word)

# Ejemplo de esquema (tú ajustas índices y posiciones):
# Supongamos que la regla S -> 0A0 es rules[idx_S_0A0], etc.
# word = g1.applyProductionRule(word, pos_inicio, pos_fin, rules[idx])
# print("Paso k:", word)

# Cuando consigas llegar a "00111100", ya tienes la cadena de derivación.

revisar