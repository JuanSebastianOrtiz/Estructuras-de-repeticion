# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# programa que define el dia del mes de febrero de febrero es segun el primer dia que escribe el usuario 
	# version 1.0 
	# 28/02/2023
	# programado por:Juan sebastian ortiz
	# definicion de variables
	d = str()
	n = int()
	# inicializacion de las variables 
	d = ""
	n = 0
	# captura de datos
	# escribir el dia de la semana en minusculas 
	print("que dia de la semana fue el primero del mes de febrero ? ")
	d = input()
	# tiene que ser un numero
	print("que dia de el mes quiere averiguar")
	n = int(input())
	if d=="miercoles" or d=="Miercoles":
		# impresion de resultados y condicionales
		if n==1 or n==8 or n==15 or n==22:
			print("es el dia miercoles ")
		elif n==2 or n==9 or n==16 or n==23:
			print("es el dia jueves")
		elif n==3 or n==10 or n==17 or n==24:         # segun el valor que se digite en la variable d se imprimira el resultado que satisfaga el numero digitado en la variable
			print("es el dia viernes ")
		elif n==4 or n==11 or n==18 or n==25:
			print("es el dia sabado")
		elif n==5 or n==12 or n==19 or n==26:
			print("es el dia domingo ")
		elif n==6 or n==13 or n==20 or n==27:
			print("es el dia lunes")
		elif n==7 or n==14 or n==21 or n==28:
			print("es el dia martes ")
		else:
			print("no es el mes de febrero ")
	else:
		print("el dia escrito no perteneces al dia 1 del mes de febrero  ")

