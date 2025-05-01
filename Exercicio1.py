#Exercicio numero 1 com listas, algoritmo de busca linear para percorrer uma lista
def busca_linear(nomes, alvo): #definir parâmetros lista e alvo
    for nome in nomes: # loop for para busca de item em lista
        if nome == alvo:
            return f"{alvo} foi encontrado." # f-string com nome do alvo
    return f"{alvo} não foi encontrado." #exceção

nomes = ["Ana", "Bruno", "Carlos", "Daniela"] #criar uma lista com nome dos alunos
print(busca_linear(nomes, "Carlos")) #chamar a lista e depois o nome para comparar nome == alvo pela função busca_linear 
print(busca_linear(nomes, "Fernanda"))
