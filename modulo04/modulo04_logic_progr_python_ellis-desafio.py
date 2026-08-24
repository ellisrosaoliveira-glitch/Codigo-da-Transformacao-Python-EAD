# PARTE 4 - CONJUNTOS

python = {"Ana", "Carlos", "Julia", "Pedro"}
html = {"Julia", "Pedro", "Mariana", "Lucas"}

print("Alunos de Python:")
print(python)

print("\nAlunos de HTML:")
print(html)

# União
uniao = python | html
print("\nUnião:")
print(uniao)

# Interseção
intersecao = python & html
print("\nInterseção:")
print(intersecao)

# Diferença
diferenca = python - html
print("\nAlunos que fazem apenas Python:")
print(diferenca)

# Diferença inversa
diferenca2 = html - python
print("\nAlunos que fazem apenas HTML:")
print(diferenca2)


# ======================================
# DESAFIO FINAL
# ======================================

# Lista de alunos
alunos = ["Ana", "Carlos", "Julia", "Pedro", "Mariana"]

# Tupla de cursos
cursos = ("Python", "HTML", "CSS", "JavaScript")

# Dicionário com informações
cadastro = {
    "nome": "Ana",
    "idade": 16,
    "curso": "Python",
    "nota": 9.5
}

# Conjuntos
python_alunos = {"Ana", "Carlos", "Julia"}
html_alunos = {"Julia", "Pedro", "Mariana"}

print("\n========== DESAFIO ==========")

print("\nLista de alunos:")
print(alunos)

print("\nCursos disponíveis:")
print(cursos)

print("\nCadastro:")
for chave, valor in cadastro.items():
    print(chave, ":", valor)

print("\nTodos os alunos dos dois cursos:")
print(python_alunos | html_alunos)

print("\nAlunos que fazem os dois cursos:")
print(python_alunos & html_alunos)

print("\nAlunos que fazem somente Python:")
print(python_alunos - html_alunos)

print("\nQuantidade total de alunos cadastrados:",
      len(alunos))

print("\n==============================")
print("Fim do desafio!")