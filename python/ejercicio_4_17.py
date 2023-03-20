# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).

from math import sqrt

if __name__ == '__main__':
	# programa que  despeja una ecuacion de segundo grado 
	# version 1.0
	# 2/03/2023
	# programado por:Juan sebastian ortiz
	# declaracion de las variables
	a = float()
	b = float()
	c = float()
	d = float()
	x1 = float()
	x2 = float()
	r = float()
	i = float()
	a = 0.0
	b = 0.0
	c = 0.0
	x1 = 0.0
	x2 = 0.0
	r = 0.0
	i = 0.0
	# captura  de datos
	print("deme los coeficiente")
	a = float(input())
	b = float(input())
	c = float(input())
	# condicionales y impresion de resultados
	if a==0:
		print("No es una ecuacion de segundo grado")
	else:
		d = b*b-4*a*c
		if d==0:
			x1 = -b/(2*a)
			x2 = x1
		else:
			if d>0:
				x1 = (-b+sqrt(d))/(2*a)
				x2 = (-b-sqrt(d))/(2*a)
				print(x1,x2)
			else:
				r = (-b)/(2*a)
				i = sqrt(abs(d))/(2*a)
				print(r,"+",i,"i")
				print(r,"-",i,"i")
	# lectura de datos

