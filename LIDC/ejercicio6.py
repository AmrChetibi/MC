from grammar import GenerativeGrammar 
g6 = GenerativeGrammar.readGrammar("ejercicio6.txt") 

#Eliminar producciones inutiles 
g6.deleteUselessSymbolsProductions(True) 
g6.writeGrammar("ejercicio6_sin_inutiles.txt") 

g7 = GenerativeGrammar.readGrammar("ejercicio6_sin_inutiles.txt") 

#Eliminar producciones unitarias 

g7.deleteUnitaryProductions(True)
#Escribir la gramática resultante en otro fichero 

g7.writeGrammar("ejercicio6_sin_unitarias.txt") 

#El problema de esta gramática es que nunca vamos a poder llegar a una palabra formada solo por terminales.
#Por ejemplo, si empezamos con S, la única regla que podemos aplicar es S -> ABaC, y luego A -> AB, y así sucesivamente.
#Nunca podremos eliminar A ya que no podemos llegar a un símbolo terminal a partir de A.
#He intentado aplicar antes la regla de eliminar producciones inútiles, pero el resultado es S -> 