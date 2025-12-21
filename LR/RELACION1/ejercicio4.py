from AFND import FiniteAutomaton

# Leer autómatas base
ases = FiniteAutomaton.readAutomaton("ejercicio4-as.txt")
mod3   = FiniteAutomaton.readAutomaton("ejercicio4-mult3.txt")
abc    = FiniteAutomaton.readAutomaton("ejercicio4-cont.txt")

#NO contiene 'abc'
comp_abc = abc.complementaryAutomaton()

print("AFD paridad de 'a'")
print(ases)
print("AFD longitud múltiplo de 3")
print(mod3)
print("AFD NO contiene 'abc'")
print(comp_abc)

# Intersección
ab = ases.productAutomaton(mod3, "intersection")

print("\nAFD (a ∧ b)")
print(ab)

# Intersección final
abc_all = ab.productAutomaton(comp_abc, "intersection")

print("\nAFD (a ∧ b ∧ c)")
print(abc_all)


minimal = abc_all.minimalAutomaton()
print("\nAFD MINIMAL")
print(minimal)
