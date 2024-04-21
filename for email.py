email=False
MiEmail=input("Introduce tu direccion email: ")

for i in MiEmail:
    if(i=="@"):
        email=True

if email:
    print("Email es correcto ")
else:
    print("El Email es incorrecto ")
    
