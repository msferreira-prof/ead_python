#
import math
# entrada de dados
print (f"Informe um angulo em Radianos: ")
anguloR = float(input())
# processamento
anguloG = anguloR * 180 / math.pi
# saida de dados
print("O angulo %.2f em Radianos equivale ao angulo %.2f em Graus " % (anguloR, anguloG))