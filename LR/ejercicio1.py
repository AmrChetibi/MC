from AFND import FiniteAutomaton

# 1) Leemos el autómata que acepta "contiene abc"
path_file = "ejercicio1.txt"
automaton_abc = FiniteAutomaton.readAutomaton(path_file)

# 2) Obtenemos el autómata complementario:
#    acepta las cadenas que NO contienen la subcadena "abc"
automaton_comp_abc = automaton_abc.complementaryAutomaton()

# 3) Lo mostramos por pantalla (como en el PDF)
print(automaton_comp_abc)
