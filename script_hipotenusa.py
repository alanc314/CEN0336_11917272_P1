#!/usr/bin/env python3

import sys # importa a biblioteca sys

if len(sys.argv) != 3: # confere se foi colocado todos parametros necessários
	print("Erro - Coloque todos os números necessários")
	sys.exit()

a = sys.argv[1] # recebe a
b = sys.argv[2] # recebe b

if not (a.isdigit() and b.isdigit()): # confere se o usuário colocar um digito e, não uma letra
    print("Erro - Coloque apenas números inteiros")
    sys.exit()

a_int = int(a) # transforma a em int
b_int = int(b) # transforma b em int

if a_int < 0 or a_int > 500 or b_int < 0 or b_int > 500: # confere se a e b são positivos e menores que 500
	print("Erro - Coloque apenas números inteiros positivos menores que 500")
	sys.exit()

hip2 = a_int ** 2 + b_int ** 2 # calcula o quadrado da hipotenusa

print(f"O quadrado da hipotenusa para o triangulo retângulo com lados a={a_int} e b={b_int}, é {hip2}") # print o resultado


