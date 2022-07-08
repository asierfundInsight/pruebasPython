
argument=input("mete valor teclado:  ")

if isinstance(argument,str):
	argument=int(argument)

print(type(argument))
if isinstance(argument, int):
	print("correcto")
else:
	print("error no es int")