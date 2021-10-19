# for
faixa = range(0, 11)

print('Digite o número da tabuada ')
numero = int(input())

for n in faixa:
    print("Tabuada %d x %d = %d" % (numero, n, numero*n)) # C like
#  ou
#  print(f"Tabuada {numero} x {n} = {numero * n}")

