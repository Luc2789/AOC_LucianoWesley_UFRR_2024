
#  FLUXO DE EXECUÇÃO DE UMA INSTRUÇÃO DO TIPO R NO MIPS DE 32BITS




## Fórmula Booleana Completa

- F = (pc_update ∧ mem_read_instr) ∧ (instr_decode ∧ reg_read_1 ∧ reg_read_2) ∧ (alu_control ∧ alu_execute) ∧ reg_write

## Fórmula Booleana Simplificada

- F = pc_update ∧ mem_read_instr ∧ instr_decode ∧ reg_read_1 ∧ reg_read_2 ∧ alu_control ∧ alu_execute ∧ reg_write

