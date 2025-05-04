# Exercício dos Slides
# João precisa organizar sua lista de compras para a semana. Siga as instruções abaixo para ajudá-lo a completar essa tarefa:

# 1. Crie uma lista vazia.
# 2. Adicione os itens à lista de compras.
# 3. João percebe que esqueceu de adicionar um item. Coloque-o na segunda posição da lista.
# 4. Exiba a lista de compras completa e mostre qual é o terceiro item na lista.
# 5. João decide que não precisa mais comprar um item. Remova-o da lista.
# 6. Ele também decide retirar o último item da lista.
# 7. Como último ajuste, João substitui o primeiro item da lista por "abacate".
# 8. Mostre a lista atualizada e, em seguida, exiba cada item individualmente.
# 9. Finalmente, organize a lista em ordem alfabética para facilitar a visualização.

# 1. Crie uma lista vazia
lista_compras = []

# 2. Adicione itens à lista de compras
lista_compras.append("banana")
lista_compras.append("maçã")
lista_compras.append("pão")
lista_compras.append("leite")

# 3. João percebe que esqueceu de adicionar um item na segunda posição
lista_compras.insert(1, "café")

# 4. Exiba a lista completa e mostre o terceiro item
print("Lista completa:", lista_compras)
print("Terceiro item:", lista_compras[2])

# 5. João decide remover um item específico
lista_compras.remove("pão")

# 6. Remove o último item da lista
lista_compras.pop()

# 7. Substitui o primeiro item por "abacate"
lista_compras[0] = "abacate"

# 8. Mostra a lista atualizada
print()
print("Lista atualizada:", lista_compras)

# 9. Exibe cada item individualmente
print()
print("Itens da lista:")
for item in lista_compras:
    print("-", item)

# 10. Organiza a lista em ordem alfabética
lista_compras.sort()

print()
print("Lista em ordem alfabética:")
for item in lista_compras:
    print("-", item)
