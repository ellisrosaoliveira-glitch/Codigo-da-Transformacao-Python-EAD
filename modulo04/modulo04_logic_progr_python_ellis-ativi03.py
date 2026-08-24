# PARTE 3 - DICIONÁRIOS

aluno = {
    "nome": "Ellis",
    "idade": 16,
    "curso": "Programação",
    "cidade": "São Paulo",
    "nota": 9.5
}

print("Informações do aluno:")
print(aluno)

# Acessando valores
print("\nNome:", aluno["nome"])
print("Idade:", aluno["idade"])
print("Curso:", aluno["curso"])
print("Nota:", aluno["nota"])

# Alterando valores
aluno["idade"] = 17
aluno["nota"] = 10

# Adicionando uma nova informação
aluno["escola"] = "Escola Técnica"

print("\nDicionário atualizado:")
print(aluno)

# Removendo uma informação
del aluno["cidade"]

print("\nDepois de remover a cidade:")
print(aluno)

# Mostrando apenas as chaves
print("\nChaves:")
print(aluno.keys())

# Mostrando apenas os valores
print("\nValores:")
print(aluno.values())

# Mostrando chave e valor
print("\nInformações:")
for chave, valor in aluno.items():
    print(chave, ":", valor)

# Verificando se existe uma chave
if "curso" in aluno:
    print("\nA chave 'curso' existe!")