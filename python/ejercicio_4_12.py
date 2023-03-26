

if __name__ == '__main__':
	# programa   que dice que dia de la semana es segun el dia del mes
	# version 1.0 
	# 28/02/2023
	# programado por:Juan sebastian ortiz
	
	# definicion de variables
	d = int()
	# inicializacion variable
	d = 0
	# lectura de datos
	print("que dia del mes es ")
	d = int(input())
	# condicionales e inpresion de resultados
	if d==1 or d==8 or d==15 or d==22:
		print("es el dia lunes ")
	elif d==2 or d==9 or d==16 or d==23:
		print("es el dia martes ")
	elif d==3 or d==10 or d==17 or d==24:
		print("es el dia miercoles ")
	elif d==4 or d==11 or d==18 or d==25:  #segun el valor digitado en la variable d se imprimira el resultado que satisface el valor escrito en d
		print("es el dia jueves")
	elif d==5 or d==12 or d==19 or d==26:
		print("es el dia viernes")
	elif d==6 or d==13 or d==20 or d==27:
		print("es el dia sabado")
	elif d==7 or d==14 or d==21 or d==28:
		print("es el dia Domingo ")
	else:
		print("no es el mes de febrero ")

