# -*- coding: utf-8 -*-
def palabras ():
	global lista
	if numero < 1:
		print("¡Imposible!")
	else:
		lista = []
		for i in range(numero):
			print("Dígame la palabra")
			palabra = raw_input()
			lista += [palabra]
	return

numero = int(input("Dígame cuántas palabras tiene la lista: "))
palabras()
print"La lista creada es:", lista

