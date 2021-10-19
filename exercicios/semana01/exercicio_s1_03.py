
soma = 0
for i in range(0, 3):
    #entrada de dados
    print (f"Digite o {i+1}o. numero inteiro: ")
    numero = int(input())
    # processamento
    soma = soma + numero

# saida de dados
print(f"Soma dos numeros informados: {soma}")