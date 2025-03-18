from z3 import *

# Definir entradas de 8 bits
A = BitVec('A', 8)
B = BitVec('B', 8)
Cin = BitVec('Cin', 1)

# ---- CIRCUITO ORIGINAL ----
S_bits = []
carry = Cin
for i in range(8):
    Ai = Extract(i, i, A)
    Bi = Extract(i, i, B)
    Si = Ai ^ Bi ^ carry  # Soma do bit
    Cout = (Ai & Bi) | (Bi & carry) | (Ai & carry)  # Carry-out
    S_bits.append(Si)
    carry = Cout  # Atualiza carry-in para o próximo bit

Cout_original = carry  # Carry final do circuito original
S_original = Concat(*reversed(S_bits))  # Soma de 8 bits

# ---- CIRCUITO SIMPLIFICADO ----
A_ext = ZeroExt(1, A)  # Expande A para 9 bits
B_ext = ZeroExt(1, B)  # Expande B para 9 bits
Cin_ext = ZeroExt(8, Cin)  # Expande Cin para 9 bits
S_simplificado_full = A_ext + B_ext + Cin_ext  # Soma com 9 bits

S_simplificado = Extract(7, 0, S_simplificado_full)  # 8 bits de soma
Cout_simplificado = Extract(8, 8, S_simplificado_full)  # Carry final (bit 8)

# ---- Verificação de Equivalência ----
solver = Solver()
solver.add(S_original != S_simplificado)  # Soma diferente?
solver.add(Cout_original != Cout_simplificado)  # Carry diferente?

if solver.check() == sat:
    print("Os circuitos NÃO são equivalentes. Simplificação incorreta.")
else:
    print("Os circuitos são equivalentes. Simplificação válida!")
