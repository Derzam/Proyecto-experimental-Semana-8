# ============================================================
# main.py
# Punto de arranque del sistema de gestión de restaurante.
# Presenta un menú interactivo que permite registrar productos,
# bebidas y clientes, y listarlos mediante polimorfismo.
# Se utilizan anotaciones de tipos en todas las funciones.
# ============================================================

from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.cliente import Cliente


def mostrar_menu() -> None:
    """Imprime las opciones disponibles del sistema."""
    print("\n===== SISTEMA DE RESTAURANTE =====")
    print("1. Registrar producto")
    print("2. Registrar bebida")
    print("3. Registrar cliente")
    print("------------------------------")
    print("4. Listar productos")
    print("5. Listar clientes")
    print("------------------------------")
    print("0. Salir")


# ----------------------------------------------------------
# Registro de productos y bebidas
# ----------------------------------------------------------
def registrar_producto(restaurante: Restaurante) -> None:
    """Solicita los datos de un producto general y lo registra."""
    print("\n-- Registrar nuevo producto --")
    try:
        nombre: str = input("Nombre del producto: ")
        categoria: str = input("Categoría: ")
        precio: float = float(input("Precio: "))
        resp: str = input("¿Disponible? (s/n): ").strip().lower()
        disponible: bool = resp == "s"

        # El constructor de Producto valida nombre, categoría y precio
        producto: Producto = Producto(nombre, categoria, precio, disponible)
        restaurante.registrar_producto(producto)
        print(f"✔ Producto '{producto.nombre}' registrado correctamente.")
    except ValueError as error:
        print(f"✘ No se pudo registrar el producto: {error}")


def registrar_bebida(restaurante: Restaurante) -> None:
    """Solicita los datos de una bebida y la registra en la misma colección de productos."""
    print("\n-- Registrar nueva bebida --")
    try:
        nombre: str = input("Nombre de la bebida: ")
        categoria: str = input("Categoría: ")
        precio: float = float(input("Precio: "))
        volumen_ml: float = float(input("Volumen (ml): "))
        resp: str = input("¿Disponible? (s/n): ").strip().lower()
        disponible: bool = resp == "s"

        # Bebida hereda de Producto; se registra en la misma colección
        # gracias al polimorfismo (Bebida ES-UN Producto).
        bebida: Bebida = Bebida(nombre, categoria, precio, volumen_ml, disponible)
        restaurante.registrar_producto(bebida)
        print(f"✔ Bebida '{bebida.nombre}' registrada correctamente.")
    except ValueError as error:
        print(f"✘ No se pudo registrar la bebida: {error}")


# ----------------------------------------------------------
# Registro de clientes
# ----------------------------------------------------------
def registrar_cliente(restaurante: Restaurante) -> None:
    """Solicita los datos de un cliente y lo registra en el sistema."""
    print("\n-- Registrar nuevo cliente --")
    try:
        id_cliente: int = int(input("ID del cliente: "))
        nombre: str = input("Nombre del cliente: ")
        correo: str = input("Correo del cliente: ")

        cliente: Cliente = Cliente(id_cliente=id_cliente, nombre=nombre, correo=correo)
        # La validación de ID/correo duplicado ocurre dentro de Restaurante
        restaurante.registrar_cliente(cliente)
        print(f"✔ Cliente '{cliente.nombre}' registrado correctamente.")
    except ValueError as error:
        print(f"✘ No se pudo registrar el cliente: {error}")


# ----------------------------------------------------------
# Listados
# ----------------------------------------------------------
def listar_productos(restaurante: Restaurante) -> None:
    """Muestra todos los productos y bebidas registrados usando polimorfismo."""
    print("\n-- Lista de productos --")
    productos: list[Producto] = restaurante.listar_productos()
    if not productos:
        print("No hay productos registrados.")
        return
    # Polimorfismo: cada objeto ejecuta SU PROPIA versión de
    # mostrar_informacion(), sin que este bucle necesite saber
    # si el objeto es un Producto o una Bebida.
    for producto in productos:
        producto.mostrar_informacion()


def listar_clientes(restaurante: Restaurante) -> None:
    """Muestra todos los clientes registrados."""
    print("\n-- Lista de clientes --")
    clientes: list[Cliente] = restaurante.listar_clientes()
    if not clientes:
        print("No hay clientes registrados.")
        return
    for cliente in clientes:
        print(f"  {cliente}")


# ----------------------------------------------------------
# Bucle principal del programa
# ----------------------------------------------------------
def main() -> None:
    """Ejecuta el menú interactivo hasta que el usuario decida salir."""
    restaurante: Restaurante = Restaurante()

    # Diccionario que enlaza cada opción del menú con su función
    opciones: dict = {
        "1": registrar_producto,
        "2": registrar_bebida,
        "3": registrar_cliente,
        "4": listar_productos,
        "5": listar_clientes,
    }

    while True:
        mostrar_menu()
        opcion: str = input("Seleccione una opción: ").strip()

        if opcion == "0":
            print("\nSaliendo del sistema. ¡Hasta pronto!")
            break
        elif opcion in opciones:
            opciones[opcion](restaurante)
        else:
            print("✘ Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()
