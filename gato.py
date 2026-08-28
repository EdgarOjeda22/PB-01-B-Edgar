from mascota import Mascota
#Hereda de la clase Mascota 
class Gato(Mascota):
    def __init__(self,color_pelaje, vidas):
        self.color_pelaje = color_pelaje
        self.vidas = vidas


    def descripcion(self):
        print(f"El gato {self.nombre} de color {self.color_pelaje}")


    def mostrar_informacion(self):
        print(f"El gato{self.nombre}tiene{self.vidas}")

        