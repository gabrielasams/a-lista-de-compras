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
    print("A. Adicionar produto")
    print("B. Remover produto ")
    print("C. Pesquisar produto")
    print("D. Sair\n")

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

def remover_produto(produtos):
    if not produtos:
        print("\nNenhum produto cadastrado para remover.\n")
        return produtos
    
    listar_produtos(produtos)
    
    try:
        id_remover = int(input("\nDigite o ID do produto que deseja remover: "))
    except ValueError:
        print("\nID inválido! Digite apenas números.\n")
        return produtos
    
    for i, produto in enumerate(produtos):
        if produto['id'] == id_remover:
            while True:
                confirmacao = input(f"Tem certeza que deseja remover '{produto['nome']}' (ID: {produto['id']})? [S/N]: ").strip().upper()
                
                if confirmacao in ['S', 'SIM']:
                    produto_removido = produtos.pop(i)
                    print(f"\nProduto '{produto_removido['nome']}' removido com sucesso!\n")
                    return produtos
                elif confirmacao in ['N', 'NÃO', 'NAO']:
                    print("\nOperação cancelada.\n")
                    return produtos
                else:
                    print("\nOpção inválida! Digite 'S' para SIM ou 'N' para NÃO.\n")
    
    print("\nNenhum produto encontrado com o ID informado.\n")
    return produtos

def pesquisar_produto(produtos):
    pesquisa = input("\nDigite o nome ou parte do nome do produto: ").strip().lower()
    resultados = []
    
    for produto in produtos:
        if pesquisa in produto['nome'].lower():
            resultados.append(produto)
    
    if not resultados:
        print("\nNenhum produto encontrado com esse termo.\n")
    else:
        print(f"\n{len(resultados)} produto(s) encontrado(s):")
        for produto in resultados:
            print(f"\nID: {produto['id']}")
            print(f"Nome: {produto['nome']}")
            print(f"Quantidade: {produto['quantidade']} {produto['unidade de medida']}")
            print(f"Descrição: {produto['descrição']}")
        print()

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
        
        elif opcao == 'A':
            produto = adicionar_produto(controle_id, dicionario_unidade_medidas)
            lista_produtos.append(produto)
            print(f"\nProduto '{produto['nome']}' adicionado com sucesso! (ID: {produto['id']})")
            controle_id += 1

        elif opcao == 'B':
            lista_produtos = remover_produto(lista_produtos)

        elif opcao == 'C':
            if not lista_produtos:
                print("\nNenhum produto cadastrado para pesquisar.\n")
            else:
                pesquisar_produto(lista_produtos)

        else:
            print("\nOpção inválida!")

iniciar_sistema()