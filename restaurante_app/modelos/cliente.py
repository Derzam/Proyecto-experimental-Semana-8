# ============================================================
# modelos/cliente.py
# Clase Cliente — implementada con el decorador @dataclass,
# que genera automáticamente __init__, __repr__ y __eq__ a
# partir de las anotaciones de tipos de sus atributos.
# ============================================================

from dataclasses import dataclass


@dataclass
class Cliente:
    """Representa a un cliente registrado en el restaurante."""

    id_cliente: int  # Identificador único del cliente
    nombre: str       # Nombre completo del cliente
    correo: str       # Correo electrónico de contacto

    def __str__(self) -> str:
        """Representación en texto del cliente."""
        return f"[ID {self.id_cliente}] {self.nombre} — {self.correo}"
