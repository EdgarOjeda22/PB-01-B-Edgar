from perro import Perro
from gato import Gato
from conejo import Conejo
from aplicacion_mascotas import AplicacionMascotas

def main():
    print("GESTIÓN DE MASCOTAS")

    
    app = AplicacionMascotas()

    
    perro1 = Perro("Firulo", 30, 3, 2)
    perro2 = Perro("Rocky", 25, 2)
    gato1 = Gato("Miau", 20, 7)
    conejo1 = Conejo("Limon", 15, "Zanahorias")

    print("\n--- ANIMALES")
    print(perro1.obtener_descripcion())
    print(perro2.obtener_descripcion())
    print(gato1.obtener_descripcion())
    print(conejo1.obtener_descripcion())

    print("Probar")


    print(f"Costo anterior de {perro1.nombre}:{perro1.get_consulta}")
    perro1.costo_consulta = 35
    print(f"Nuevo costo de {perro1.nombre} con:{perro1.set_consulta}")

    perro1.get_consulta = -5

    print("Agrega mascota")
    app.agregar_mascota(perro1)
    app.agregar_mascota(perro2)
    app.agregar_mascota(gato1)
    app.agregar_mascota(conejo1)


    app.mostrar_catalogo()
    
    total_consultas = app.calcular_costo_total_consultas()
    print(f"Costo total de consultas en la clínica:{total_consultas}")


if __name__ == "__main__":
    main()