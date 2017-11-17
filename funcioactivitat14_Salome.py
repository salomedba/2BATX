# -*- coding: utf-8 -*-

def crear (lista):
	print "Dime quants elements té la llista: "
	numero = int(input())
	if numero < 1:
		print("Imposible!")
	else:
		for i in range(numero):
			print"Dime l'element ", i+1, ": "
			n = int(input())
			lista += [n]
	print"La llista creada és:", lista
	
def mijana (lista):
	suma = 0
	for i in lista:
		suma+=i	
	mij = suma/len(lista)
	print "La mijana de la llista és: ", mij
		
lista = []
crear(lista)
mijana(lista)
