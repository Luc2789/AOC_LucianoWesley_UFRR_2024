from z3 import *

# Definir os bits de entrada
A = BitVec('A', 8)  # Primeiro operando (8 bits)
B = BitVec('B', 8)  # Segundo operando (8 bits)
Cin = BitVec('Cin', 1)  # Carry-in (1 bit)

# Criar a soma bit a bit e calcular os carrys
S_bits = []  # Lista para armazenar os bits da soma
carry = Cin  # Começa com carry-in

for i in range(8):
    Ai = Extract(i, i, A)  # Bit i de A
    Bi = Extract(i, i, B)  # Bit i de B
    Si = Ai ^ Bi ^ carry  # Soma do bit
    Cout = (Ai & Bi) | (Bi & carry) | (Ai & carry)  # Carry-out

    S_bits.append(Si)  # Adiciona o bit da soma
    carry = Cout  # Carry-out se torna Carry-in para o próximo bit

Cout_final = carry  # Carry final
S = Concat(*reversed(S_bits))  # Concatena todos os bits para formar a soma de 8 bits

# Criar o solver e testar uma soma específica
solver = Solver()
solver.add(A == 0b11001100, B == 0b10101010, Cin == 1)

# Executar e exibir resultados
if solver.check() == sat:
    model = solver.model()
    soma_resultado = model.eval(S).as_long()
    carry_resultado = model.eval(Cout_final).as_long()
    print(f"Soma (S): {bin(soma_resultado)}")
    print(f"Carry final (Cout): {carry_resultado}")
else:
    print("Erro na verificação.")
