# ======================================================================
# 🚀 Parte 1: Criando e lendo um arquivo
# ======================================================================

# 📋 Passo 1: Criando e escrevendo no arquivo
# O modo "w" cria o arquivo e permite escrever nele.

arquivo = open("clientes.txt", "w", encoding="utf-8")

arquivo.write("Nome: João\n")
arquivo.write("Idade: 18\n")
arquivo.write("Cidade: São Paulo\n")

arquivo.close()

# ======================================================================
# 📋 Passo 2: Abrindo o arquivo para leitura
# O modo "r" permite ler o conteúdo que foi salvo.

arquivo = open("clientes.txt", "r", encoding="utf-8")

conteudo = arquivo.read()

print("--- Dados do Cliente ---")
print(conteudo)

arquivo.close()

# ======================================================================
# 🏁 Fim do Programa
# ======================================================================