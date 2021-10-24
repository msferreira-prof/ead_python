# # carrinho
# carrinho = []
# produto = []

# while produto != 'sair':
#     print("Adicione o produto na lista ou 'sair' para sair")
#     produto = input()

#     if produto != 'sair':
#         carrinho.append(produto)

# for produto in carrinho:
#     print(f"Produto inserido no carrinho: {produto}")


cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[0])

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice += 1

# utilizando o enumerate
for indice, cor in enumerate(cores):
    print(indice, cor)

# utilizando o enumerate v2 (lembra um array associativo)
listaEnumerate = list(enumerate(cores))
print("Lista com Enumerate: %s" % listaEnumerate)

