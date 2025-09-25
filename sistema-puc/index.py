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