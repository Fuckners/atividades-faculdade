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
ARQUIVO_ESTUDANTES = os.path.join("dados", "estudante", "data.json")

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

def carregar_dados_recurso(nome_recurso):
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

def salvar_estudantes(lista_estudantes):
  salvar_dados_recurso("estudantes", lista_estudantes)

def carregar_estudantes():
  return carregar_dados_recurso("estudantes")

def apresentar_menu_principal():
  index = 0
  print("\nMenu principal")
  
  recursos_nomes = list(recursos.keys())
  for recurso in recursos:
    print(f"[{index}] - {recurso}")
    index += 1
  
  return recursos_nomes

def apresentar_menu_operacoes(opcao_nome):
  # menu de operações para um recurso específico
  print(f"\nVocê escolheu gerenciar {opcao_nome}...")
  
  print("\nAções disponíveis: ")
  
  acoes = recursos[opcao_nome]["acoes"]
  for index, acao in enumerate(acoes):
    print(f"[{index}] - {acao}")
  
  return acoes

def criar_estudante():
  codigo = int(input("Digite o código do estudante: "))
  nome = input("Digite o nome do estudante: ")
  cpf = input("Digite o CPF do estudante: ")
  
  novo_estudante = {
    "codigo": codigo,
    "nome": nome,
    "cpf": cpf,
  }
  
  lista_estudantes = carregar_estudantes()
  
  codigo_existe = False
  for estudante in lista_estudantes:
    if estudante["codigo"] == codigo:
      codigo_existe = True
      break
  
  if codigo_existe:
    print(f"\033[91mCódigo {codigo} já está em uso. Tente novamente com outro código.\033[0m")
    return
  
  lista_estudantes.append(novo_estudante)
  
  salvar_estudantes(lista_estudantes)
  
  print("Estudante adicionado com sucesso.")

def listar_estudantes():
  lista_estudantes = carregar_estudantes()

  if len(lista_estudantes) == 0:
    print("\033[93mNenhum estudante foi cadastrado.\033[0m")
    return
  
  estudantes_ordenados = sorted(lista_estudantes, key=lambda x: x['nome'])

  for i, estudante in enumerate(estudantes_ordenados):
    par = i % 2 == 0
    cor = "\033[47m" if par else "\033[46m"
    print(f"{cor} - {estudante['codigo']} - {estudante['nome']} - {estudante['cpf']} \033[0m")

  print("Fim da lista.")

def editar_estudante():
  lista_estudantes = carregar_estudantes()
  
  if len(lista_estudantes) == 0:
    print("\033[93mNenhum estudante foi cadastrado.\033[0m")
    return
  
  codigo = int(input("Digite o código do estudante que deseja atualizar: "))
  
  estudante_encontrado = None
  for estudante in lista_estudantes:
    if estudante["codigo"] == codigo:
      estudante_encontrado = estudante
      break
  
  if not estudante_encontrado:
    print(f"\033[93mNenhum estudante encontrado com o código {codigo}.\033[0m")
    return
  
  novo_codigo = input(f"Digite o novo código do estudante [{estudante_encontrado['nome']}] (opcional): ")
  
  codigo_existe = False
  
  if novo_codigo and int(novo_codigo) != estudante_encontrado["codigo"]:
    for estudante in lista_estudantes:
      if estudante["codigo"] == int(novo_codigo):
        codigo_existe = True
        break
  
  if codigo_existe:
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
  salvar_estudantes(lista_estudantes)
  
  print("Estudante atualizado com sucesso.")

def excluir_estudante():
  lista_estudantes = carregar_estudantes()

  if len(lista_estudantes) == 0:
    print("\033[93mNenhum estudante foi cadastrado.\033[0m")
    return
  
  codigo = int(input("Digite o código do estudante que deseja remover: "))
  
  estudante_encontrado = None
  for estudante in lista_estudantes:
    if estudante["codigo"] == codigo:
      estudante_encontrado = estudante
      break
  
  if not estudante_encontrado:
    print(f"\033[91mNenhum estudante encontrado com o código {codigo}.\033[0m")
    return
  
  lista_estudantes.remove(estudante_encontrado)
  
  salvar_estudantes(lista_estudantes)
  
  print(f"Estudante {estudante_encontrado['nome']} removido com sucesso.")

def main():
  while True:
    try:
      recursos_nomes = apresentar_menu_principal()
      
      opcao = int(input("Escolha o recurso que deseja gerenciar (0-5): "))
      
      opcao_nome = recursos_nomes[opcao]
      recurso = recursos[opcao_nome]
      
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
          
          # Ações de alunos
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
          
          if acao == "listar":
            lista_dados = carregar_dados_recurso(opcao_nome)
            
            if len(lista_dados) == 0:
              print(f"\033[93mNenhum dado foi cadastrado para {opcao_nome}.\033[0m")
              continue
            
            print(f"\nLista de {opcao_nome}:")
            for i, dado in enumerate(sorted(lista_dados, key=lambda x: x["nome"])):
              par = i % 2 == 0
              cor = "\033[47m" if par else "\033[46m"
              print(f"{cor} - {dado["nome"]} \033[0m")
              
            print("Fim da lista.")

          elif acao == "criar":
            novo_nome = input(f"Digite o nome que você deseja para {opcao_nome}: ")
            
            lista_dados = carregar_dados_recurso(opcao_nome)
            
            novo_item = {"nome": novo_nome}
            
            lista_dados.append(novo_item)
            
            salvar_dados_recurso(opcao_nome, lista_dados)
            
            print(f"\033[92m{opcao_nome.capitalize()} '{novo_nome}' adicionado com sucesso!\033[0m")
          
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