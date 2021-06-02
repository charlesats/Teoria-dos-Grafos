
def posicao_elemento(lista, elemento):
    pos = -1
    for i in range(0, len(lista)):
        if elemento == lista[i]:
            pos = i

    return pos


Vet = [15, 56, 69, 54, 48, 48, 2, 1, 0]
num = int(input("Digite um numero: "))
resp = posicao_elemento(Vet, num)
print("Posicao: ", resp)
