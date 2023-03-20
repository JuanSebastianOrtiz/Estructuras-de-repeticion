# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# programa que calcula el salario total de un empleado teniendo en cuenta su salario y horas trabajadas
	# version 1.0 
	# 9/03/2023
	# programado por:Juan sebastian ortiz
	# definicion de variables
	nombre = str()
	ht = int()
	# se recalca que el salario es en euros para que tengan una idea y no pongan salarios de mas d 1000000
	vh = float()
	vhe = float()
	vimp = float()
	sb = float()
	sp = float()
	# inicializacion de las variables
	ht = 0
	vh = 0.0
	vhe = 0.0
	vimp = 0.0
	sb = 0.0
	sp = 0.0
	nombre = ""
	# captura de datos
	print("Cual es su nombre ")
	nombre = input()
	print("Horas trabajadas semanales")
	ht = int(input())
	print("¿cuanto es valor de la hora trabajada?")
	vh = float(input())
	# condicionales y procesos aritmeticos
	if ht<=35:
		sb = ht*vh
	else:
		if ht>35:
			sb = 35*vh
			vhe = (ht+35)*1.5
			sb = sb+vhe
		if sb<=2000:
			print("Salario libre de impuestos ",sb)
		else:
			if sb>2000 and sb<=2220:
				vimp = (sb-2000)*0.20
			else:
				if sb>2220:
					vimp = (sb-2220)*0.30+(220*0.20)
	sp = sb-vimp
	# impresion de resultados 
	print("empleado con nombre: ",nombre)
	print("Numero de horas trabajadas: ",ht," El valor de hora es: ",vh)
	print("Su sueldo base es: ",sb)
	print("impuestos: ",vimp," su sueldo a pagar es: ",sp)

