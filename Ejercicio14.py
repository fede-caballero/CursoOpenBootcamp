class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
    def get_nota(self):
        return self.nota
    
    def resultado(self):
        if self.nota < 7:
            print(f"El estudiante {self.nombre} esta desaprobado")
            
        elif self.nota >= 7 and self.nota <= 10:
            print(f"El estudiante {self.nombre} esta aprobado")
            
a1 = Alumno("Federico", 6)
a2 = Alumno("Franco", 7)
print(f"El resultado obtenido por el alumno {a1.nombre} es: ", a1.get_nota())
a1.resultado()
print(f"El resultado obtenido por el alumno {a2.nombre} es: ", a2.get_nota())
a2.resultado()
