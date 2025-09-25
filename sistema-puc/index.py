import json
import os

# Conforme as orientações iniciais, o projeto envolve a criação de um sistema para gestão de dados acadêmicos,
# ou seja, gerenciamento de dados de estudantes, disciplinas, professores, turmas e matrículas.
# Este tipo de sistema pode ser chamado de CRUD (Create – Read - Update – Delete),
# pois para cada um dos dados citados, desenvolveremos as funcionalidades de incluir, listar, atualizar e excluir.

recursos = {
  "estudantes": {
    "acoes": ["criar", "listar", "atualizar", "remover", "voltar"], # { criar: criarEstudante, listar: listarEstudante, ... } (Não sou mt profissional em python, então necessitamos pensar melhor como fazer)
  },
  "disciplinas": {
    "acoes": ["criar", "listar", "atualizar", "remover", "voltar"],
  },
  "professores": {
    "acoes": ["criar", "listar", "atualizar", "remover", "voltar"],
  },
  "turmas": {
    "acoes": ["criar", "listar", "atualizar", "remover", "voltar"],
  },
  "matriculas": {
    "acoes": ["criar", "listar", "atualizar", "remover", "voltar"],
  },
  "sair": {}
}

MENSAGEM_VALUE_ERROR = "\033[91m\nOpção inválida. Por favor, digite apenas números inteiros.\033[0m"
MENSAGEM_INDEX_ERROR = "\033[91m\nOpção inválida. Por favor, digite apenas números que correspondam com uma das opções mostradas.\033[0m"

def obter_caminho_arquivo(nome_recurso):
  return os.path.join("dados", nome_recurso, "data.json")


def salvar_dados_recurso(nome_recurso, lista_dados):
  arquivo_caminho = obter_caminho_arquivo(nome_recurso)
  
  try:
    # criar diretório se não existir
    diretorio = os.path.dirname(arquivo_caminho)
    
    if not os.path.exists(diretorio):
      os.makedirs(diretorio)
      print(f"\033[93mDiretório {diretorio} criado.\033[0m")
    
    with open(arquivo_caminho, 'w', encoding='utf-8') as arquivo:
      json.dump(lista_dados, arquivo, ensure_ascii=False)
    print(f"\033[92mDados de {nome_recurso} salvos com sucesso!\033[0m")
    
  except Exception as e:
    print(f"\033[91mErro ao salvar dados de {nome_recurso}: {e}\033[0m")


def carregar_dados_recurso(nome_recurso) -> list[dict]:
  arquivo_caminho = obter_caminho_arquivo(nome_recurso)
  
  if not os.path.exists(arquivo_caminho):
    print(f"\033[93mArquivo de {nome_recurso} não encontrado. Criando nova lista vazia.\033[0m")
    return []
  
  try:
    with open(arquivo_caminho, 'r', encoding='utf-8') as arquivo:
      dados = json.load(arquivo)
    print(f"\033[92mDados de {nome_recurso} carregados com sucesso!\033[0m")
    return dados
    
  except json.JSONDecodeError:
    print(f"\033[91mErro ao ler arquivo JSON de {nome_recurso}. Criando nova lista vazia.\033[0m")
    return []

  except Exception as e:
    print(f"\033[91mErro ao carregar dados de {nome_recurso}: {e}\033[0m")
    return []


def apresentar_menu_principal():
  print("\nMenu principal")
  
  recursos_nomes = list(recursos.keys())

  for index, recurso in enumerate(recursos_nomes):
    print(f"[{index}] - {recurso}")
  
  return recursos_nomes


def apresentar_menu_operacoes(opcao_nome):
  # menu de operações para um recurso específico
  print(f"\nVocê escolheu gerenciar {opcao_nome}...")
  
  print("\nAções disponíveis: ")
  
  acoes = recursos[opcao_nome]["acoes"]
  for index, acao in enumerate(acoes):
    print(f"[{index}] - {acao}")
  
  return acoes


def listar(lista_dados: list[dict]):  
  if len(lista_dados) == 0:
    print(f"\033[93mNenhum dado foi cadastrado.\033[0m")
    return

  for i, dado in enumerate(lista_dados):
    par = i % 2 == 0
    cor = "\033[47m" if par else "\033[46m"
    print(f"{cor} - {" - ".join(map(str, dado.values()))} \033[0m")
    
  print("Fim da lista.")


def buscar_codigo(lista_dados: list[dict], codigo: int):
  for dado in lista_dados:
    if dado["codigo"] == codigo:
      return dado
      
  return None


def verificar_codigo_unico(lista_dados: list[dict], codigo: int):
  # considerando que a PK de todas as "tabelas" ai ser sempre o código
  dado = buscar_codigo(lista_dados, codigo)
  
  return dado is None


def criar_estudante():
  codigo = int(input("Digite o código do estudante: "))
  nome = input("Digite o nome do estudante: ")
  cpf = input("Digite o CPF do estudante: ")
  
  novo_estudante = {
    "codigo": codigo,
    "nome": nome,
    "cpf": cpf,
  }
  
  lista_estudantes = carregar_dados_recurso("estudantes")
  
  codigo_unico = verificar_codigo_unico(lista_estudantes, codigo)

  if not codigo_unico:
    print(f"\033[91mCódigo {codigo} já está em uso. Tente novamente com outro código.\033[0m")
    return
  
  lista_estudantes.append(novo_estudante)
  
  salvar_dados_recurso("estudantes", lista_estudantes)
  
  print("Estudante adicionado com sucesso.")


def listar_estudantes():
  lista_estudantes = carregar_dados_recurso("estudantes")
  
  estudantes_ordenados = sorted(lista_estudantes, key=lambda x: x['nome'])

  listar(estudantes_ordenados)


def editar_estudante():
  lista_estudantes = carregar_dados_recurso("estudantes")
  
  if len(lista_estudantes) == 0:
    print("\033[93mNenhum estudante foi cadastrado.\033[0m")
    return
  
  codigo = int(input("Digite o código do estudante que deseja atualizar: "))
  
  estudante_encontrado = buscar_codigo(lista_estudantes, codigo)
  
  if not estudante_encontrado:
    print(f"\033[93mNenhum estudante encontrado com o código {codigo}.\033[0m")
    return
  
  novo_codigo = input(f"Digite o novo código do estudante [{estudante_encontrado['nome']}] (opcional): ")
  
  codigo_unico = verificar_codigo_unico(lista_estudantes, int(novo_codigo)) if novo_codigo else True
  
  if not codigo_unico and int(novo_codigo) != estudante_encontrado["codigo"]:
    print(f"\033[91mCódigo {novo_codigo} já está em uso. Tente novamente com outro código.\033[0m")

    print("Lista de estudantes disponíveis:")
    listar_estudantes()
    return
  
  novo_nome = input(f"Digite o novo nome do estudante [{estudante_encontrado['nome']}] (opcional): ")
  novo_cpf = input(f"Digite o novo CPF do estudante [{estudante_encontrado['cpf']}] (opcional): ")
  
  estudante_encontrado["codigo"] = int(novo_codigo) if novo_codigo else estudante_encontrado["codigo"]
  estudante_encontrado["nome"] = novo_nome or estudante_encontrado["nome"]
  estudante_encontrado["cpf"] = novo_cpf or estudante_encontrado["cpf"]

  # aqui a gente tem fé que estudante_encontrado é uma referência de uma posição X na lista de estudantes, logo, quando alteramos ele, já é pra ter alterado na lista
  salvar_dados_recurso("estudantes", lista_estudantes)
  
  print("Estudante atualizado com sucesso.")


def excluir_estudante():
  lista_estudantes = carregar_dados_recurso("estudantes")

  if len(lista_estudantes) == 0:
    print("\033[93mNenhum estudante foi cadastrado.\033[0m")
    return
  
  codigo = int(input("Digite o código do estudante que deseja remover: "))
  
  estudante_encontrado = buscar_codigo(lista_estudantes, codigo)
  
  if not estudante_encontrado:
    print(f"\033[91mNenhum estudante encontrado com o código {codigo}.\033[0m")
    return
  
  lista_estudantes.remove(estudante_encontrado)
  
  salvar_dados_recurso("estudantes", lista_estudantes)
  
  print(f"Estudante {estudante_encontrado['nome']} removido com sucesso.")


# ===== PROFESSORES =====
def criar_professor():
  codigo = int(input("Digite o código do professor(a): "))
  nome = input("Digite o nome do professor(a): ")
  cpf = input("Digite o CPF do professor(a): ")
  
  novo_professor = {
    "codigo": codigo,
    "nome": nome,
    "cpf": cpf,
  }
  
  lista_professores = carregar_dados_recurso("professores")
  
  codigo_unico = verificar_codigo_unico(lista_professores, codigo)

  if not codigo_unico:
    print(f"\033[91mCódigo {codigo} já está em uso. Tente novamente com outro código.\033[0m")
    return
  
  lista_professores.append(novo_professor)
  
  salvar_dados_recurso("professores", lista_professores)
  
  print("Professor(a) adicionado com sucesso.")

def listar_professores():
  lista_professores = carregar_dados_recurso("professores")
  
  professores_ordenados = sorted(lista_professores, key=lambda x: x['nome'])

  listar(professores_ordenados)

def editar_professor():
  lista_professores = carregar_dados_recurso("professores")
  
  if len(lista_professores) == 0:
    print("\033[93mNenhum professor(a) foi cadastrado.\033[0m")
    return
  
  codigo = int(input("Digite o código do professor(a) que deseja atualizar: "))
  
  professor_encontrado = buscar_codigo(lista_professores, codigo)
  
  if not professor_encontrado:
    print(f"\033[93mNenhum professor(a) encontrado com o código {codigo}.\033[0m")
    return
  
  novo_codigo = input(f"Digite o novo código do professor(a) [{professor_encontrado['nome']}] (opcional): ")
  
  codigo_unico = verificar_codigo_unico(lista_professores, int(novo_codigo)) if novo_codigo else True
  
  if not codigo_unico and int(novo_codigo) != professor_encontrado["codigo"]:
    print(f"\033[91mCódigo {novo_codigo} já está em uso. Tente novamente com outro código.\033[0m")
    print("Lista de professores disponíveis:")
    listar_professores()
    return
  
  novo_nome = input(f"Digite o novo nome do professor(a) [{professor_encontrado['nome']}] (opcional): ")
  novo_cpf = input(f"Digite o novo CPF do professor(a) [{professor_encontrado['cpf']}] (opcional): ")
  
  professor_encontrado["codigo"] = int(novo_codigo) if novo_codigo else professor_encontrado["codigo"]
  professor_encontrado["nome"] = novo_nome or professor_encontrado["nome"]
  professor_encontrado["cpf"] = novo_cpf or professor_encontrado["cpf"]

  salvar_dados_recurso("professores", lista_professores)
  
  print("Professor atualizado com sucesso.")

def excluir_professor():
  lista_professores = carregar_dados_recurso("professores")

  if len(lista_professores) == 0:
    print("\033[93mNenhum professor(a) foi cadastrado.\033[0m")
    return
  
  codigo = int(input("Digite o código do professor(a) que deseja remover: "))
  
  professor_encontrado = buscar_codigo(lista_professores, codigo)
  
  if not professor_encontrado:
    print(f"\033[91mNenhum professor(a) encontrado com o código {codigo}.\033[0m")
    return
  
  lista_professores.remove(professor_encontrado)
  
  salvar_dados_recurso("professores", lista_professores)
  
  print(f"Professor {professor_encontrado['nome']} removido com sucesso.")


# ===== DISCIPLINAS =====
def criar_disciplina():
  codigo = int(input("Digite o código da disciplina: "))
  nome = input("Digite o nome da disciplina: ")
  
  nova_disciplina = {
    "codigo": codigo,
    "nome": nome,
  }
  
  lista_disciplinas = carregar_dados_recurso("disciplinas")
  
  codigo_unico = verificar_codigo_unico(lista_disciplinas, codigo)

  if not codigo_unico:
    print(f"\033[91mCódigo {codigo} já está em uso. Tente novamente com outro código.\033[0m")
    return
  
  lista_disciplinas.append(nova_disciplina)
  
  salvar_dados_recurso("disciplinas", lista_disciplinas)
  
  print("Disciplina adicionada com sucesso.")

def listar_disciplinas():
  lista_disciplinas = carregar_dados_recurso("disciplinas")
  
  disciplinas_ordenadas = sorted(lista_disciplinas, key=lambda x: x['nome'])

  listar(disciplinas_ordenadas)

def editar_disciplina():
  lista_disciplinas = carregar_dados_recurso("disciplinas")
  
  if len(lista_disciplinas) == 0:
    print("\033[93mNenhuma disciplina foi cadastrada.\033[0m")
    return
  
  codigo = int(input("Digite o código da disciplina que deseja atualizar: "))
  
  disciplina_encontrada = buscar_codigo(lista_disciplinas, codigo)
  
  if not disciplina_encontrada:
    print(f"\033[93mNenhuma disciplina encontrada com o código {codigo}.\033[0m")
    return
  
  novo_codigo = input(f"Digite o novo código da disciplina [{disciplina_encontrada['nome']}] (opcional): ")
  
  codigo_unico = verificar_codigo_unico(lista_disciplinas, int(novo_codigo)) if novo_codigo else True
  
  if not codigo_unico and int(novo_codigo) != disciplina_encontrada["codigo"]:
    print(f"\033[91mCódigo {novo_codigo} já está em uso. Tente novamente com outro código.\033[0m")
    print("Lista de disciplinas disponíveis:")
    listar_disciplinas()
    return
  
  novo_nome = input(f"Digite o novo nome da disciplina [{disciplina_encontrada['nome']}] (opcional): ")
  
  disciplina_encontrada["codigo"] = int(novo_codigo) if novo_codigo else disciplina_encontrada["codigo"]
  disciplina_encontrada["nome"] = novo_nome or disciplina_encontrada["nome"]

  salvar_dados_recurso("disciplinas", lista_disciplinas)
  
  print("Disciplina atualizada com sucesso.")

def excluir_disciplina():
  lista_disciplinas = carregar_dados_recurso("disciplinas")

  if len(lista_disciplinas) == 0:
    print("\033[93mNenhuma disciplina foi cadastrada.\033[0m")
    return
  
  codigo = int(input("Digite o código da disciplina que deseja remover: "))
  
  disciplina_encontrada = buscar_codigo(lista_disciplinas, codigo)
  
  if not disciplina_encontrada:
    print(f"\033[91mNenhuma disciplina encontrada com o código {codigo}.\033[0m")
    return
  
  lista_disciplinas.remove(disciplina_encontrada)
  
  salvar_dados_recurso("disciplinas", lista_disciplinas)
  
  print(f"Disciplina {disciplina_encontrada['nome']} removida com sucesso.")


# ===== TURMAS =====
def criar_turma():
  codigo = int(input("Digite o código da turma: "))
  codigo_professor = int(input("Digite o código do professor(a): "))
  
  # Verificar se professor(a) existe
  lista_professores = carregar_dados_recurso("professores")
  professor_encontrado = buscar_codigo(lista_professores, codigo_professor)
  
  if not professor_encontrado:
    print(f"\033[91mProfessor com código {codigo_professor} não encontrado.\033[0m")
    return
  

  codigo_disciplina = int(input("Digite o código da disciplina: "))
  # Verificar se disciplina existe
  lista_disciplinas = carregar_dados_recurso("disciplinas")
  disciplina_encontrada = buscar_codigo(lista_disciplinas, codigo_disciplina)
  
  if not disciplina_encontrada:
    print(f"\033[91mDisciplina com código {codigo_disciplina} não encontrada.\033[0m")
    return
  
  nova_turma = {
    "codigo": codigo,
    "codigo_professor": codigo_professor,
    "codigo_disciplina": codigo_disciplina,
  }
  
  lista_turmas = carregar_dados_recurso("turmas")

  turma_repetida = None
  for turma in lista_turmas:
    if (turma["codigo_professor"] == codigo_professor and 
        turma["codigo_disciplina"] == codigo_disciplina):
      turma_repetida = turma
      break

  if turma_repetida:
    print(f"\033[91mJá existe uma turma com o professor(a) {professor_encontrado['nome']} para a disciplina {disciplina_encontrada['nome']} (código da turma: {turma_repetida['codigo']}).\033[0m")
    return
  
  codigo_unico = verificar_codigo_unico(lista_turmas, codigo)

  if not codigo_unico:
    print(f"\033[91mCódigo {codigo} já está em uso. Tente novamente com outro código.\033[0m")
    return
  
  lista_turmas.append(nova_turma)
  
  salvar_dados_recurso("turmas", lista_turmas)
  
  print("Turma adicionada com sucesso.")

def listar_turmas():
  lista_turmas = carregar_dados_recurso("turmas")
  
  turmas_ordenadas = sorted(lista_turmas, key=lambda x: x['codigo'])

  listar(turmas_ordenadas)

def editar_turma():
  lista_turmas = carregar_dados_recurso("turmas")
  
  if len(lista_turmas) == 0:
    print("\033[93mNenhuma turma foi cadastrada.\033[0m")
    return
  
  codigo = int(input("Digite o código da turma que deseja atualizar: "))
  
  turma_encontrada = buscar_codigo(lista_turmas, codigo)
  
  if not turma_encontrada:
    print(f"\033[93mNenhuma turma encontrada com o código {codigo}.\033[0m")
    return
  
  novo_codigo = input(f"Digite o novo código da turma [{turma_encontrada['codigo']}] (opcional): ")
  
  codigo_unico = verificar_codigo_unico(lista_turmas, int(novo_codigo)) if novo_codigo else True
  
  if not codigo_unico and int(novo_codigo) != turma_encontrada["codigo"]:
    print(f"\033[91mCódigo {novo_codigo} já está em uso. Tente novamente com outro código.\033[0m")
    print("Lista de turmas disponíveis:")
    listar_turmas()
    return
  
  novo_codigo_professor = input(f"Digite o novo código do professor(a) [{turma_encontrada['codigo_professor']}] (opcional): ")
  novo_codigo_disciplina = input(f"Digite o novo código da disciplina [{turma_encontrada['codigo_disciplina']}] (opcional): ")
  
  # Verificar se novo professor(a) existe (se fornecido)
  if novo_codigo_professor:
    lista_professores = carregar_dados_recurso("professores")
    professor_encontrado = buscar_codigo(lista_professores, int(novo_codigo_professor))
    
    if not professor_encontrado:
      print(f"\033[91mProfessor com código {novo_codigo_professor} não encontrado.\033[0m")
      return
  
  # Verificar se nova disciplina existe (se fornecida)
  if novo_codigo_disciplina:
    lista_disciplinas = carregar_dados_recurso("disciplinas")
    disciplina_encontrada = buscar_codigo(lista_disciplinas, int(novo_codigo_disciplina))
    
    if not disciplina_encontrada:
      print(f"\033[91mDisciplina com código {novo_codigo_disciplina} não encontrada.\033[0m")
      return
  
  turma_encontrada["codigo"] = int(novo_codigo) if novo_codigo else turma_encontrada["codigo"]
  turma_encontrada["codigo_professor"] = int(novo_codigo_professor) if novo_codigo_professor else turma_encontrada["codigo_professor"]
  turma_encontrada["codigo_disciplina"] = int(novo_codigo_disciplina) if novo_codigo_disciplina else turma_encontrada["codigo_disciplina"]

  salvar_dados_recurso("turmas", lista_turmas)
  
  print("Turma atualizada com sucesso.")

def excluir_turma():
  lista_turmas = carregar_dados_recurso("turmas")

  if len(lista_turmas) == 0:
    print("\033[93mNenhuma turma foi cadastrada.\033[0m")
    return
  
  codigo = int(input("Digite o código da turma que deseja remover: "))
  
  turma_encontrada = buscar_codigo(lista_turmas, codigo)
  
  if not turma_encontrada:
    print(f"\033[91mNenhuma turma encontrada com o código {codigo}.\033[0m")
    return
  
  lista_turmas.remove(turma_encontrada)
  
  salvar_dados_recurso("turmas", lista_turmas)
  
  print(f"Turma {turma_encontrada['codigo']} removida com sucesso.")


# ===== MATRÍCULAS =====
def criar_matricula():
  codigo_turma = int(input("Digite o código da turma: "))
  
  # Verificar se turma existe
  lista_turmas = carregar_dados_recurso("turmas")
  turma_encontrada = buscar_codigo(lista_turmas, codigo_turma)
  
  if not turma_encontrada:
    print(f"\033[91mTurma com código {codigo_turma} não encontrada.\033[0m")
    return
    
  codigo_estudante = int(input("Digite o código do estudante: "))
  
  # Verificar se estudante existe
  lista_estudantes = carregar_dados_recurso("estudantes")
  estudante_encontrado = buscar_codigo(lista_estudantes, codigo_estudante)
  
  if not estudante_encontrado:
    print(f"\033[91mEstudante com código {codigo_estudante} não encontrado.\033[0m")
    return
  
  nova_matricula = {
    "codigo_turma": codigo_turma,
    "codigo_estudante": codigo_estudante,
  }
  
  lista_matriculas = carregar_dados_recurso("matriculas")
  
  # Verificar se já existe matrícula para essa turma e estudante
  matricula_existente = False
  for matricula in lista_matriculas:
    if matricula["codigo_turma"] == codigo_turma and matricula["codigo_estudante"] == codigo_estudante:
      matricula_existente = True
      break
  
  if matricula_existente:
    print(f"\033[91mJá existe uma matrícula para o estudante {codigo_estudante} na turma {codigo_turma}.\033[0m")
    return
  
  lista_matriculas.append(nova_matricula)
  
  salvar_dados_recurso("matriculas", lista_matriculas)
  
  print("Matrícula adicionada com sucesso.")

def listar_matriculas():
  lista_matriculas = carregar_dados_recurso("matriculas")
  
  matriculas_ordenadas = sorted(lista_matriculas, key=lambda x: (x['codigo_turma'], x['codigo_estudante']))

  listar(matriculas_ordenadas)

def editar_matricula():
  lista_matriculas = carregar_dados_recurso("matriculas")
  
  if len(lista_matriculas) == 0:
    print("\033[93mNenhuma matrícula foi cadastrada.\033[0m")
    return
  
  print("\nMatrículas existentes:")
  for i, matricula in enumerate(lista_matriculas):
    print(f"[{i}] - Turma: {matricula['codigo_turma']}, Estudante: {matricula['codigo_estudante']}")
  
  index = int(input("Escolha o índice da matrícula que deseja atualizar: "))
  
  if index < 0 or index >= len(lista_matriculas):
    print("\033[91mÍndice inválido.\033[0m")
    return
  
  matricula_encontrada = lista_matriculas[index]
  
  novo_codigo_turma = input(f"Digite o novo código da turma [{matricula_encontrada['codigo_turma']}] (opcional): ")
  novo_codigo_estudante = input(f"Digite o novo código do estudante [{matricula_encontrada['codigo_estudante']}] (opcional): ")
  
  # Verificar se nova turma existe (se fornecida)
  if novo_codigo_turma:
    lista_turmas = carregar_dados_recurso("turmas")
    turma_encontrada = buscar_codigo(lista_turmas, int(novo_codigo_turma))
    
    if not turma_encontrada:
      print(f"\033[91mTurma com código {novo_codigo_turma} não encontrada.\033[0m")
      return
  
  # Verificar se novo estudante existe (se fornecido)
  if novo_codigo_estudante:
    lista_estudantes = carregar_dados_recurso("estudantes")
    estudante_encontrado = buscar_codigo(lista_estudantes, int(novo_codigo_estudante))
    
    if not estudante_encontrado:
      print(f"\033[91mEstudante com código {novo_codigo_estudante} não encontrado.\033[0m")
      return
  
  codigo_turma_final = int(novo_codigo_turma) if novo_codigo_turma else matricula_encontrada["codigo_turma"]
  codigo_estudante_final = int(novo_codigo_estudante) if novo_codigo_estudante else matricula_encontrada["codigo_estudante"]
  
  # Verificar se já existe outra matrícula com essa combinação
  if (codigo_turma_final != matricula_encontrada["codigo_turma"] or 
      codigo_estudante_final != matricula_encontrada["codigo_estudante"]):
    
    for i, matricula in enumerate(lista_matriculas):
      if (i != index and matricula["codigo_turma"] == codigo_turma_final and 
          matricula["codigo_estudante"] == codigo_estudante_final):
        print(f"\033[91mJá existe uma matrícula para o estudante {codigo_estudante_final} na turma {codigo_turma_final}.\033[0m")
        return
  
  matricula_encontrada["codigo_turma"] = codigo_turma_final
  matricula_encontrada["codigo_estudante"] = codigo_estudante_final

  salvar_dados_recurso("matriculas", lista_matriculas)
  
  print("Matrícula atualizada com sucesso.")

def excluir_matricula():
  lista_matriculas = carregar_dados_recurso("matriculas")

  if len(lista_matriculas) == 0:
    print("\033[93mNenhuma matrícula foi cadastrada.\033[0m")
    return
  
  print("\nMatrículas existentes:")
  for i, matricula in enumerate(lista_matriculas):
    print(f"[{i}] - Turma: {matricula['codigo_turma']}, Estudante: {matricula['codigo_estudante']}")
  
  index = int(input("Escolha o índice da matrícula que deseja remover: "))
  
  if index < 0 or index >= len(lista_matriculas):
    print("\033[91mÍndice inválido.\033[0m")
    return
  
  matricula_removida = lista_matriculas.pop(index)
  
  salvar_dados_recurso("matriculas", lista_matriculas)
  
  print(f"Matrícula (Turma: {matricula_removida['codigo_turma']}, Estudante: {matricula_removida['codigo_estudante']}) removida com sucesso.")


def main():
  while True:
    try:
      recursos_nomes = apresentar_menu_principal()
      
      opcao = int(input("Escolha o recurso que deseja gerenciar (0-5): "))
      
      opcao_nome = recursos_nomes[opcao]
      # recurso = recursos[opcao_nome]
      
      if opcao_nome == "sair":
        print("\nFoi bom enquanto durou...")
        break
      
      while True:
        try:
          acoes = apresentar_menu_operacoes(opcao_nome)
          
          opcao = int(input("Escolha a ação que deseja realizar (0-4): "))
          
          acao = acoes[opcao]
          
          if acao == "voltar":
            print("\nVoltando...")
            break
          
          print(f"\nVocê escolheu a ação {acao}")
          
          if opcao_nome == "estudantes":
            if acao == "listar":
              listar_estudantes()
            elif acao == "criar":
              criar_estudante()
            elif acao == "atualizar":
              editar_estudante()
            elif acao == "remover":
              excluir_estudante()
            continue

          elif opcao_nome == "disciplinas":
            if acao == "listar":
              listar_disciplinas()
            elif acao == "criar":
              criar_disciplina()
            elif acao == "atualizar":
              editar_disciplina()
            elif acao == "remover":
              excluir_disciplina()
            continue
          
          elif opcao_nome == "professores":
            if acao == "listar":
              listar_professores()
            elif acao == "criar":
              criar_professor()
            elif acao == "atualizar":
              editar_professor()
            elif acao == "remover":
              excluir_professor()
            continue

          elif opcao_nome == "turmas":
            if acao == "listar":
              listar_turmas()
            elif acao == "criar":
              criar_turma()
            elif acao == "atualizar":
              editar_turma()
            elif acao == "remover":
              excluir_turma()
            continue

          elif opcao_nome == "matriculas":
            if acao == "listar":
              listar_matriculas()
            elif acao == "criar":
              criar_matricula()
            elif acao == "atualizar":
              editar_matricula()
            elif acao == "remover":
              excluir_matricula()
            continue
          
          else:
            print(f"\nAção {acao} de {opcao_nome} em desenvolvimento")
            
          print("\nVoltando para o menu principal...")
          
        # os except acabaram ficando duplicados, mas era pq, se eu deixasse só no while maior,
        # toda vez que digitassem um valor incorreto, voltaria pro menu principal e não pro menu do recurso
        except ValueError:
          print(MENSAGEM_VALUE_ERROR)
        
        except IndexError:
          print(MENSAGEM_INDEX_ERROR)
    
    except ValueError:
      print(MENSAGEM_VALUE_ERROR)
    
    except IndexError:
      print(MENSAGEM_INDEX_ERROR)
    
    except Exception as error:
      print(f"\033[91m\nVish maria, como que tu fez isso? {error}\033[0m")


if __name__ == "__main__":
  main()