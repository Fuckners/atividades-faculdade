Atividade Formativa - Raciocínio computacional - Semanas 1/2/3/4

# Descrição
    Conforme as orientações iniciais, o projeto envolve a criação de um sistema para gestão de dados acadêmicos, ou seja, gerenciamento de dados de   estudantes, disciplinas, professores, turmas e matrículas. Este tipo de sistema pode ser chamado de CRUD (Create – Read - Update – Delete), pois para cada um dos dados citados, desenvolveremos as funcionalidades de incluir, listar, atualizar e excluir.


# Semana 01
---

# Semana 02
---

# Semana 03
---

# Semana 04
---

# Semana 05

- Ao incluir, listar ou editar um estudante, as seguintes informações devem ser utilizadas:
    - Código do estudante (Número inteiro).
    - Nome do estudante (String).
    - CPF do estudante (String).

- Os dados do estudante devem ser armazenados em um dicionário ou tupla, que por sua vez, devem ser adicionados à uma lista.
  - ANTES: lista de nomes de estudantes, onde cada posição da lista é uma string equivalente ao nome do estudante
    ```py
    ["Lucas", "Pedro"]
    ```

  - AGORA: lista de estudantes, onde cada posição da lista é um dicionário ou uma tupla, representando os dados do estudante (e exemplo abaixo utiliza dicionário)

    ```py
    [ 
        {"codigo": 1, "nome": "Lucas", "cpf": "999"}, 
        {"codigo": 2, "nome": "Pedro", "cpf": "555"} 
    ]
    ```
- Desenvolver a funcionalidade de excluir um estudante, onde deve ser perguntado ao usuário qual o código do estudante que ele deseja excluir, para então remover o estudante correspondente da lista. Lembre-se que você deve percorrer a lista e encontrar uma tupla ou dicionário que contenha o código igual ao informado, e então excluir esta estrutura da lista.
- 
- Desenvolver a funcionalidade de editar um estudante, onde deve ser perguntado ao usuário o código do estudante que se deseja editar, e então realizar a entrada dos dados correspondentes a todos dados do estudante (código, nome e cpf). Após isso, estes dados devem ser atualizados no dicionário ou tupla correspondente dentro da lista de estudantes.

---

# Semana 06
Chegou a hora de iniciarmos a utilização de funções dentro de nosso algoritmo, visando a modularização de nosso sistema, maior organização do script e reaproveitamento de código. Vamos lá?
O que devo desenvolver?
- Você deve obrigatoriamente modularizar (colocar dentro de funções) as seguintes funcionalidades:
  - Apresentação do Menu Principal
  - Apresentação do Menu de Operações
  - Inclusão de estudante
  - Listagem de estudantes
  - Edição de estudante
  - Exclusão de estudante
  
Caso queira, você pode modularizar outras partes do sistema, desde que seguindo boas práticas de desenvolvimento e modularização.
Para refletir: As 4 operações que estamos trabalhando (incluir, listar, editar, excluir), futuramente devem ser aplicadas a todos os dados que vamos trabalhar (estudantes, turmas, disciplinas, professores, matrículas). Será que conseguimos criar uma função única de inclusão para todos os tipos de dados? E para as outras operações?

---

# Semana 07
O que devo desenvolver?
- Função para salvar lista de estudantes em um arquivo JSON.
- Função para recuperar lista de estudantes de um arquivo JSON e armazenar em uma variável em memória.
- Adaptação das funções de incluir, listar, excluir e editar estudantes para que acessem as duas funções acima sempre que necessário.
Tem como me dar mais detalhes?
Vamos tomar como exemplo o fluxo para incluir um estudante, a seguir o passo a passo das operações pensando nas novas funções para manipulação do arquivo JSON:
- 1.	Leitura dos dados do novo estudante.
- 2.	Criação de um dicionário ou tupla contendo todos os campos informados.
- 3.	Chamada à função para recuperar os dados já cadastrados.
  - 3.1. A função deve buscar o arquivo de estudantes e retornar a lista recuperada do arquivo (caso o arquivo não exista, retornar uma lista vazia).
- 4.	Adicionar o dicionário ou tupla na lista retornada.
- 5.	Chamada à função para salvar lista de estudantes atualizada.
Deste modo, sempre que incluirmos um novo estudante, já atualizaremos o arquivo que está em disco.
