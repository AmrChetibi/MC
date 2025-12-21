from AFND import FiniteAutomaton

L1 = FiniteAutomaton.readAutomaton("ejercicio9-L1.txt")
L2 = FiniteAutomaton.readAutomaton("ejercicio9-L2.txt")


# Complementarios
L1c = L1.complementaryAutomaton()
L2c = L2.complementaryAutomaton()


# L1 \ L2 = L1 ∩ ¬L2
L1_minus_L2 = L1.intersectionAutomaton(L2c)

# L2 \ L1 = L2 ∩ ¬L1
L2_minus_L1 = L2.intersectionAutomaton(L1c)

# (L1 \ L2) ∪ (L2 \ L1)
symdiff = L1_minus_L2.unionAutomaton(L2_minus_L1)


# Minimización final
symdiff_min = symdiff.minimalAutomaton()
print("\nAUTÓMATA MINIMAL PARA (L1 \\ L2) ∪ (L2 \\ L1)")
print(symdiff_min)


#L₁ y L₂ representan el mismo lenguaje