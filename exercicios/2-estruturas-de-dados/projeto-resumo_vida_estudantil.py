# Nesse exercício coletaremos dados de uma estudante, armazenaremos em um dicionário e imprimiremos na tela esse dados em um formato amigável.

# 1. Solicite a estudante os seguintes dados: nome, ano que conheceu o LinkedIn, ano atual e os cursos realizados no LinkedIn Learning separados por virgula em ordem cronológica
# 2. Armazene esses dados em um dicionário
# 3. Imprima na tela uma string com as informações de nome, ano_conheceu_linkedin, total de anos transcurridos, total de cursos realizados e (apenas) o primeiro e último curso.

estudante = {}
estudante['nome'] = input('Qual o seu nome? ')
estudante['ano_LinkedIn'] = int(input('Qual o ano que conheceu o LinkedIn Learning? '))
estudante['ano_atual'] = int(input('Qual o ano atual? '))
cursos = input('Quais os cursos que fez na plataforma? (Separe-os com vírgula[,] e espaço) ')

anos_transcorridos = estudante['ano_atual'] - estudante['ano_LinkedIn']
estudante['cursos'] = cursos.split(', ')
total_cursos = len(estudante['cursos'])
print(f"O/A estudante {estudante['nome']} conheceu o LinkedIn Learning no ano de {estudante['ano_LinkedIn']}. Agora se passaram {anos_transcorridos} anos e seu primeiro curso foi de {estudante['cursos'][0]}, totalizando hoje {total_cursos} cursos")