# -*- coding: utf-8 -*-
def suma(a,b):
	suma = a+b
	print "El resultat de la suma és: ", suma
def resta (a,b):
	resta = a-b
	print "El resultat de la resta és: ", resta
def mult(a,b):
	mult = a*b
	print "El resultat de la multiplicació és: ", mult
def div (a,b):
	div = a/b
	print "El resultat de la divisió és: ", div

print "Quins factors vols operar ? "
op1 = int(input())
op2 = int (input())
print "Quina operacio vols realitzar (S, R, M, D)?"
op = raw_input()
if (op=="s" or op=="S"):
	suma(op1,op2)
if op=="r" or op=="R":
	resta(op1,op2)
if op=="m" or op=="M":
	mult(op1,op2)
if op=="d" or op=="D":
	div(op1,op2)
