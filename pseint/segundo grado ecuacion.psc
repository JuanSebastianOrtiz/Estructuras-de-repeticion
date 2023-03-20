Algoritmo ejercicio_3_17
	// programa que  despeja una ecuacion de segundo grado 
	//version 1.0
	//2/03/2023
	// programado por:Juan sebastian ortiz
	//declaracion de las variables
	definir a,b,c,d,x1,x2,r,i como reales
        a=0.0
        b=0.0
        c=0.0
        x1=0.0
        x2=0.0
        r=0.0
        i=0.0
//captura  de datos
	escribir "deme los coeficiente"
	leer a,b,c
//condicionales y impresion de resultados
	si a = 0 entonces
		escribir "No es una ecuacion de segundo grado"
	sino 
		d = b *b-4*a*c
		si d = 0 Entonces
			x1 = -b/(2*a)
			x2=x1
		sino
		si d > 0 Entonces
			x1 = (-b + rc(d))/(2*a)
			x2 = (-b - rc(d))/(2*a)
			escribir x1 , x2
		sino
			r = (-b)/(2*a)
			i = rc(abs(d))/(2*a)
			escribir r, "+", i ,"i"
			escribir r, "-",i,"i"
		FinSi
	finsi
FinSi
	
   //lectura de datos
	
FinAlgoritmo
