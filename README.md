<p align="center">
  <img src="https://img.shields.io/badge/versão-1.0-blue" alt="Versão">
  <img src="https://img.shields.io/badge/status-em%20desenvolvimento-yellow" alt="Status do Curso">
  <img src="https://img.shields.io/badge/feito%20com-Python%203.x-blue?logo=python&logoColor=white" alt="Feito com Python">
  <img src="https://img.shields.io/badge/licença-MIT-green" alt="Licença">
</p>

<p align="center">
  <img src="assets/banner_python101.png" width="400" alt="Python101 Logo">
</p>

# 🐍 python101
## Professor, Dr. Vinícius Costa Amador
### ✨ Seja bem-vindo(a)! Este material foi preparado com carinho para acolher você no curso de Python do ciclo básico de programação...

# Módulo 2: Estruturas de Dados e Coleções | Data Structures and Collections | 数据结构和集合
## 📁 Sumário | Summary | 目录

### 1. Listas (Listas Mutáveis) | Lists (Mutable Sequences) | 列表（可变序列）
- Criação e Inicialização | Creating and Initializing | 创建与初始化
- Acesso a Elementos | Accessing Elements | 访问元素
- Operações Básicas | Basic Operations | 基本操作
- Iteração com Listas | Looping Through Lists | 遍历列表
- Listas Aninhadas | Nested Lists | 嵌套列表
- Vetores e Matrizes | Vectors and Matrices | 向量和矩阵

### 2. Dicionários (Mapeamento de Pares Chave-Valor) | Dictionaries (Key-Value Mappings) | 字典（键值映射）
- Criação de Dicionários | Creating Dictionaries | 创建字典
- Acesso e Modificação | Access and Modification | 访问与修改
- Métodos Comuns | Common Methods | 常用方法
- Iteração com Dicionários | Looping Through Dictionaries | 遍历字典

### 3. Tuplas (Listas Imutáveis) | Tuples (Immutable Sequences) | 元组（不可变序列）
- Criação e Características | Creation and Properties | 创建与特性
- Acesso a Elementos | Accessing Elements | 访问元素
- Imutabilidade e Vantagens | Immutability and Benefits | 不可变性与优点
- Desempacotamento de Tuplas | Tuple Unpacking | 元组解包

### 4. Exercícios: Algoritmos de Busca | Search Algorithms Exercises | 查找算法练习
- Pesquisa Linear | Linear Search | 线性查找
- Pesquisa Binária | Binary Search | 二分查找

---

### 1. Listas (Listas Mutáveis) | Lists (Mutable Sequences) | 列表（可变序列）

Listas são estruturas de dados ordenadas e mutáveis. Elas permitem armazenar múltiplos valores em uma única variável, sendo possível modificar, adicionar ou remover elementos após a criação.
Lists are ordered and mutable data structures. They allow storing multiple values in a single variable, with the ability to modify, add, or remove elements after creation.
列表是有序且可变的数据结构。它们允许在一个变量中存储多个值，并在创建后修改、添加或删除元素。

🔹 Criação e Inicialização | Creating and Initializing | 创建与初始化
```bash
frutas = ["maçã", "banana", "laranja"]
```
Listas são estruturas dinâmicas que armazenam sequências ordenadas de elementos. Podem conter dados de diferentes tipos.

🔹 Acesso a Elementos | Accessing Elements | 访问元素
```bash
print(frutas[0])  # maçã
```
Indexação começa em 0.
É possível usar índices negativos para acessar de trás para frente.

🔹 Operações Básicas | Basic Operations | 基本操作
```bash
frutas.append("uva")          # Adiciona ao final
frutas.insert(1, "melancia")  # Insere na posição 1
frutas.extend(["abacaxi", "kiwi"])  # Adiciona múltiplos elementos
print(frutas.index("laranja"))       # Retorna o índice de um elemento
frutas.pop()                 # Remove o último elemento
frutas.remove("banana")      # Remove a primeira ocorrência
print(len(frutas))           # Retorna o tamanho
```
- `append()`: adiciona um elemento ao final da lista.
- `insert()`: insere um elemento em uma posição específica.
- `extend()`: adiciona múltiplos elementos ao final.
- `index()`: retorna o índice da primeira ocorrência de um elemento.
- `pop()`: remove e retorna o último item (ou o item de um índice específico).
- `remove()`: remove a primeira ocorrência de um valor.
- `len()`: retorna o número de elementos na lista.

Essas operações tornam as listas extremamente versáteis para organizar, modificar e consultar dados dinâmicos.

🔹 Iteração com Listas | Looping Through Lists | 遍历列表
```bash
for fruta in frutas:
    print(fruta)
```
Útil para acessar todos os elementos.
Pode usar `range()` para acessar por índice.

🔹 Listas Aninhadas | Nested Lists | 嵌套列表
```bash
lista_aninhada = [[1, 2], [3, 4]]
print(lista_aninhada[1][0])  # 3
```
Listas dentro de listas.
Usadas para representar dados bidimensionais.

🔹 Vetores e Matrizes | Vectors and Matrices | 向量和矩阵
🔹 Vetores | Vectors | 向量
Vetores são listas unidimensionais usadas para representar sequências de dados.
```bash
notas = [7.5, 8.0, 9.2, 6.5]
print(notas[0])  # Acessa o primeiro elemento
```
🌐 Aplicabilidade: vetores são úteis para armazenar dados simples como notas, temperaturas, pontuações, etc.
📅 Característica principal: acesso direto por índice.

🔹 Matrizes | Matrices | 矩阵
Matrizes são listas de listas (ou tabelas 2D) que armazenam dados em linhas e colunas.
```bash
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matriz[0][1])  # Acessa o elemento da primeira linha, segunda coluna
```
🌐 Aplicabilidade: úteis para representar tabelas, grades de jogos, pixels de imagem, dados de sensores, etc.

📌 Percorrendo com for:
```bash
for linha in matriz:
    for elemento in linha:
        print(elemento, end=' ')
    print()
```
💡 Dica: embora Python não tenha matrizes nativas como outras linguagens, bibliotecas como NumPy oferecem ferramentas mais avançadas para operações matriciais.

### Boas práticas com Listas | Best Practices with Lists | 列表使用规范
✅ O que fazer:
- Aproveite a mutabilidade para adicionar ou remover elementos dinamicamente
- Utilize in para verificar se um valor está presente antes de acessá-lo.
❌ O que evitar:
- Não acesse índices fora do intervalo da lista — isso causará `IndexError`.
- Não misture tipos incompatíveis que dificultem o tratamento (ex.: strings e números sem contexto).

### 2. Dicionários | Dictionaries | 字典

Dicionários são coleções não ordenadas de pares chave-valor, ideais para associar identificadores a dados. Eles permitem acesso rápido aos valores por meio de suas chaves.
Dictionaries are unordered collections of key-value pairs, ideal for mapping identifiers to data. They allow fast access to values via their keys.
字典是无序的键值对集合，适合将标识符与数据关联起来，可通过键快速访问对应的值。

🔹 Criação de Dicionários | Creating Dictionaries | 创建字典
```bash
aluno = {"nome": "Ana", "idade": 21, "curso": "Python"}
```
As chaves devem ser únicas e de tipos imutáveis (string, int, float ou tuple).

🔹 Acesso e Modificação | Access and Modification | 访问与修改
```bash
print(aluno["nome"])            # Ana
aluno["idade"] = 22               # Modifica valor existente
aluno["email"] = "ana@email.com"  # Adiciona nova chave-valor
```
A tentativa de acessar uma chave inexistente diretamente gera erro.

Use `get()` para evitar erros:
```bash
print(aluno.get("telefone", "Não informado"))
```
🔹 Métodos Comuns | Common Methods | 常用方法
```bash
print(aluno.keys())    # Todas as chaves
print(aluno.values())  # Todos os valores
print(aluno.items())   # Pares chave-valor
aluno.pop("curso")     # Remove a chave "curso"
aluno.setdefault("telefone", "Não informado")  # Adiciona se não existir
aluno.update({"idade": 23})  # Atualiza um ou mais pares
aluno.clear()  # Remove todos os itens
```
🔹 Iteração com Dicionários | Looping Through Dictionaries | 遍历字典
```bash
for chave, valor in aluno.items():
    print(chave, ":", valor)
```
Útil para visualizar todos os dados armazenados.

### Boas práticas com Dicionários | Best Practices with Dictionaries | 字典使用规范
✅ O que fazer:
- Verifique se uma chave existe com in antes de acessá-la.
- Use `get()` para acessar chaves opcionais de forma segura.
- Utilize nomes de chave consistentes e descritivos.
❌ O que evitar:
- Evite sobrescrever valores importantes sem necessidade.
- Não itere diretamente sobre dict se precisar das chaves e valores — prefira `items()`.

### 3. Tuplas | Tuples | 元组

Tuplas são estruturas ordenadas e imutáveis. São ideais para armazenar dados que não devem ser alterados e que precisam de acesso rápido por índice.
Tuples are ordered and immutable structures. They are ideal for storing data that should not be changed and need fast access by index.
元组是有序且不可变的数据结构，适用于存储不应更改的数据，并支持通过索引快速访问。

🔹 Criação e Características | Creation and Properties | 创建与特性
```bash
tupla = (10, 20, 30)
tupla_simples = (5,)  # Tupla com um único elemento
```
Tuplas são criadas com parênteses.
A imutabilidade significa que os dados não podem ser modificados após a criação.

🔹 Acesso a Elementos | Accessing Elements | 访问元素
```bash
print(tupla[1])  # Acessa o segundo elemento (20)
```
Indexação como nas listas, a partir de 0.

🔹 Imutabilidade e Vantagens | Immutability and Benefits | 不可变性与优点

Garantem integridade dos dados.
São mais eficientes que listas em acesso.
Podem ser usadas como chaves de dicionários (por serem imutáveis).

🔹 Desempacotamento de Tuplas | Tuple Unpacking | 元组解包
```bash
nome, idade, curso = ("Ana", 30, "Python")
print(nome)
print(idade)
print(curso)
```
Permite extrair os valores diretamente para variáveis.

### Boas práticas com Tuplas | Best Practices with Tuples | 元组使用规范
✅ O que fazer:
- Use tuplas quando os dados não devem ser alterados.
- Empregue tuplas como chaves de dicionários, se necessário.
- Desempacote tuplas para clareza e legibilidade.

❌ O que evitar:
- Não tente modificar elementos: isso resultará em TypeError.
- Evite usar tuplas para dados que mudam com frequência.

### 4. Exercícios: Algoritmos de Busca | Search Algorithms Exercises | 查找算法练习

🔍 Pesquisa Linear | Linear Search | 线性查找
💡 Princípio:
A pesquisa linear percorre todos os elementos de uma lista até encontrar o valor desejado ou até o fim da lista.
🧠 Complexidade:
Tempo: O(n) — Cresce linearmente com o número de elementos.
Ideal para listas desordenadas ou curtas.

📌 Exemplo:
```bash
valores = [10, 20, 30, 40, 50]
alvo = 30
encontrado = False

for valor in valores:
    if valor == alvo:
        encontrado = True
        break

if encontrado:
    print("Valor encontrado!")
else:
    print("Valor não encontrado.")
```
🧪 Exercício:

Implemente uma função que receba uma lista de nomes e um nome alvo, e diga se o nome está presente ou não usando busca linear.

🔎 Pesquisa Binária | Binary Search | 二分查找

💡 Princípio:
A pesquisa binária divide uma lista ordenada ao meio a cada passo, reduzindo drasticamente o número de comparações.
🧠 Complexidade:
Tempo: O(log n) — Cresce logaritmicamente com o número de elementos.
Necessita que a lista esteja ordenada.

📌 Exemplo:
```bash
def busca_binaria(lista, alvo):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == alvo:
            return True
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return False

numeros = [10, 20, 30, 40, 50, 60, 70]
print(busca_binaria(numeros, 50))  # True
```
🧪 Exercício:
Crie uma função que verifique se um número está presente em uma lista ordenada usando busca binária.

🧠 Conceito de Complexidade de Algoritmos | Algorithm Complexity | 算法复杂度
A complexidade de um algoritmo expressa quanto tempo (ou memória) ele consome à medida que a entrada cresce.

Tipos comuns:
- O(1): tempo constante (ex: acessar um índice de lista)
- O(n): tempo linear (ex: laço for em uma lista)
- O(log n): tempo logarítmico (ex: busca binária)
- O(n²): tempo quadrático (ex: dois loops aninhados)

📌 Avaliar a complexidade é essencial para escolher o algoritmo mais eficiente para cada situação.
