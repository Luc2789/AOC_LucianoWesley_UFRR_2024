# ULA
## Formula Boolenas

| Operação       | Fórmula Booleana Completa                          | Fórmula Booleana Simplificada                  |
|----------------|---------------------------------------------------|-----------------------------------------------|
| **Subtração**  | \( A + (\sim B + 1) \)                            | \( A - B \) (implementação direta em hardware) |
| **XOR**        | \( (A_i \land \neg B_i) \lor (\neg A_i \land B_i) \) | \( A_i \oplus B_i \) (já simplificado)         |
| **NAND**       | \( \neg (A_i \land B_i) \)                        | \( \neg (A_i \land B_i) \) (já simplificado)   |
| **NOR**        | \( \neg (A_i \lor B_i) \)                         | \( \neg (A_i \lor B_i) \) (já simplificado)    |
| **Shift Left** | \( A_{i-2} \) (para \( i \geq 2 \)), \( 0 \) (para \( i < 2 \)) | \( A << 2 \) (implementação direta)            |
