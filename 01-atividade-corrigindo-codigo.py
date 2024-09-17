
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
os.system("cls || clear")  # Limpar a tela (opcional)

def inverter_lista(lista):
    lista_invertida = []
    for i in range(len(lista) - 1, -1, -1):
        lista_invertida.append(lista[i])
    return lista_invertida

numeros = []
for i in range(5):
    numero = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)
    
lista_vetores = []
quantidade_pares = 0
quantidade_impares = 0
quantidade_positivos = 0
quantidade_negativos = 0
soma_pares = 0
soma_impares = 0
soma_geral = 0

maior_numero = float('-inf')
menor_numero = float('inf')

for numero in numeros:
    if numero % 2 == 0:
        quantidade_pares += 1
        soma_pares += numero
    else:
        quantidade_impares += 1
        soma_impares += numero

    if numero > 0:
        quantidade_positivos += 1
    elif numero < 0:
        quantidade_negativos += 1

    maior_numero = max(maior_numero, numero)
    menor_numero = min(menor_numero, numero)

    soma_geral += numero

media_pares = soma_pares / quantidade_pares if quantidade_pares > 0 else 0
media_impares = soma_impares / quantidade_impares if quantidade_impares > 0 else 0
media_geral = soma_geral / 5


numeros_invertidos = inverter_lista(lista_vetores)

print("\nAqui estão os resultados dos números que você digitou:")
print(f"Quantos números são pares: {quantidade_pares}")
print(f"Quantos números são ímpares: {quantidade_impares}")
print(f"Quantos números são positivos: {quantidade_positivos}")
print(f"Quantos números são negativos: {quantidade_negativos}")
print(f"Maior número: {maior_numero}")
print(f"Menor número: {menor_numero}")
print(f"Média dos números pares: {media_pares:.2f}")
print(f"Média dos números ímpares: {media_impares:.2f}")
print(f"Média de todos os números: {media_geral:.2f}")
print(f"Números na ordem inversa: {numeros_invertidos}")
