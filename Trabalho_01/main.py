
with open('example.txt') as arquivo:
    M = {}
    for linha in arquivo:
        u, v = map(int, linha.split())
        if u not in M:
            M[u] = [v]
        else:
            M[u].append(v)


print(M)