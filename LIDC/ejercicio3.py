from grammar import GenerativeGrammar

g3 = GenerativeGrammar.readGrammar("ejercicio3.txt")
rules = g3.getProductionRules()

for i, r in enumerate(rules):
    print(i, ":", r)

#APARTADO A Y B

print("\n Primera derivación de 'aaaaaa'\n")

p = g3.getInitialSymbol() #S
print("Paso 0:", p)

#S -> A   
p = g3.applyProductionRule(p, 0, 0, rules[0])
print("Paso 1:", p) #A

#A -> aaA  
p = g3.applyProductionRule(p, 0, 0, rules[2])
print("Paso 2:", p) #aaA

#A -> aaA 
p = g3.applyProductionRule(p, 2, 2, rules[2])
print("Paso 3:", p) #aaaaA

#A -> aaA  
p = g3.applyProductionRule(p, 4, 4, rules[2])
print("Paso 4:", p) #aaaaaaA

#A -> ε    
p = g3.applyProductionRule(p, 6, 6, rules[3])
print("Paso 5 (final):", p) #aaaaaa

print("\nSegunda derivación de 'aaaaaa'\n")

s = g3.getInitialSymbol()
print("Paso 0:", s)

#S -> B   
s = g3.applyProductionRule(s, 0, 0, rules[1])
print("Paso 1:", s)        # B

#B -> aaaB sobre la B en pos 0
s = g3.applyProductionRule(s, 0, 0, rules[4])
print("Paso 2:", s)        # aaaB

#B -> aaaB otra vez sobre la B en pos 3
s = g3.applyProductionRule(s, 3, 3, rules[4])
print("Paso 3:", s)        # aaaaaaB

#B -> ε sobre la B en pos 6
s = g3.applyProductionRule(s, 6, 6, rules[5])
print("Paso 4 (final):", s) # aaaaaa


#APARTADO C Y D

print("\n=============================================\n")
print("GRAMÁTICA NO AMBIGUA\n")

g4 = GenerativeGrammar.readGrammar("ejercicio3_linealizq.txt")

rules_new = g4.getProductionRules()
for i, r in enumerate(rules_new):
    print(i, ":", r)

print("\n¿Es lineal por la izquierda?:", g4.linearLeft())