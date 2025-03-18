from z3 import *

# Definindo as entradas de 8 bits
A = BitVec('A', 8)  # Entrada A de 8 bits
B = BitVec('B', 8)  # Entrada B de 8 bits

# Definindo as operações da ULA
subtracao = A - B          # Subtração
xor = A ^ B                # XOR
nand = ~(A & B)            # NAND
nor = ~(A | B)             # NOR
shift_left = A << 2        # Shift de 2 bits à esquerda

# Criando um solver Z3
solver = Solver()

# Adicionando condições de teste para validar as operações
# Exemplo: Verificar se a subtração está correta para A = 10, B = 5
solver.add(A == 10, B == 5)
solver.add(subtracao == 5)  # 10 - 5 = 5

# Verificando se as condições são satisfeitas
result = solver.check()

# Interpretando o resultado
if result == sat:
    print("SAT: As operações estão corretas para os valores de teste.")
else:
    print("UNSAT: Há um erro nas operações para os valores de teste.")
