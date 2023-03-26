 

from math import sqrt

if __name__ == '__main__':
	# programa que calcula el area de cuualquier triangulo  //
	# desarrollador juan sebastian ortiz ibarra //
	# fecha 7/03/2023//
	# version 1.0//
	# definicion de variables
	l1 = float()
	l2 = float()
	l3 = float()
	sp = float()
	area = float()
	# inicializacion de las variables
	l1 = 0.0
	l2 = 0.0
	l3 = 0.0
	sp = 0.0
	area = 0.0
	# captura de datos
	print("escriba el lado 1 ")
	l1 = float(input())
	print("escriba el lado 2 ")
	l2 = float(input())
	print("escriba el lado 3 ")
	l3 = float(input())
	# procesos aritmeticos
	sp = (l1+l2+l3)/2
	area = (sqrt(sp*((sp-l1)*(sp-l2)*(sp-l3))))  # formula de heron utiliza el semiperimetro y funciona para  resolver cualquier tipo de triangulo
	# impresion del resultado
	# se recuerda, se tiene  que saber cuanto miden los 3 lados del triangulo sino no se puede aplicar esta formula
	print("El area del triangulo es: ",area)

