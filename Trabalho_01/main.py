def converte_matriz(L, v):
    matriz = [[0 for _ in range(v)] for _ in range(v)]
    return matriz



L = []
M = []
T = []
with open('example.txt') as arquivo:
    for linha in arquivo:
        L.append(linha.strip().split())

for i in range(0, len(L)):
    for j in range(0, len(L[i])):
        L[i][j] = int(L[i][j])

vertices = L[0][0]
arestas = L[0][1]


for i in range(1, len(L)):
    M.append(L[i])

for i in range(len(M)):
    T.append(M[i][0])

#print(vertices)
#print(arestas)
print(M)
print(converte_matriz(M, vertices))