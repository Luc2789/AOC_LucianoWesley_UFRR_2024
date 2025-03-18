
from z3 import *

# verificando as saidas
S0, S1, S2, S3 = Bools('S0 S1 S2 S3')
# Definição da saída esperada (exemplo)
F = Or(And(S0, S1), And(S1, Not(S2)), And(S2, S3), And(Not(S0), S3))
    
solver = Solver()
solver.add(Not(F))  # Testar se F pode ser falso
solver.add(S0 == True, S1 == True, S2 == False, S3 == True)
    
if solver.check() == sat:
  print("A especificação falhou.")
else:
  print("A especificação foi atendida.")

# Verificação de Equivalência com Z3
# a formula completa do circuito: original​=((A∧B)∨C)∨C
# a formula simplificada do circuito: simplificado​=(A∧B)∨C
A, B, C = Bools('A B C')


original = Or(And(A, B), C, C)
simplificado = Or(And(A, B), C)


solver3 = Solver()


solver3.add(original != simplificado)

resultado = solver3.check()

print(resultado)

if resultado == sat:
    print("SAT: Há entradas que diferenciam os circuitos. A redundância não pode ser removida.")
else:
    print("UNSAT: Os circuitos são equivalentes para todas as entradas. A redundância pode ser eliminada.")
