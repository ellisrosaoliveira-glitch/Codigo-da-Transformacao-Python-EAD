# PARTE 2 - TUPLAS

materias = ("Python", "HTML", "CSS", "JavaScript", "Banco de Dados")

print("Matérias:")
print(materias)

# Acessando elementos
print("\nPrimeira matéria:", materias[0])
print("Segunda matéria:", materias[1])
print("Última matéria:", materias[-1])

# Quantidade de elementos
print("\nQuantidade de matérias:", len(materias))

# Verificando se uma matéria existe
if "Python" in materias:
    print("\nPython está na tupla!")

# Percorrendo a tupla
print("\nTodas as matérias:")
for materia in materias:
    print("-", materia)

# Contando quantas vezes um valor aparece
print("\nQuantidade de Python:", materias.count("Python"))

# Descobrindo a posição
print("Posição do CSS:", materias.index("CSS"))

# As tuplas não podem ser alteradas
# materias[0] = "PHP"  # Isso causaria erro