import math

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = b ** 2 - (4*a*c)

if delta < 0:
	print("esta equação não possui raízes reais")
elif delta == 0:
	raiz = (-b + math.sqrt(delta))/(2*a)
	print("a raiz desta equação é",raiz)
else:
	raizx = (-b + math.sqrt(delta))/(2*a)
	raizy = (-b - math.sqrt(delta))/(2*a)
	if raizx <= raizy:
		print("as raízes da equação são",raizx,"e",raizy)
	else:
		print("as raízes da equação são",raizy,"e",raizx)