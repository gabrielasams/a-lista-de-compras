def listar_produtos(produtos):
    print("\n" + "=" * 30)
    if not produtos:
        print("Nenhum produto adicionado ainda.")
    else:
        print("Lista de Compras:")
        for produto in produtos:
            print(f"\nID: {produto['id']}")
            print(f"Produto: {produto['nome']}")
            print(f"Quantidade: {produto['quantidade']} {produto['unidade de medida']}")
            print(f"Descrição: {produto['descrição']}")
    print("=" * 30 + "\n")

def visualizar_menu():
    print("Bem-vinde a Lista de Compras Simples")
    print("\nOpções:")
    print("A - Adicionar produto")
    print("D - Sair\n")

def adicionar_produto(controleID, medidas):
    print("\n" + "-" * 30)
    print("Adicionar novo produto\n")
    nome = validar_entrada("Nome: ")
    unidade = escolher_medida(medidas)

    while True:
        try:
            quantidade = input("Quantidade: ").replace(",", ".")
            quantidade = float(quantidade)
            
            if quantidade <= 0:
                print("Digite um valor positivo.")
            else:
                break
        except ValueError:
            print("Entrada inválida! Digite um número válido (ex: 2 ou 1.5).")
      
    descricao = validar_entrada("Descrição: ")
    print("-" * 30)

    produto = {
        "id": controleID,
        "nome": nome,
        "unidade de medida": unidade,
        "quantidade": quantidade,
        "descrição": descricao
    }
    return produto

def validar_texto(texto):
    return texto and not texto.isspace()

def validar_entrada(mensagem):
    while True:
        entrada = input(mensagem).strip()
        if validar_texto(entrada):
            return entrada.capitalize()
        print("Esse campo não pode ficar vazio! Tente novamente.")

def escolher_medida(medidas):
    print("\nEscolha a unidade de medida:")
    for letra, unidade in medidas.items():
        print(f"{letra} - {unidade}")

    while True:
        opcao = input("\nOpção: ").upper()
        if opcao in medidas:
            return medidas[opcao]
        print("Opção inválida! Digite uma letra de A a G.")

def iniciar_sistema():
    dicionario_unidade_medidas = {
        'A': 'Quilograma',
        'B': 'Grama',
        'C': 'Litro',
        'D': 'Mililitro',
        'E': 'Unidade',
        'F': 'Metro',
        'G': 'Centímetro'
    }
    
    lista_produtos = []
    controle_id = 1

    while True:
        listar_produtos(lista_produtos)
        visualizar_menu()

        opcao = input("Escolha uma opção: ").upper().strip()

        if opcao == 'D':
            print("\nObrigada por utilizar a Lista de Compras Simples!")
            break
        
        if opcao == 'A':
            produto = adicionar_produto(controle_id, dicionario_unidade_medidas)
            lista_produtos.append(produto)
            print(f"\nProduto '{produto['nome']}' adicionado com sucesso! (ID: {produto['id']})")
            controle_id += 1
        else:
            print("\nOpção inválida! Digite 'A' para adicionar ou 'D' para sair.")

iniciar_sistema()