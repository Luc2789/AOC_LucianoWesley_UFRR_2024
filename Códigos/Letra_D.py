from z3 import *

# Definir variáveis booleanas
A, B, C, D = Bools('A B C D')

# Expressão original
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

# Imprimir a expressão
print(f"Fórmula original simplificada: {simplify(F_original)}")
