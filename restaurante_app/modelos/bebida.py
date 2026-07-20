# ============================================================
# modelos/bebida.py
# Clase Bebida — hereda de Producto (herencia) e incorpora un
# atributo propio (volumen_ml). Aplica el principio Abierto/
# Cerrado: extiende el sistema sin modificar Producto ni
# Restaurante. Se utilizan anotaciones de tipos en todos los
# métodos.
# ============================================================

from modelos.producto import Producto


class Bebida(Producto):
    """Representa una bebida del restaurante; es un tipo especial de Producto."""

    def __init__(
        self,
        nombre: str,
        categoria: str,
        precio: float,
        volumen_ml: float,
        disponible: bool = True,
    ) -> None:
        # Reutiliza el constructor de Producto para inicializar
        # los atributos comunes (nombre, categoria, precio, disponible)
        super().__init__(nombre, categoria, precio, disponible)
        # Atributo propio de Bebida, también controlado por @property/@setter
        self.volumen_ml = volumen_ml

    # --------------------------------------------------------
    # Propiedad: volumen_ml (atributo adicional propio de Bebida)
    # --------------------------------------------------------
    @property
    def volumen_ml(self) -> float:
        """Devuelve el volumen de la bebida en mililitros."""
        return self._volumen_ml

    @volumen_ml.setter
    def volumen_ml(self, valor: float) -> None:
        """Valida que el volumen sea un número mayor que cero."""
        try:
            valor = float(valor)
        except (TypeError, ValueError):
            raise ValueError("El volumen de la bebida debe ser numérico.")
        if valor <= 0:
            raise ValueError("El volumen de la bebida debe ser mayor que cero.")
        self._volumen_ml = valor

    # --------------------------------------------------------
    # Sobrescritura de mostrar_informacion() (polimorfismo)
    # --------------------------------------------------------
    def mostrar_informacion(self) -> None:
        """Muestra los datos de la bebida, incluyendo su volumen."""
        estado = "Disponible" if self.disponible else "No disponible"
        print(
            f"  [{self.categoria}] {self.nombre} — ${self.precio:.2f} "
            f"| {self.volumen_ml:.0f} ml | {estado}"
        )

    def __str__(self) -> str:
        """Representación en texto de la bebida."""
        return f"{self.nombre} ({self.volumen_ml:.0f} ml, ${self.precio:.2f})"
