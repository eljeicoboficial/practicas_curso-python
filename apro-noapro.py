print("programa de evaluacion de notas de alumno")

nota_alumno=input()

def evaluacion(nota):
    valoracion="aprobado"
    if nota<5:
        valoracion="reprobado"
        return valoracion

    
print(evaluacion(int(nota_alumno)))
