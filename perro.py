from mascota import Mascota

class Perro(Mascota):
    def __init__(self, nombre,tamanio,costo_consulta, cantidad_vacunas):
        super().__init__(nombre, costo_consulta)
        self._cantidad_vacunas = 0
        self.tamaño = tamanio
        self.cantidad_vacunas = cantidad_vacunas  

   
    def cantidad_vacunas1(self):
        return self._cantidad_vacunas

    def cantidad_vacunas(self,cantidad):
      
        if cantidad > 0:
            self._cantidad_vacunas = cantidad
        else:
            print(f"La cantidad de vacunas para el perro '{self.nombre}' debe ser mayor a 0.")

    def descripcion(self):
        print(f"El perro {self.nombre} es de tamaño {self.tamanio}")





    def mostrar_informacion(self):
        return f"Perro de nombre: {self.nombre}, Vacunas: {self.cantidad_vacunas}, con un costo en consulta: ${self.costo_consulta}"


