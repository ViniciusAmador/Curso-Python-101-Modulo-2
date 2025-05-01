#Exercício 2 do curso com algoritmo e busca binária 
def busca_binaria(lista, alvo): #Definição de parâmetros de busca
    inicio = 0 #índice de início da busca
    fim = len(lista) - 1 #índice do final da busca # ambos definidos para trabalhar o loop while

    while inicio <= fim: # definição de particionamento da estrutura de dados
        meio = (inicio + fim) // 2 # exatamente o meio da lista
        if lista[meio] == alvo:
            return f"{alvo} foi encontrado."
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return f"{alvo} não foi encontrado."

# Exemplo de uso
numeros = [5, 10, 15, 20, 25, 30, 35]
print(busca_binaria(numeros, 25))
print(busca_binaria(numeros, 8))
