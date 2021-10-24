# tuplas sao imutaveis
# declaracao: ()

tupla = (1, 2, 3, 4, 5, 6)
print(type(tupla))
print(tupla)

# definir uma tupla com apenas um elemento (utilizar a virgula apos o valor)
tupla2 = (4,)
print(type(tupla))
print(tupla2)
print(len(tupla2))

# desempacotar tuplas
tupla4 = ('Curso de Python', 'Para os melhores professores')
print(tupla4)
curso, elogio = (tupla4)
print(curso)
print(elogio)

print('Tupla4: %s' % (tupla4,) )
print(f'Tupla {tupla4}')
