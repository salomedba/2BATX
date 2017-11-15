# -*- coding: utf-8 -*-
def bisiesto():
	if fecha % 400 == 0 or (fecha % 100 != 0 and fecha % 4 == 0):
		print "El any", fecha, "és un any bisiesto."
	else:
		print "El any", fecha, " no és un any bisiesto."
	return
    
print("Comprobador d'anys bisiestos")
fecha = int(input("Escriu un any i te diré si és bisiesto: "))
bisiesto ()

