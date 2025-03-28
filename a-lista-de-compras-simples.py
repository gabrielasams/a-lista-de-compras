def validar_entrada(texto):
    if not texto or texto.isspace():
        return False
    return True

def solicitar_entrada_valida(mensagem):
    while True:
        entrada = input(mensagem)
        if validar_entrada(entrada):
            return entrada.strip().capitalize()
        else:
            print("Esse campo não pode ficar vazio ou conter apenas espaços! Tente novamente.")

def escolher_unidade_medida(dicionario_unidade_medidas):

    print("Escolha uma unidade de medida: ")

    for letra, unidade in dicionario_unidade_medidas.items():
        print(f"{letra} - {unidade}")
    while True:
        try:
            unidade_medida = input("Opção: ").upper()
            if unidade_medida in dicionario_unidade_medidas:
                return dicionario_unidade_medidas[unidade_medida]
            else:
                print("Entrada inválida! Digite uma letra entre A e G.")
        except Exception as e:
            print(f"Erro inesperado: {e}. Tente novamente.")

def adicionar_produto(contador_id, dicionario_unidade_medidas):

    nome = solicitar_entrada_valida("Nome: ")
    unidade = escolher_unidade_medida(dicionario_unidade_medidas)

    while True:
        try:
            quantidade = input("Quantidade: ")
            quantidade = quantidade.replace(",", ".")
            quantidade = float(quantidade)

            if quantidade <= 0:
                print("Digite um valor positivo.")
            else:
                break
        except ValueError:
            print("Entrada inválida! Digite um número válido (ex: 2 ou 1).")
      
    descricao = solicitar_entrada_valida("Descrição: ")

    produto = {
            "id": contador_id,
            "nome": nome,
            "unidade de medida": unidade,
            "quantidade": quantidade,
            "descrição": descricao
            }
    return produto

def lista_de_compras():
    
    dicionario_unidade_medidas = {
                                "A": "Quilograma",
                                "B": "Grama",
                                "C": "Litro",
                                "D": "Mililitro",
                                "E": "Unidade",
                                "F": "Metro",
                                "G": "Centímetro"
                                }
    
    lista_produtos = []
    contador_id = 1

    while True:

        print("\nBem-vinde a Lista de Compras Simples")
        print("A - Adicionar produto")
        print("D - Sair da Lista de Compras Simples")

        opcao = input("Escolha uma opção: ").upper()

        if opcao == 'D':
            print("Obrigada por utilizar a Lista de Compras Simples!")
            break
        
        if opcao not in ['A', 'B', 'C', 'D']:
            print("Opção inválida! Tente novamente.")
            continue

        elif opcao == 'A':
            produto = adicionar_produto(contador_id, dicionario_unidade_medidas)
            lista_produtos.append(produto)
            print(f"Produto '{produto['nome']}' adicionado com sucesso! ID: {produto['id']}")
            contador_id += 1

lista_de_compras()
