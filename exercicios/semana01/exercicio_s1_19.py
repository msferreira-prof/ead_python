# entrada de dados
print (f"Informe um volume em litros: ")
vL = float(input())
# processamento
vM3 = vL / 1000
# saida de dados
print("%.2f litros equivale a %.3f metros cubicos" % (vL, vM3))