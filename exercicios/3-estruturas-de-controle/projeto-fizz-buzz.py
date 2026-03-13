# Criaremos um programa para substituir números por palavras em uma lista
# 1. Crie uma lista com 15 números
listaNumeros = list(range(100,151))
print(listaNumeros)
# 2. Crie um for loop para percorrer todos os elementos da lista
# 3. Crie uma estrutura condicional para verificar cada número da lista:
# 3.1 Caso o número seja divisível por 3, substitua-o por "Fizz"
# 3.2 Caso o número seja divisível por 5, substitua-o por "Buzz"
# 3.3 Caso o número seja divisível por 3 e 5, substitua-o por "FizzBuzz"
index = 0
for numeros in listaNumeros:
  if numeros % 3 == 0 and numeros % 5 == 0:
    listaNumeros[index] = "FizzBuzz"
  elif numeros % 3 == 0:
    listaNumeros[index] = "Fizz"
  elif numeros % 5 == 0:
    listaNumeros[index] = "Buzz"
  index += 1
print(listaNumeros)

