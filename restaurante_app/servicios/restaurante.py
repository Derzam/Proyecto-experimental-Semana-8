# ============================================================
# servicios/restaurante.py
# Clase Restaurante — administra una colección ÚNICA de
# productos (Producto y Bebida conviven allí gracias al
# polimorfismo) y una colección de clientes.
# Se utilizan anotaciones de tipos en todos los métodos.
#
# Principios SOLID aplicados en esta clase:
#   S: solo coordina colecciones, no conoce los detalles
#      internos de Producto, Bebida o Cliente.
#   O: acepta cualquier subclase de Producto (como Bebida) sin
#      necesitar modificaciones cuando aparecen nuevos tipos.
#   L: trata cada objeto de la lista como un Producto, sin
#      importar si en realidad es una Bebida.
# ============================================================

from typing import List

from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:
    """Clase de servicio que administra productos (y bebidas) y clientes."""

    def __init__(self) -> None:
        # Colección única: puede contener tanto objetos Producto
        # como objetos Bebida, ya que Bebida ES-UN Producto.
        self._productos: List[Producto] = []
        self._clientes: List[Cliente] = []

    # --------------------------------------------------------
    # Gestión de productos (incluye bebidas, por herencia)
    # --------------------------------------------------------
    def registrar_producto(self, producto: Producto) -> None:
        """Agrega un Producto o Bebida a la colección única de productos."""
        self._productos.append(producto)

    def listar_productos(self) -> List[Producto]:
        """Devuelve la lista completa de productos y bebidas registrados."""
        return self._productos

    # --------------------------------------------------------
    # Gestión de clientes
    # --------------------------------------------------------
    def registrar_cliente(self, cliente: Cliente) -> None:
        """Agrega un Cliente, validando que el ID y el correo sean únicos."""
        for existente in self._clientes:
            if existente.id_cliente == cliente.id_cliente:
                raise ValueError(
                    f"Ya existe un cliente registrado con el ID {cliente.id_cliente}."
                )
            if existente.correo.strip().lower() == cliente.correo.strip().lower():
                raise ValueError(
                    f"Ya existe un cliente registrado con el correo '{cliente.correo}'."
                )
        self._clientes.append(cliente)

    def listar_clientes(self) -> List[Cliente]:
        """Devuelve la lista completa de clientes registrados."""
        return self._clientes
