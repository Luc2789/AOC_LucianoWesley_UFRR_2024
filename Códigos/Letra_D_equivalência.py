from z3 import *

# Definir variáveis booleanas
A, B, C, D = Bools('A B C D')

# ---- Fórmula original ----
F_original = Or(
    And(A, B, C, D),
    And(A, B, Not(C), D),
    And(A, B, Not(C), Not(D)),
    And(A, Not(B), C, D),
    And(Not(A), B, C, D),
    And(Not(A), B, C, Not(D)),
    And(Not(A), B, Not(C), D),
    And(Not(A), Not(B), Not(C), D)
)

# ---- Fórmula simplificada ----
F_simplificado = Or(
    And(A, Or(D, Not(C))),
    And(Not(A), B, C),
    And(Not(A), Not(B), Not(C), D)
)

# ---- Verificação de Equivalência ----
solver = Solver()
solver.add(F_original != F_simplificado)  # Verifica se as expressões são diferentes

# Resultado da verificação
if solver.check() == sat:
    print("Os circuitos NÃO são equivalentes. Simplificação incorreta.")
else:
    print("Os circuitos são equivalentes. Simplificação válida!")
