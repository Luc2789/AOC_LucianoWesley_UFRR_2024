# Expressão original
original_xor = A ^ B

# Expressão simplificada (hipotética)
simplified_xor = (A | B) & ~(A & B)

# Verificando se as expressões são equivalentes
solver = Solver()
solver.add(original_xor != simplified_xor)
result = solver.check()

if result == sat:
    print("SAT: As expressões não são equivalentes. A simplificação não é válida.")
else:
    print("UNSAT: As expressões são equivalentes. A simplificação é válida.")
