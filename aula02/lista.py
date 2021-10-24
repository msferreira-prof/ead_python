# listas (array)
# listas sao mutaveis
# declaracao: []
lista1 = [1, 2, 3, 4, 5]
lista2 = ['s', 'e', 'n', 'a', 'c']
lista3 = []
lista4 = list(range(11))
lista5 = ['Senac ARRJ']
lista6 = [1, 1, 1, 1, 5]

# print 
print(type(lista1))
print('lista1: %s' % lista1)
print('lista2: %s' % lista2)
print('lista3: %s' % lista3)
print('lista4: %s' % lista4)
print('lista5: %s' % lista5)
print('\n')

# procurando um valor no array
num = 18
if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')
print('\n')

# procurando uma string no array
if 'e' in lista2:
    print(f'Encontrei a letra e')
else:
    print(f'Não encontrei a letra e')
print('\n')

# sort em uma lista
lista2.sort()
print('lista2: %s' % lista2)
print('\n')

# reverso em uma lista
lista2.reverse()
print('lista2: %s' % lista2)
print('\n')

# contar ocorrencias de um valor em uma lista
print('Qtd letra "e": %d' % lista2.count('e'))
print('Qtd numero 1: %d' % lista6.count(1))
print('\n')

# incluindo valores na lista
print('Tipo elemento 0 do array: %s' % type(lista4[0]))
print('\n')

lista4.append(11)
lista4.insert(1, 5)
lista4.extend([20, 21, 22])

print('lista4: %s' % lista4)
print('\n')

# array dentro de array
lista3.append(1)
lista3.append([8, 3, 1])
print('lista3: %s' % lista3)
print('\n')

# verificando se um array existe como elemento em outro array
if ([8, 3, 1]) in lista3:
    print('Encontrei o vetor como elemento')
else:
    print('Não encontrei o vetor como elemento')
print('\n')

# inserindo caracteres de uma palavra/frase em um array
lista2.extend('Python')
print('lista2: %s' % lista2)
print('\n')

# concatenando array
print('Concatenando lista1 e lista2: %s' % (lista1 + lista2))
print('\n')

# copiar listas
print('lista6: %s' % lista6)
lista7 = lista6.copy()
# remover o ultimo elemento da lista destino
lista7.pop()
print('lista7: %s' % lista7)
print('\n')

# remover um elemento em um indice
lista7.pop(1)
print('lista7: %s' % lista7)
print('Qtd elementos lista7: %d' % len(lista7))
print('\n')

# remover todos os elementos de uma lista
lista7.clear()
print('Lista7 sem elementos: %s' % lista7)
print('\n')

# repetir os elementos de um array 3 vexes e armazar no proprio array
print('lista1: %s' % lista1)
lista8 = lista1 * 3
print('lista8: %s' % lista8)
print('\n')

# gerar lista a partir de string
curso = 'Curso Python Jovem Aprendiz'
print('String: %s' % curso)
curso = curso.split()
print('Array: %s' % curso)
print('\n')

# gerar lista a partir de string com separador
curso1 = 'Curso,Python,Jovem,Aprendiz,'
print('String: %s' % curso1)
curso1 = curso1.split(',')
print('Array: %s' % curso1)
print('\n')

# gerar string a partir de um lista de string
curso = ['Curso', 'Python', 'Jovem', 'Aprendiz']
print('Array: %s' % curso1)
# sem virgula
curso2 = ' '.join(curso)
print('String: %s' % curso2)
# com virgula
curso3 = ', '.join(curso)
print('String: %s' % curso3)
