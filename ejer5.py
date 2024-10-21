import random

random1=random.randrange(2,10)
random2=random.randrange(2,10)
resultadoRandom=random.randrange(2,81)
resultado=random1*random2


print(f"Cual es el resultado de: {random1} * {random2}")


usuarioResultado = int  (input("Introduzca el resultado que usted cree correcto para la operacion:"))

if usuarioResultado == resultado:
      print("La respuesta es correcta")
else:
      print(f"El resultado no es correcto, el verdadero resultado es {resultado}")


