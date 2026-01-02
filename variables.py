default_result = 1
def sumar_dos_numeros(numero1=None, numero2=None):
	global default_result
	if numero1 is None or numero2 is None:
		return default_result
	else:
		return numero1 + numero2

print("Imprime la suma de los dos numeros", sumar_dos_numeros(1,2))
# Resultad 3
# Imprime la suma de los dos numeros 3
print("Imprime el valor por defecto", sumar_dos_numeros(2))
# Resultado 1
# Imprime el valor por defecto 1
