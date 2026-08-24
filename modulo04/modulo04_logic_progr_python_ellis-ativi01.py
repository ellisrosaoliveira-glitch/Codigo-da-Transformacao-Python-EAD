# PARTE 1 - LISTAS

alunos = ["Ana", "Carlos", "Julia", "Pedro"]

print("Lista inicial:")
print(alunos)

# Acessando elementos
print("\nPrimeiro aluno:", alunos[0])
print("Último aluno:", alunos[-1])

# Adicionando elementos
alunos.append("Mariana")
alunos.insert(1, "Lucas")

print("\nDepois de adicionar:")
print(alunos)

# Alterando elementos
alunos[0] = "Amanda"

print("\nDepois de alterar:")
print(alunos)

# Removendo elementos
alunos.remove("Pedro")

print("\nDepois de remover Pedro:")
print(alunos)

# Removendo pelo índice
alunos.pop(2)

print("\nDepois de remover pelo índice:")
print(alunos)

# Quantidade de elementos
print("\nQuantidade de alunos:", len(alunos))

# Ordenando a lista
alunos.sort()

print("\nLista organizada:")
print(alunos)

# Verificando se um nome está na lista
if "Lucas" in alunos:
    print("\nLucas está na lista!")
else:
    print("\nLucas não está na lista!")