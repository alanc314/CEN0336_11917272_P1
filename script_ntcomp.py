#!/usr/bin/env python3

seq = input("Insira sua sequência de DNA: ").upper() # recebe a seq por input

# cria variáveis vazias para receber a contagem
contagem_A = 0
contagem_C = 0
contagem_T = 0
contagem_G = 0

for i in seq: # confere se há letras inválidas na sequência e faz a contagem
    if i != "A" and i != "C" and i != "T" and i != "G":
        print("Erro - Insira apenas a sequência de DNA com letras que simbolizam nucleotídeos.")
        break  
    else:
        if i == "A":
            contagem_A += 1
        elif i == "C":
            contagem_C += 1
        elif i == "T":
            contagem_T += 1
        elif i == "G":
            contagem_G += 1

# imprime os resultados
print(f"A: {contagem_A}")
print(f"T: {contagem_T}")
print(f"C: {contagem_C}")
print(f"G: {contagem_G}")

