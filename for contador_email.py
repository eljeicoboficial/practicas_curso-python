contador=0
MiEmail=input("Introduce tu direccion email: ")

for i in MiEmail:
    if(i=="@" or i=="."):
        contador = contador+1

if contador==2:
    print("Email es correcto ")
else:
    print("El Email es incorrecto ")
    
