# f = ((~y+z)*x)*(~x+y)*~(y+(~y*x))

from z3 import*

# definição das variaveis 

y, z, x = Bools('y z x')

#Expressão booleana do circuito

F = And(And(And(Or(Not(y),z), x), Or(Not(x),y)), Not(Or(y, And(Not(y),x))))

# Solver para verificar a especificação
solver = Solver()

solver.add(F)
solver.add(y == True, x == True, z == False)

# resultado da verificação
if solver.check() == sat:
    print("A especificação falhou.")
else:
    print("A especificação foi atendida.")
