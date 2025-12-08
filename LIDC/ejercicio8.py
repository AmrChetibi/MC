from grammar import GenerativeGrammar

# 1) Leer la gramática desde fichero
g8 = GenerativeGrammar.readGrammar("ejercicio8.txt")

print("GRAMÁTICA INICIAL\n")
print(g8)

# 2) Comprobar si se puede aplicar Greibach
print("\n¿SE PUEDE APLICAR GREIBACH?\n")
appliable = g8.greibachAppliable(True)
print("\nResultado greibachAppliable:", appliable)

# 3) Si se puede, transformarla a Forma Normal de Greibach
if appliable:
    print("\n=== TRANSFORMANDO A FORMA NORMAL DE GREIBACH ===\n")
    g8.transformGreibach(True)

    # 4) Escribir la gramática resultante en un fichero
    g8.writeGrammar("ejercicio8_Greibach.txt")
    print("\nGramática en Forma Normal de Greibach escrita en 'ejercicio8_Greibach.txt'")
else:
    print("\nNo se puede aplicar Greibach a esta gramática según greibachAppliable().")
