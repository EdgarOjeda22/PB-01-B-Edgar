from mascota import Mascota

class Conejo(Mascota):

    def __init__(self,color_pelaje, nombre, costo_consulta, tipo_alimentacion):
        super().__init__(nombre, costo_consulta)
        self._tipo_alimentacion = ""
        self.tipo_alimentacion = tipo_alimentacion 
        self.color_pelaje = color_pelaje

    def tipo_alimentacion(self):
        return self._tipo_alimentacions

    
    def tipo_alimentacion(self,valor):
    
        if valor in valor:
            self._tipo_alimentacion = valor
        else:
            print(f"El tipo de alimentación del conejo '{self.nombre}' no puede estar vacío. Valor rechazado.")

    def obtener_descripcion(self) :
        return (f"Conejo - Nombre: {self.nombre}, Alimentación: {self.tipo_alimentacion}, Costo Consulta:{self.costo_consulta}")
        