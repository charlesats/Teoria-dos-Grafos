def media(lista):
    soma = 0

    for i in range(0, len(lista)):
        soma += lista[i]

    media_elementos = soma / len(lista)

    return media_elementos


Lista = [10, 15, 33, 5]
result = media(Lista)
print(result)
