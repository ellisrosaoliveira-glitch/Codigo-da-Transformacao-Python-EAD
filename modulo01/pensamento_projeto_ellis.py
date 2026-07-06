'''
um bloco de cometario.

projeto hamburgueria:

PO: (como dono do negocio: quero um sistema de vendas para a minha hamburgeria,
para que eu possa controlar as vendas e produtos.)

QA: (como cliente: quero um sistema de vendas para a minha hamburgeria para 
que eu possa comprar meus produtos favoritos de forma facil e rapido.)

Tech: (como programador: quero um sistema de vendas para a minha hamburgeria,
para que eu possa desenvolver um software eficiente e funcional para o negocio.)

Dev: (como programador quero um sistema de vendas para a minha hambuergeria
 para que eu possa implementar as funcionalidades necessarias para atender as 
 necessidades do negocio e dos clientes.)

UX: (como designer de experiencia do usuario: quero um sistema de vendas
 para a minha hambuergeria para que eu possa criar uma interface intuitiva e 
 agradavel para os usuarios, garantindo uma experiencia de compra satisfatoria.)

IA: (como analista de dados: quero um sistema de vendas para a minha hamburgeria,
para que eu possa coletar e analisar os dados de vendas, ajudando a identificar
padrões de consumo e otimizar as estrategias de marketing e estoque.)
#
'''
p1_nome = p2_nome = p3_nome = ""
p1_estoque = p2_estoque = p3_estoque = 0
p1_preco = p2_preco = p3_preco = 0.0
p1_validade = p2_validade = p3_validade = ""
p1_descricao = p2_descricao = p3_descricao = ""

print("\n== Hamburgeria ===")

print("1. Cardapio ")
print("2. Bebidas ")
print("3. Sobremesas ")
print("4. Combos ")
print("5. Pedidos ")
print("6. Fazer Pedidos ")
print("7. Combo Infantil ")
print("8. Forma de Pagamento ")
print("9. Combo do Dia ")
print("0. Sair")
print('-' * 50 + "\n")

while True:
    opcao = input("Digite a opção desejada: ")

    if opcao == '1':
        print('Cadastrando produtos...\n')

        if p1_nome == "":
            p1_nome = input("Digite o nome do produto: ")
            p1_estoque = int(input("Digite a quantidade em estoque: "))
            p1_preco = float(input("Digite o preço do produto: "))
            p1_validade = input("Digite a validade do produto: ")
            p1_descricao = input("Digite a descrição do produto: ")

            print(f"✅ Produto '{p1_nome}' cadastrado na vaga 1!")

        elif p2_nome == "":
            p2_nome = input("Digite o nome do produto: ")
            p2_estoque = int(input("Digite a quantidade em estoque: "))
            p2_preco = float(input("Digite o preço do produto: "))
            p2_validade = input("Digite a validade do produto: ")
            p2_descricao = input("Digite a descrição do produto: ")

            print(f"✅ Produto '{p2_nome}' cadastrado na vaga 2!")

        elif p3_nome == "":
            p3_nome = input("Digite o nome do produto: ")
            p3_estoque = int(input("Digite a quantidade em estoque: "))
            p3_preco = float(input("Digite o preço do produto: "))
            p3_validade = input("Digite a validade do produto: ")
            p3_descricao = input("Digite a descrição do produto: ")

            print(f"✅ Produto '{p3_nome}' cadastrado na vaga 3!")

        else:
            print("❌ Sistema cheio! Limite de 3 produtos atingido.")

    elif opcao == '2':
        print('Listando produtos...')

        if p1_nome == "" and p2_nome == "" and p3_nome == "":
            print('Nenhum produto cadastrado no sistema ainda.')

        else:
            if p1_nome != "":
                print(f"Nome: {p1_nome} | Preço: R$ {p1_preco:.2f} | Estoque: {p1_estoque} unid.")
                print(f"Validade: {p1_validade} | Descrição: {p1_descricao}")
                print('🔥' * 30)

            if p2_nome != "":
                print(f"Nome: {p2_nome} | Preço: R$ {p2_preco:.2f} | Estoque: {p2_estoque} unid.")
                print(f"Validade: {p2_validade} | Descrição: {p2_descricao}")
                print('-' * 30)

            if p3_nome != "":
                print(f"Nome: {p3_nome} | Preço: R$ {p3_preco:.2f} | Estoque: {p3_estoque} unid.")
                print(f"Validade: {p3_validade} | Descrição: {p3_descricao}")
                print('-' * 30)

    elif opcao == '0':
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida. Escolha uma opção válida.")

    print('-' * 50 + "\n")