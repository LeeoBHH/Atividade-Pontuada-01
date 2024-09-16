
"""
Você está fazendo parte de uma equipe de desenvolvimento e precisa corrigir um código que um de seus colegas não concluiu. 
O objetivo é criar um algoritmo que leia 5 números inteiros e, em seguida, mostre na tela:

1. A quantidade de números pares e ímpares.
2. A quantidade de números positivos e negativos.
3. A quantidade de números inseridos.
4. O maior e o menor número.
5. A média de números pares.
6. A média de números ímpares.
7. A média de todos os números inseridos.
8. Mostrar os números lidos na ordem inversa.
"""
import os
os.system("cls || clear")

# Variáveis para armazenar as estatísticas
lista_vetores = []
QUANTIDADE_NUMEROS = 5
quantidade_pares = 0
quantidade_impares = 0
quantidade_positivos = 0
quantidade_negativos = 0
maior_numero = 0
menor_numero = 0
soma_pares = 0
soma_impares = 0
media_pares = 0
media_impares = 0
media_geral = 0

# Quantidade de números pares e impares.
maior_numero = float('-inf')
menor_numero = float('inf')

for i in range(5):
    numero = int(input(f"Digite o {i+1}° número: "))
    if numero % 2 == 0:
        quantidade_pares += 1
        soma_pares += numero
        media_pares = soma_pares/quantidade_pares
    else: 
        quantidade_impares += 1
        soma_impares += numero
        media_impares = soma_impares/quantidade_impares
    if numero < 0:
        quantidade_negativos += 1
    else:
        quantidade_positivos += 1

        maior_numero = max(maior_numero, numero)
        menor_numero = min(menor_numero, numero) 

        media_geral = numero / QUANTIDADE_NUMEROS
        
print(f"Quantidade de números pares: {quantidade_pares}")
print(f"Quantidade de números impares: {quantidade_impares}")
print(f"Quantidade de números positivos: {quantidade_positivos}")
print(f"Quantidade de números negativos: {quantidade_negativos}")
print(f"A média dos números pares é: {media_pares}")
print(f"A média dos números impares é: {media_impares}")
print(f"O maior número digitado foi: {maior_numero}")
print(f"O menor número digitado foi: {menor_numero}")
print(f"A média geral é: {media_geral}")