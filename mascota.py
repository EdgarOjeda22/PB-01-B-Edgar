from aplicacion_mascotas import AplicacionMascotas

#Clase padre mascota
class Mascota:
   
    def __init__(self, nombre, edad, raza, peso costo_consulta):
        self._nombre = nombre
        self.edad = edad
        self.peso = peso 
        self.raza = raza 
        self._costo_consulta = self._costo_consulta

        
    def descripcion (self):
        print (f"De nombre {self.nombre}")
        return self._nombre


    def get_consulta(self):
        return self._costo_consulta


    def set_consulta(self,nuevo_costo):
        if nuevo_costo > 0:
            self._costo_consulta = nuevo_costo
        else:
            print(f"El costo de consulta {nuevo_costo} debe ser mayor que 0")

    