# Declare 4 variáveis do tipo numérica
a = 29
f = 51.7
l = 1.66
p = 674

# Crie uma estrutura condicional para comparar dois números
if a >= f:
  print(True)
else:
  print(False)

# Se a condição for verdadeira, imprima na tela uma mensagem informando que a condição foi cumprida e informando o número de maior valor
if a >= f:
  print(f'{a}, o maior valor da condição, é maior que {f}')
else:
  print(False)

# Se a condição não for cumprida, imprima na tela uma mensagem informando que a condição é negativa e informe o número de maior valor
if a >= f:
  print(True)
else:
  print(f'{a} não é maior que {f}, o maior valor da condição')

# Insira outras condições na estrutura condicional usando o elif
if a > f:
  print(True)
elif a == f:
  print(True * 2)
else:
  print(False)

# Incremente a estrutura condicional já existente com expressões lógicas utilizando "and" ou "or"
if (a > f) and (l < p):
  print(True)
elif (a == f) or (a < p):
  print(f'True * 2')
else:
  print(False)

# Crie uma estrutura condicional onde mais de uma condição seja verdadeira, e use apenas a palavra reservada "if"
if (a < p):
  print(f'{p} é maior que {a}')
if (f > l):
  print(f'{f} é maior do que {l}')