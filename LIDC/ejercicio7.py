from grammar import GenerativeGrammar

g7 = GenerativeGrammar.readGrammar("ejercicio7.txt")

#Eliminar símbolos y producciones inútiles
print("\nELIMINANDO SÍMBOLOS Y PRODUCCIONES INÚTILES\n")
g7.deleteUselessSymbolsProductions(True)
g7.writeGrammar("ejercicio7_sin_inutiles.txt")

#Eliminar producciones nulas y unitarias
g7_clean = GenerativeGrammar.readGrammar("ejercicio7_sin_inutiles.txt")

print("\nELIMINANDO PRODUCCIONES NULAS\n")
g7_clean.deleteNullProductions(True)
g7_clean.writeGrammar("ejercicio7_sin_nulas.txt")

print("\nELIMINANDO PRODUCCIONES UNITARIAS\n")
g7_clean.deleteUnitaryProductions(True)
g7_clean.writeGrammar("ejercicio7_sin_nulas_unitarias.txt")

#Pasar la gramática a Forma Normal de Chomsky
print("\nFORMA NORMAL DE CHOMSKY\n")
g7_chomsky = GenerativeGrammar.readGrammar("ejercicio7_sin_nulas_unitarias.txt")
g7_chomsky.transformChomsky(True)
g7_chomsky.writeGrammar("ejercicio7_Chomsky.txt")
