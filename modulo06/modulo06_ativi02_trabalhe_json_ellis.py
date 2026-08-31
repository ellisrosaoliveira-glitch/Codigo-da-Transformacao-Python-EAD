# ======================================================================
# 🚀 Parte 2: Trabalhando com arquivos JSON
# ======================================================================

import json

# 📋 Passo 1: Criando os dados do cliente
# Vamos utilizar um dicionário para guardar as informações.

cliente = {
    "nome": "Maria",
    "idade": 17,
    "cidade": "São Paulo"
}

# ======================================================================
# 📋 Passo 2: Salvando os dados em um arquivo JSON
# O "w" permite escrever os dados no arquivo.

with open("cliente.json", "w", encoding="utf-8") as arquivo:
    json.dump(cliente, arquivo, indent=4, ensure_ascii=False)

print("✅ Cliente salvo com sucesso!")

# ======================================================================
# 📋 Passo 3: Lendo os dados do arquivo JSON

with open("cliente.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

print("\n--- Dados do Cliente ---")
print(f"Nome: {dados['nome']}")
print(f"Idade: {dados['idade']}")
print(f"Cidade: {dados['cidade']}")

# ======================================================================
# 🏁 Fim do Programa
# ======================================================================