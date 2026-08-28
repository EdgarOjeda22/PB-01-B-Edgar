from mascota import Mascota

class Conejo(Mascota):

    def __init__(self, nombre, costo_consulta, tipo_alimentacion):
        super().__init__(nombre, costo_consulta)
        self._tipo_alimentacion = ""
        self.tipo_alimentacion = tipo_alimentacion  # Validación mediante setter

    @property
    def tipo_alimentacion(self) -> str:
        """Retorna el tipo de alimentación del conejo."""
        return self._tipo_alimentacion

    @tipo_alimentacion.setter
    def tipo_alimentacion(self, valor: str):
        """
        Regla de negocio: El tipo de alimentación de un conejo no puede estar vacío.
        El sistema muestra un error y no acepta valores vacíos o espacios en blanco.
        """
        if valor and valor.strip():
            self._tipo_alimentacion = valor.strip()
        else:
            print(f"[ERROR] El tipo de alimentación del conejo '{self.nombre}' no puede estar vacío. Valor rechazado.")

    def obtener_descripcion(self) -> str:
        """
        Implementación del método heredado (Polimorfismo).
        Retorna la descripción detallada del conejo.
        """
        return f"Conejo - Nombre: {self.nombre}, Alimentación: {self.tipo_alimentacion}, Costo Consulta: ${self.costo_consulta:.2f}"
        