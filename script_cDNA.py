#!/usr/bin/env python3

import sys # importa a bibloteca

if len(sys.argv) != 8: # confere se o usuaríos colocou todos os items
    print("Erro - Coloque a sequência de DNA e seis números inteiros.")
    sys.exit()

# recebe os itens e guarda em variáveis
seq = sys.argv[1]  
n1 = sys.argv[2]
n2 = sys.argv[3]
n3 = sys.argv[4]
n4 = sys.argv[5]
n5 = sys.argv[6]
n6 = sys.argv[7]

if not (n1.isdigit() and n2.isdigit() and n3.isdigit() and n4.isdigit() and n5.isdigit() and n6.isdigit()): # confere seus os números das posições são inteiros
    print("Erro - Todos os números devem ser inteiros")
    sys.exit()

# transforma todos os números em int
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)
n4 = int(n4)
n5 = int(n5)
n6 = int(n6)

seq_lenght = len(seq) # calcula o tamanho da seq

# Conferir se os números não são maiores que o tamanho da sequência
for num in [n1, n2, n3, n4, n5, n6]:
    if num > seq_lenght:
        print("Erro -  Algum(s) do(s) número(s) inseridos são maiores que a própria sequência.")
        sys.exit()


seq_CDS1_CDS2 = seq[n2:n3] # pega a seq entre o final da CDS1 e o início da CDS2

# confere se seq_CDS1_CDS2 começa com GT e termina com AG
if not (seq_CDS1_CDS2.startswith("GT") and seq_CDS1_CDS2.endswith("AG")):
    print("A sequência entre CDS1 e CDS2 não começa com 'GT' e termina com 'AG'.")
    sys.exit()


seq_CDS2_CDS3 = seq[n4:n5] # pega a seq entre o final da CDS2 e o início da CDS#

# confere se seq_CDS2_CDS3 começa com GT e termina com AG
if not (seq_CDS2_CDS3.startswith("GT") and seq_CDS2_CDS3.endswith("AG")):
    print("A sequência entre CDS2 e CDS3 não começa com 'GT' e termina com 'AG'.")
    sys.exit()
# Retorna as seq das CDSs
CDS1 = seq[n1:n2]
CDS2 = seq[n3:n4]
CDS3 = seq[n5:n6]
seq_final = CDS1 + CDS2 + CDS3

# imprime a seq das CDSs concatenada
print(f"A sequência final concatenada das CDS 1, 2 e 3 é {seq_final}")

