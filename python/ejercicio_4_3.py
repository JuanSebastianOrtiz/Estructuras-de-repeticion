# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# programa que  resuelvo ecuacion de primer grado de la forma ax + b = 0 
	# version 1.2
	# 2/03/2023
	# programado por:Juan sebastian ortiz
	# definicion de variables
	a = float()
	b = float()
	x = float()
	# inicializacion de lasvariables
	a = 0.0
	b = 0.0
	x = 0.0
	# captura  de datos
	print("recordar que se trata de una ecuacion de primer grado de la forma  ax + b = 0")
	print("cual es el valor de a")
	a = float(input())
	print("Cual es el valor de b ")
	b = float(input())
	# operaciones aritmeticas
	x = (-b)/a
	print("el resultado de la ecuacion es: ",x)

