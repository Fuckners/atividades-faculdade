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

MENSAGEM_VALUE_ERROR = "\nOpção inválida. Por favor, digite apenas números inteiros."
MENSAGEM_INDEX_ERROR = "\nOpção inválida. Por favor, digite apenas números que correspondam com uma das opções mostradas."

while True:
  try:
    index = 0
    print("\nMenu principal")

    recursos_nomes = list(recursos.keys())
    # print(recursos_nomes)
    for recurso in recursos:
      print(f"[{index}] - {recurso}")
      index += 1

    opcao = int(input("Escolha o recurso que deseja gerenciar (0-5): "))

    opcao_nome = recursos_nomes[opcao]
    recurso = recursos[opcao_nome]

    if opcao_nome == "sair":
      print("\nFoi bom enquanto durou...")
      break

    print(f"\nVocê escolheu gerenciar {opcao_nome}...")

    while True:
      try:
        index = 0
        print("\nAções disponíveis: ")

        acoes = recurso["acoes"]
        for acao in acoes:
          print(f"[{index}] - {acao}")
          index += 1

        opcao = int(input("Escolha a ação que deseja realizar (0-4): "))

        acao = acoes[opcao]

        if acao == "voltar":
          print("\nVoltando...")
          break

        print(f"\nVocê escolheu a ação {acao}")

        if acao == "criar": # o plano é dps usar esse ação pra chamar um callback, ai a prop "ações" de cada recurso iria ser um objeto (ou algo nessa vibe)
          novo_dado = input(f"Digite o nome que você deseja [{opcao_nome}]: ")
          recurso["dados"].append(novo_dado)
          print("Dado adicionado com sucesso.")

        elif acao == "listar":
          if len(recurso["dados"]) == 0:
            print(f"Nenhum dado foi cadastrado para {opcao_nome}.")
            continue

          for dado in sorted(recurso["dados"]):
            print(f" - {dado}")
            
          print("Fim da lista.")

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
    print(f"\nVish maria, como que tu fez isso? {error}")