Algoritmo Ejercicio_4_5
	// programa que calcula el salario total de un empleado teniendo en cuenta su salario y horas trabajadas
	//version 1.0 
	//9/03/2023
	// programado por:Juan sebastian ortiz
	//definicion de variables
	Definir Nombre Como Caracter
	definir ht Como Entero
	definir vh,vhe,vimp,sb,sp como real // se recalca que el salario es en euros para que tengan una idea y no pongan salarios de mas d 1000000
	//inicializacion de las variables
	ht = 0
	vh = 0.0
	vhe = 0.0
	vimp = 0.0
	sb = 0.0
	sp = 0.0
      Nombre = ""
	//captura de datos
	escribir "Cual es su nombre "
	leer Nombre
	escribir "Horas trabajadas semanales"
	leer ht
	escribir "¿cuanto es valor de la hora trabajada?"
	leer vh
	//condicionales y procesos aritmeticos
	si  ht <= 35  entonces 
		sb = ht * vh  // se multiplica horas trabajadas por valor de horas si el valor de horas es menor a 35
	sino 
		si ht > 35 
			sb = 35 * vh
			vhe = (ht + 35 ) * 1.5//formula horas trabajadas extras
			sb = sb + vhe
			
		Finsi	
		
		si sb <= 2000
			escribir "Salario libre de impuestos " sb
		sino
			si sb > 2000 y sb <= 2220 entonces // formula impuesto si el sueldo es menor a 2220 euros
				vimp=(sb-2000)*0.20 //si e
			SiNo
				si sb > 2220 Entonces
				vimp = (sb -2220) * 0.30 + (220 * 0.20)// formula en caso que el sueldo sea mayor a 2220
				FinSi
			FinSi
			FinSi
		
		FinSi
		sp = sb - vimp // formula salario total
		//impresion de resultados 
	escribir "empleado con nombre: " Nombre
	escribir "Numero de horas trabajadas: " ht " El valor de hora es: " vh
	escribir "Su sueldo base es: " sb 
	escribir "impuestos: " vimp " su sueldo a pagar es: " sp
FinAlgoritmo
