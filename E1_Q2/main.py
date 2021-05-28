n = int(input("Digite o tamanho do quadrado: "))


largura = n
altura = n

print('*' * largura)

for _ in range(altura-2):
    print('*' + ' ' * (largura-2) + '*')

print('*' * largura)
