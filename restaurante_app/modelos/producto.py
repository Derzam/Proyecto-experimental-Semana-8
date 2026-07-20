# ============================================================
# modelos/producto.py
# Clase Producto — implementada con constructor tradicional
# (__init__) y control de atributos mediante @property/@setter.
# Se utilizan anotaciones de tipos en todos los métodos.
# ============================================================


class Producto:
    """Representa un producto disponible en el restaurante."""

    def __init__(
        self,
        nombre: str,
        categoria: str,
        precio: float,
        disponible: bool = True,
    ) -> None:
        # El constructor asigna los valores usando los setters,
        # de esta forma cada atributo queda validado desde su creación.
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.disponible = disponible

    # --------------------------------------------------------
    # Propiedad: nombre
    # --------------------------------------------------------
    @property
    def nombre(self) -> str:
        """Devuelve el nombre del producto."""
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        """Valida que el nombre no esté vacío antes de asignarlo."""
        if not valor or not valor.strip():
            raise ValueError("El nombre del producto no puede estar vacío.")
        self._nombre = valor.strip()

    # --------------------------------------------------------
    # Propiedad: categoria
    # --------------------------------------------------------
    @property
    def categoria(self) -> str:
        """Devuelve la categoría del producto."""
        return self._categoria

    @categoria.setter
    def categoria(self, valor: str) -> None:
        """Valida que la categoría no esté vacía antes de asignarla."""
        if not valor or not valor.strip():
            raise ValueError("La categoría del producto no puede estar vacía.")
        self._categoria = valor.strip()

    # --------------------------------------------------------
    # Propiedad: precio
    # --------------------------------------------------------
    @property
    def precio(self) -> float:
        """Devuelve el precio del producto."""
        return self._precio

    @precio.setter
    def precio(self, valor: float) -> None:
        """Valida que el precio sea un número mayor que cero."""
        try:
            valor = float(valor)
        except (TypeError, ValueError):
            raise ValueError("El precio del producto debe ser numérico.")
        if valor <= 0:
            raise ValueError("El precio del producto debe ser mayor que cero.")
        self._precio = valor

    # --------------------------------------------------------
    # Propiedad: disponible
    # --------------------------------------------------------
    @property
    def disponible(self) -> bool:
        """Devuelve la disponibilidad del producto."""
        return self._disponible

    @disponible.setter
    def disponible(self, valor: bool) -> None:
        """Almacena la disponibilidad como valor booleano."""
        self._disponible = bool(valor)

    # --------------------------------------------------------
    # Métodos de comportamiento
    # --------------------------------------------------------
    def mostrar_informacion(self) -> None:
        """Muestra los datos del producto de forma legible en consola."""
        estado = "Disponible" if self.disponible else "No disponible"
        print(f"  [{self.categoria}] {self.nombre} — ${self.precio:.2f} | {estado}")

    def __str__(self) -> str:
        """Representación en texto del producto."""
        return f"{self.nombre} (${self.precio:.2f})"
