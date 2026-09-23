# Portfólio de EMC - Parte 1

## Identificação
**Nome:** Felipe Baines de Cicco Lima
**Matrícula:** 2612130051
**Disciplina:** Estruturas Matemáticas para Computação
**Turno:** Matutino

## Atividade 1 - Teoria dos Conjuntos
**Localização do programa:**
P1/atividade_01_conjuntos/conjuntos.py

**Como executar:**
No terminal, dentro da pasta do projeto, execute:
python3 P1/atividade_01_conjuntos/conjuntos.py
O programa solicita os elementos dos conjuntos A e B separados por espaços.

**Exemplo de entrada:**
A = 1 2 3 4
B = 3 4 5 6

**O programa apresenta:**
• união;
• interseção;
• diferenças;
• cardinalidades;
• conjunto das partes;
• cardinalidade dos conjuntos das partes;
• exemplo de partição;
• produto cartesiano;
• inclusão dos conjuntos.

**Exemplo de resultado:**
União A ∪ B: {1, 2, 3, 4, 5, 6}
Interseção A ∩ B: {3, 4}
Diferença A - B: {1, 2}
Diferença B - A: {5, 6}
|A| = 4
|B| = 4
|A ∪ B| = 6
|A ∩ B| = 2
|P(A)| = 16
|P(B)| = 16
A está contido em B: NÃO
B está contido em A: NÃO

## Atividade 2 - Divisibilidade, MDC e MMC
**Localização do programa:**
P1/atividade_02_divisibilidade/divisibilidade.py

**Como executar:**
No terminal, dentro da pasta do projeto, execute:
python3 P1/atividade_02_divisibilidade/divisibilidade.py
O programa solicita dois números inteiros positivos.

**Exemplo de entrada:**
Primeiro número: 48
Segundo número: 18

**O programa apresenta:**
• DIV;
• MOD;
• passo a passo do Algoritmo de Euclides;
• MDC;
• MMC.

**Exemplo de resultado:**
Div = 2
Mod = 12
48 = 18 × 2 + 12
18 = 12 × 1 + 6
12 = 6 × 2 + 0
MDC de Euclides = 6
MMC = 144