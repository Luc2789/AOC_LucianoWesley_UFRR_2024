from z3 import *

# Definição das variáveis booleanas para os sinais de controle do pipeline
IF, ID, EX, MEM, WB = Bools('IF ID EX MEM WB')

# Modelagem do fluxo de execução de uma instrução do tipo R no MIPS de 32 bits
# Passos do pipeline: IF -> ID -> EX -> WB
fluxo_execucao = And(IF, ID, EX, WB)

# Solver para verificar a validade do fluxo de execução
solver = Solver()
solver.add(fluxo_execucao)

print("Fluxo de execução da instrução do tipo R no MIPS:")
print(fluxo_execucao)

print("\nValidação do fluxo de execução:")
if solver.check() == sat:
    print("O fluxo de execução está correto.")
else:
    print("Erro no fluxo de execução.")
