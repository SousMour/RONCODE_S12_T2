#Escreva um programa que calcule o fatorial de um número inteiro lido, sabendo-se que: N ! = 1 x 2 x 3 x ... x N-1 x N 0 ! = 1

numeros = int(input())
fatorial = 1
contador = 1
while contador <= numeros:
    fatorial *= contador
    contador += 1
print(fatorial)