from grammar import GenerativeGrammar

g2 = GenerativeGrammar.readGrammar("ejercicio2.txt")
rules = g2.getProductionRules()

for i, r in enumerate(rules):
    print(i, ":", r)

print("\n Primera derivación de 'aaz'\n")

# S
p = g2.getInitialSymbol()   
print("Paso 0:", p)

#S -> aSA 
p= g2.applyProductionRule(p, 0, 0, rules[0])
print("Paso 1:", p)  #aSA

#S -> aSA
p = g2.applyProductionRule(p, 1, 1, rules[0])
print("Paso 2:", p)  #aaSAA

#S -> ε   
p = g2.applyProductionRule(p, 2, 2, rules[1])
print("Paso 3:", p) # aaAA

# Ahora tenemos aaAA 

#primer A -> z en la posición 2
s = g2.applyProductionRule(p, 2, 2, rules[3])
print("Paso 4:", s) # aazA

#segundo A -> ε en la posición 3
s = g2.applyProductionRule(s, 3, 3, rules[4])
print("Paso 5 (final):", s) #aaz


print("\nSegunfa derivación de 'aaz'\n")

#Hago lo mismo hasta llegar a 'aaAA'
p = g2.getInitialSymbol()
print("Paso 0:", p)
p = g2.applyProductionRule(p, 0, 0, rules[0])  # S -> aSA
print("Paso 1:", p)         # aSA
p = g2.applyProductionRule(p, 1, 1, rules[0])  # S -> aSA
print("Paso 2:", p)         # aaSAA
p = g2.applyProductionRule(p, 2, 2, rules[1])  # S -> ε
print("Paso 3:", p)         # aaAA

#primer A -> ε en la posición 2
s = g2.applyProductionRule(p, 2, 2, rules[4])
print("Paso 4:", s)        # aaA

#ahora el único A -> z en la posición 2
s = g2.applyProductionRule(s, 2, 2, rules[3])
print("Paso 5 (final):", s)  #aaz
