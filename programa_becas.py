print ("programa de becas")

distancia_escuela=int(input("Introduce la distancia a la escuela en km: "))
print (distancia_escuela)

numero_hermano=int(input("Introduce el numero de hermanos: "))
print (numero_hermano) 

salario_familiar=int(input("Introduce el salario anual bruto: "))
print (salario_familiar)

if distancia_escuela>40 or numero_hermano>2 or salario_familiar<=200000:
    print("FELICIDADES TIENE DERECHO A LA BECA")
else:
    print("No tienes derecho a la beca")
    
