from z3 import *

# Definindo as variáveis booleanas
x, y, z = Bools('x y z')

# Definindo a fórmula original
formula_original = And(
    And(Or(Not(y), z), x),
    Or(Not(x), y),
    Not(Or(y, And(Not(y), x)))
)

# Criando um solver Z3
solver = Solver()

# Adicionando a fórmula ao solver
solver.add(formula_original)

# Verificando se a fórmula é satisfatível
result = solver.check()

# Interpretando o resultado
if result == sat:
    print("Fórmula original: SAT (satisfatível)")
    model = solver.model()
    print(f"x = {model[x]}, y = {model[y]}, z = {model[z]}")
else:
    print("Fórmula original: UNSAT (insatisfatível)")
