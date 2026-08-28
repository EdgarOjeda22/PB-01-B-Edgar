from mascota import Mascota

class AplicacionMascotas:
    def __init__(self):
        self._lista_mascotas = []

    def agregar_mascota(self, mascota: Mascota):
        self._lista_mascotas.append(mascota)

    def mostrar_catalogo(self):
        print(" MASCOTAS REGISTRADAS ---")
        if not self._lista_mascotas:
            print("No hay mascotas registradas.")
            return
        
        for mascota in self._lista_mascotas:
            print(mascota.obtener_descripcion())

    def calcular_costo_total_consultas(self):
        total = sum(mascota.costo_consulta for mascota in self._lista_mascotas)
        return total