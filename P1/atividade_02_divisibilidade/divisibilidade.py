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
print("Digite dois números inteiros")

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

# Verificar se os números são positivos
while numero1 <= 0 or numero2 <= 0:

    print("Erro! Os números devem ser inteiros positivos.")

    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))

# Calcular a divisão e o resto da divisão
div = numero1 // numero2
resto = numero1 % numero2

print(f"Div = {div}")
print(f"Mod = {resto}")

numero1_original = numero1
numero2_original = numero2

# Calcular o MDC de Euclides e apresentar o passo a passo
while numero2 != 0:

    div = numero1 // numero2
    resto = numero1 % numero2

    print(f"{numero1} = {numero2} × {div} + {resto}")

    numero1 = numero2
    numero2 = resto

print(f"MDC ({numero1_original} e {numero2_original}) = {numero1}")

# Calcular o MMC
mmc = (numero1_original * numero2_original) // numero1

print(f"MMC = {mmc}")