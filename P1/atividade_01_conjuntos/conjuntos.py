# ==================================================
# PORTFÓLIO DE PROGRAMAÇÃO MATEMÁTICA
# Disciplina: Estruturas Matemáticas para Computação
# Atividade 1 - Teoria dos Conjuntos
# ==================================================
nome = input("Nome: ")
matricula = input("Matrícula: ")
turno = input("Turno: ")

print("\n==============================================")
print("PORTFÓLIO DE PROGRAMAÇÃO MATEMÁTICA")
print("==============================================")
print("Aluno:", nome)
print("Matrícula:", matricula)
print("Disciplina: Estruturas Matemáticas para Computação")
print("Turno:", turno)
print("==============================================")

conjunto_a = input("Digite os elementos do conjunto A separados por espaços: ")

elementos_a = conjunto_a.split()

numeros_a = []

for elemento in elementos_a:
    numero = int(elemento)
    numeros_a.append(numero)

conjunto_a = set(numeros_a)

# Entrada do conjunto B
conjunto_b = input("Digite os elementos do conjunto B separados por espaços: ")

elementos_b = conjunto_b.split()

numeros_b = []

for elemento in elementos_b:
    numero = int(elemento)
    numeros_b.append(numero)

conjunto_b = set(numeros_b)

# APRESENTAÇÃO DOS CONJUNTOS
print("TEORIA DOS CONJUNTOS")
print("Conjunto A:", conjunto_a)
print("Conjunto B:", conjunto_b)

# 1. UNIÃO A ∪ B 
uniao = set()

for elemento in conjunto_a:
    uniao.add(elemento)

for elemento in conjunto_b:
    uniao.add(elemento)

print("\nUnião A ∪ B:", uniao)

# 2. INTERSEÇÃO A ∩ B
intersecao = set()

for elemento in conjunto_a:
    if elemento in conjunto_b:
        intersecao.add(elemento)

print("Interseção A ∩ B:", intersecao)

# 3. DIFERENÇAS
diferenca_a_b = set()

for elemento in conjunto_a:
    if elemento not in conjunto_b:
        diferenca_a_b.add(elemento)

diferenca_b_a = set()

for elemento in conjunto_b:
    if elemento not in conjunto_a:
        diferenca_b_a.add(elemento)

print("Diferença A - B:", diferenca_a_b)
print("   Diferença B - A:", diferenca_b_a)

# 4. CARDINALIDADES
cardinalidade_a = 0

for elemento in conjunto_a:
    cardinalidade_a = cardinalidade_a + 1

cardinalidade_b = 0

for elemento in conjunto_b:
    cardinalidade_b = cardinalidade_b + 1

cardinalidade_uniao = 0

for elemento in uniao:
    cardinalidade_uniao = cardinalidade_uniao + 1

cardinalidade_intersecao = 0

for elemento in intersecao:
    cardinalidade_intersecao = cardinalidade_intersecao + 1

print("\nCardinalidades:")
print("   |A| =", cardinalidade_a)
print("   |B| =", cardinalidade_b)
print("   |A ∪ B| =", cardinalidade_uniao)
print("   |A ∩ B| =", cardinalidade_intersecao)

# 5. CONJUNTO DAS PARTES DE A
partes_a = [set()]

for elemento in conjunto_a:

    novas_partes = []

    for parte in partes_a:
        nova_parte = set(parte)
        nova_parte.add(elemento)
        novas_partes.append(nova_parte)

    for nova_parte in novas_partes:
        partes_a.append(nova_parte)

print("\nConjunto das partes de A:")
print("Quantidade de subconjuntos:", end=" ")

quantidade_a = 0

for parte in partes_a:
    quantidade_a = quantidade_a + 1

print(quantidade_a)

print("Subconjuntos de A:")

contador = 0

for parte in partes_a:
    print(parte)
    contador = contador + 1

# CONJUNTO DAS PARTES DE B
partes_b = [set()]

for elemento in conjunto_b:

    novas_partes = []

    for parte in partes_b:
        nova_parte = set(parte)
        nova_parte.add(elemento)
        novas_partes.append(nova_parte)

    for nova_parte in novas_partes:
        partes_b.append(nova_parte)

print("\nConjunto das partes de B:")
print("Quantidade de subconjuntos:", end=" ")

quantidade_b = 0

for parte in partes_b:
    quantidade_b = quantidade_b + 1

print(quantidade_b)

print("Subconjuntos de B:")

contador = 0

for parte in partes_b:
    print(parte)
    contador = contador + 1

# CARDINALIDADE DOS CONJUNTOS DAS PARTES
print("\nCardinalidade dos conjuntos das partes:")
print(" |P(A)| =", quantidade_a)
print(" |P(B)| =", quantidade_b)

# EXEMPLO DE PARTIÇÃO DE A
primeira_parte = set()
segunda_parte = set()

contador = 0

for elemento in conjunto_a:

    if contador % 2 == 0:
        primeira_parte.add(elemento)
    else:
        segunda_parte.add(elemento)

    contador = contador + 1

print("\nExemplo de partição de A:")

print("   Parte 1:", primeira_parte)
print("   Parte 2:", segunda_parte)

# PRODUTO CARTESIANO A × B
produto_cartesiano = []

for elemento_a in conjunto_a:

    for elemento_b in conjunto_b:

        par = (elemento_a, elemento_b)
        produto_cartesiano.append(par)

print("\nProduto cartesiano A × B:")
print(produto_cartesiano)

# INCLUSÃO
a_esta_contido_em_b = True

for elemento in conjunto_a:

    if elemento not in conjunto_b:
        a_esta_contido_em_b = False

b_esta_contido_em_a = True

for elemento in conjunto_b:

    if elemento not in conjunto_a:
        b_esta_contido_em_a = False

print("\nInclusão:")

if a_esta_contido_em_b:
    print("   A está contido em B: SIM")
else:
    print("   A está contido em B: NÃO")

if b_esta_contido_em_a:
    print("   B está contido em A: SIM")
else:
    print("   B está contido em A: NÃO")