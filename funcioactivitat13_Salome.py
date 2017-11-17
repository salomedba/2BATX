# -*- coding: utf-8 -*-

def crear (lista):
	print "Dime quants elements té la llista: "
	numero = int(input())
	if numero < 1:
		print("¡Imposible!")
	else:
		for i in range(numero):
			print"Dime l'element ", i+1, ": "
			n = int(input())
			lista += [n]
	print "La lista creada es:", lista

def suma (lista):
	suma = 0
	for i in lista:
		suma+=i
	print "La suma de la llista", lista, "és: ", suma
		
lista= []
crear (lista)
suma (lista)
