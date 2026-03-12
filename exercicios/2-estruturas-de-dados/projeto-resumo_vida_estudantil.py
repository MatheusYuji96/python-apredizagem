# Nesse exercício coletaremos dados de uma estudante, armazenaremos em um dicionário e imprimiremos na tela esse dados em um formato amigável.

# 1. Solicite a estudante os seguintes dados: nome, ano que conheceu o LinkedIn, ano atual e os cursos realizados no LinkedIn Learning separados por virgula em ordem cronológica
# 2. Armazene esses dados em um dicionário
# 3. Imprima na tela uma string com as informações de nome, ano_conheceu_linkedin, total de anos transcurridos, total de cursos realizados e (apenas) o primeiro e último curso.

estudante = {}
estudante['nome'] = input('Qual o seu nome? ')
estudante['ano_LinkedIn'] = input('Qual o ano que conheceu o LinkedIn Learning? ')
estudante['ano_atual'] = input('Qual o ano atua? ')
cursos = input('Quais os cursos que fez na plataforma? (Separe-os com vírgula[,] e espaço) ')

estudante['cursos'] = cursos.split(', ')
print(f"O/A estudante {estudante['nome']} conheceu o LinkedIn Learning no ano de {estudante['ano_LinkedIn']}. Agora é {estudante['ano_atual']} e já fez os cursos de {estudante['cursos']}")