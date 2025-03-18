from z3 import *

# Definindo as variáveis booleanas
x, y, z = Bools('x y z')

# Fórmula original
formula_original = And(
    And(Or(Not(y), z), x),
    Or(Not(x), y),
    Not(Or(y, And(Not(y), x)))
)

# Fórmula simplificada
formula_simplificada = BoolVal(False)  # Fórmula simplificada é False

# Criando um solver Z3
solver = Solver()

# Verificando se as fórmulas são equivalentes
solver.add(formula_original != formula_simplificada)
result = solver.check()

# Interpretando o resultado
if result == sat:
    print("As fórmulas NÃO são equivalentes.")
else:
    print("As fórmulas são equivalentes.")
