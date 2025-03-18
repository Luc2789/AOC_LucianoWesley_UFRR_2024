# Verificando a operação XOR para A = 10, B = 5
solver.push()
solver.add(A == 10, B == 5)
solver.add(xor == 15)  # 10 XOR 5 = 15
result = solver.check()
if result == sat:
    print("SAT: XOR está correto para os valores de teste.")
else:
    print("UNSAT: Há um erro na operação XOR.")
solver.pop()

# Verificando a operação NAND para A = 10, B = 5
solver.push()
solver.add(A == 10, B == 5)
solver.add(nand == 0xF5)  # 10 NAND 5 = 0xF5
result = solver.check()
if result == sat:
    print("SAT: NAND está correto para os valores de teste.")
else:
    print("UNSAT: Há um erro na operação NAND.")
solver.pop()

# Verificando a operação NOR para A = 10, B = 5
solver.push()
solver.add(A == 10, B == 5)
solver.add(nor == 0xF0)  # 10 NOR 5 = 0xF0
result = solver.check()
if result == sat:
    print("SAT: NOR está correto para os valores de teste.")
else:
    print("UNSAT: Há um erro na operação NOR.")
solver.pop()

# Verificando a operação de shift à esquerda para A = 10
solver.push()
solver.add(A == 10)
solver.add(shift_left == 40)  # 10 << 2 = 40
result = solver.check()
if result == sat:
    print("SAT: Shift à esquerda está correto para os valores de teste.")
else:
    print("UNSAT: Há um erro na operação de shift à esquerda.")
solver.pop()
