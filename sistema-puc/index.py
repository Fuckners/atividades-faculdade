# Conforme as orientações iniciais, o projeto envolve a criação de um sistema para gestão de dados acadêmicos,
# ou seja, gerenciamento de dados de estudantes, disciplinas, professores, turmas e matrículas.
# Este tipo de sistema pode ser chamado de CRUD (Create – Read - Update – Delete),
# pois para cada um dos dados citados, desenvolveremos as funcionalidades de incluir, listar, atualizar e excluir.

# cogitar criar uma variável a parte pra ser o "banco"
# dados = {
#   "estudantes": [],
#   "disciplinas": [],
#   "professores": [],
#   "turmas": [],
#   "matriculas": [],
# }

# ["estudantes", "disciplinas", "professores", "turmas", "matriculas", "sair"]
recursos = {
  "estudantes": {
    "acoes": ["criar", "listar", "atualizar", "remover", "voltar"], # { criar: criarEstudante, listar: listarEstudante, ... } (Não sou mt profissional em python, então necessitamos pensar melhor como fazer)
    "dados": [],
  },
  "disciplinas": {
    "acoes": ["criar", "listar", "atualizar", "remover", "voltar"],
    "dados": [],
  },
  "professores": {
    "acoes": ["criar", "listar", "atualizar", "remover", "voltar"],
    "dados": [],
  },
  "turmas": {
    "acoes": ["criar", "listar", "atualizar", "remover", "voltar"],
    "dados": [],
  },
  "matriculas": {
    "acoes": ["criar", "listar", "atualizar", "remover", "voltar"],
    "dados": [],
  },
  "sair": {}
}

# Lembrete: dá pra colocar corzinhas dps pra ficar mais fácil do cara se localizar

MENSAGEM_VALUE_ERROR = "\033[91m\nOpção inválida. Por favor, digite apenas números inteiros.\033[0m"
MENSAGEM_INDEX_ERROR = "\033[91m\nOpção inválida. Por favor, digite apenas números que correspondam com uma das opções mostradas.\033[0m"

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
  
  index = 0
  print("\nAções disponíveis: ")
  
  acoes = recursos[opcao_nome]["acoes"]
  for acao in acoes:
    print(f"[{index}] - {acao}")
    index += 1
  
  return acoes

def criar_estudante():
  recurso = recursos["estudantes"]

  codigo = int(input("Digite o código do estudante: "))

  codigo_existe = False
  for estudante in recurso["dados"]:
    if estudante["codigo"] == codigo:
      codigo_existe = True
      break
  
  if codigo_existe:
    print(f"\033[91mCódigo {codigo} já está em uso. Tente novamente com outro código.\033[0m")
    return
  
  nome = input("Digite o nome do estudante: ")
  cpf = input("Digite o CPF do estudante: ")
  
  recurso["dados"].append({
    "codigo": codigo,
    "nome": nome,
    "cpf": cpf,
  })
  
  print("Estudante adicionado com sucesso.")

def listar_estudantes():
  recurso = recursos["estudantes"]

  if len(recurso["dados"]) == 0:
    print("\033[93mNenhum estudante foi cadastrado.\033[0m")
    return
  
  estudantes_ordenados = sorted(recurso["dados"], key=lambda x: x['nome'])

  for i, estudante in enumerate(estudantes_ordenados):
    par = i % 2 == 0
    cor = "\033[47m" if par else "\033[46m"
    print(f"{cor} - {estudante['codigo']} - {estudante['nome']} - {estudante['cpf']} \033[0m")

  print("Fim da lista.")

def editar_estudante():
  recurso = recursos["estudantes"]
  if len(recurso["dados"]) == 0:
    print("\033[93mNenhum estudante foi cadastrado.\033[0m")
    return
  
  codigo = int(input("Digite o código do estudante que deseja atualizar: "))
  
  estudante_encontrado = None
  for estudante in recurso["dados"]:
    if estudante["codigo"] == codigo:
      estudante_encontrado = estudante
      break
  
  if not estudante_encontrado:
    print(f"\033[93mNenhum estudante encontrado com o código {codigo}.\033[0m")
    return
  
  novo_codigo = input(f"Digite o novo código do estudante [{estudante_encontrado['nome']}] (opcional): ")
  
  codigo_existe = False
  
  if novo_codigo and int(novo_codigo) != estudante_encontrado["codigo"]:
    for estudante in recurso["dados"]:
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
  estudante_encontrado["nome"] = novo_nome if novo_nome else estudante_encontrado["nome"]
  estudante_encontrado["cpf"] = novo_cpf if novo_cpf else estudante_encontrado["cpf"]
  
  print("Estudante atualizado com sucesso.")

def excluir_estudante():
  recurso = recursos["estudantes"]

  if len(recurso["dados"]) == 0:
    print("\033[93mNenhum estudante foi cadastrado.\033[0m")
    return
  
  codigo = int(input("Digite o código do estudante que deseja remover: "))
  
  estudante_encontrado = None
  for estudante in recurso["dados"]:
    if estudante["codigo"] == codigo:
      estudante_encontrado = estudante
      break
  
  if not estudante_encontrado:
    print(f"\033[91mNenhum estudante encontrado com o código {codigo}.\033[0m")
    return
  
  recurso["dados"].remove(estudante_encontrado)
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
            if len(recurso["dados"]) == 0:
              print(f"Nenhum dado foi cadastrado para {opcao_nome}.")
              continue
            
            for dado in sorted(recurso["dados"]):
              print(f" - {dado}")
              
            print("Fim da lista.")

          elif acao == "criar": # o plano é dps usar esse ação pra chamar um callback, ai a prop "ações" de cada recurso iria ser um objeto (ou algo nessa vibe)
            novo_dado = input(f"Digite o nome que você deseja [{opcao_nome}]: ")
            recurso["dados"].append(novo_dado)
            print("Dado adicionado com sucesso.")
          
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