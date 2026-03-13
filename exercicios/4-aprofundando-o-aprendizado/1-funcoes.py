# Crie uma função para selecionar o curso desejado em uma trilha profissional
def cursoTrilha():
  curso = int(input('Escolha um dos cursos a seguir: 1 - Python, 2 - Java: '))
  return curso

# Crie uma função para percorrer todos os níveis de um curso e imprimir na tela a informação do nível atual
def niveisCurso(cursoEscolhido):
  trilha = {1: {'nome': 'Python', 'numerosNiveis': 6}, 2: {'nome': 'Java', 'numerosNiveis': 7}}

  nomeCursoAtual = trilha[cursoEscolhido]['nome']
  nivelCursoAtual = 1
  niveisCursoAtual = trilha[cursoEscolhido]['numerosNiveis']

  print(f'Curso atual: {nomeCursoAtual}. Nível atual: {nivelCursoAtual}. Número total de níveis: {niveisCursoAtual}')

  while nivelCursoAtual <= niveisCursoAtual:
    print(f'Você chegou ao fim do nível {nivelCursoAtual}. Hora de avançar ao próximo nível.')
    nivelCursoAtual += 1
  else:
    print(f'Você chegou ao fim do curso {nomeCursoAtual}. Parabéns!')

# Execute as funções
curso = cursoTrilha()
niveisCurso(curso)
        