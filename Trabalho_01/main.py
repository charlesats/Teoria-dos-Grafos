def converte_matriz(L):
    matriz = [[0 for _ in range(len(L))] for _ in range(len(L))]
    for i in range(len(L)):
        for j in range(len(L[i])):
            matriz[i][L[i][j]] = 1
    return matriz


L = []
with open('example.txt') as arquivo:
    for linha in arquivo:
        L.append(linha.strip().split())

for i in range(0, len(L)):
    for j in range(0, len(L[i])):
        L[i][j] = int(L[i][j])

print(L)

