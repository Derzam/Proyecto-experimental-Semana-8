# 🍽️ Sistema de Gestión de Restaurante
### Programación Orientada a Objetos en Python — Versión con herencia y principios SOLID
## Autor : Derly Zambrano
---

## 📋 Descripción

Esta versión del sistema `restaurante_app` incorpora **herencia** y **polimorfismo**: se agrega la clase `Bebida`, que extiende a `Producto`, y el servicio `Restaurante` administra ambos tipos de objetos en una **única colección**, sin necesitar lógica especial para distinguirlos.

El sistema permite **registrar productos, bebidas y clientes**, y **listarlos**, mediante un **menú interactivo ejecutado desde consola**.

---

## 🗂️ Estructura del Proyecto

```
restaurante_app/
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py           # Clase Producto (__init__, @property, @setter)
│   ├── bebida.py             # Clase Bebida — hereda de Producto
│   └── cliente.py            # Clase Cliente (@dataclass)
│
├── servicios/
│   ├── __init__.py
│   └── restaurante.py        # Clase Restaurante (colección polimórfica)
│
└── main.py                   # Punto de arranque con menú interactivo
```

---

## 🧩 Clases Implementadas

### 📦 `Producto` — `modelos/producto.py`

Representa los datos comunes de cualquier producto del restaurante, con `__init__` tradicional y atributos controlados por `@property`/`@setter`.

| Atributo | Validación |
|---|---|
| `nombre` | No puede estar vacío |
| `categoria` | No puede estar vacía |
| `precio` | Debe ser mayor que cero |
| `disponible` | Se normaliza a booleano |

`mostrar_informacion()` imprime los datos del producto en consola.

---

### 🥤 `Bebida` — `modelos/bebida.py` (hereda de `Producto`)

`Bebida` **extiende** a `Producto` mediante herencia. Su constructor llama a `super().__init__(...)` para reutilizar la inicialización de los atributos comunes, y añade un atributo propio:

| Atributo adicional | Validación |
|---|---|
| `volumen_ml` | Debe ser un número mayor que cero |

`Bebida` **sobrescribe** `mostrar_informacion()` para incluir el volumen en la salida — este es el mecanismo de **polimorfismo**: el mismo método (`mostrar_informacion()`) produce resultados distintos según el objeto que lo ejecuta.

```python
class Bebida(Producto):
    def __init__(
        self,
        nombre: str,
        categoria: str,
        precio: float,
        volumen_ml: float,
        disponible: bool = True,
    ) -> None:
        super().__init__(nombre, categoria, precio, disponible)
        self.volumen_ml = volumen_ml
```

---

### 👤 `Cliente` — `modelos/cliente.py`

Implementada con `@dataclass`. Atributos: `id_cliente`, `nombre`, `correo`.

---

### 🏠 `Restaurante` — `servicios/restaurante.py`

Administra **una única lista de productos**, en la que conviven objetos `Producto` y `Bebida` gracias al polimorfismo, y una lista independiente de clientes.

| Método | Descripción |
|---|---|
| `registrar_producto(producto)` | Agrega un `Producto` **o** `Bebida` a la colección única |
| `listar_productos()` | Devuelve todos los productos/bebidas registrados |
| `registrar_cliente(cliente)` | Agrega un `Cliente`, validando que el ID y el correo no estén repetidos |
| `listar_clientes()` | Devuelve todos los clientes registrados |

> La validación de duplicados (ID/correo) vive **dentro de `Restaurante`**, no en `main.py`, para mantener la lógica de negocio encapsulada en el servicio.

---

## 🧠 Principios SOLID Aplicados

| Principio | Aplicación en el proyecto |
|---|---|
| **S — Responsabilidad única** | `Producto`/`Bebida` representan productos; `Cliente` representa un cliente; `Restaurante` solo coordina las colecciones, sin conocer los detalles internos de cada clase |
| **O — Abierto/cerrado** | `Bebida` amplía el sistema mediante herencia; `Restaurante` no necesitó modificarse para aceptar el nuevo tipo |
| **L — Sustitución de Liskov** | Cualquier objeto `Bebida` puede usarse donde se espera un `Producto` (misma lista, mismo método `mostrar_informacion()`) sin romper el sistema |

*(Los principios de Segregación de Interfaces e Inversión de Dependencias no aplican al alcance de esta actividad.)*

---

## ▶️ Cómo Ejecutar el Programa

### Requisitos
- Python 3.7 o superior

### Pasos

```bash
python main.py
```

---

## 🖥️ Menú Interactivo

```
===== SISTEMA DE RESTAURANTE =====
1. Registrar producto
2. Registrar bebida
3. Registrar cliente
------------------------------
4. Listar productos
5. Listar clientes
------------------------------
0. Salir
```

El sistema permanece en ejecución en un bucle `while True` hasta que el usuario selecciona **`0`**.

---

## 🔄 Flujo del Sistema

```
usuario selecciona una opción
        ↓
main.py solicita los datos
        ↓
se crea un objeto Producto, Bebida o Cliente
        ↓
Restaurante procesa el registro (incluye validaciones)
        ↓
el objeto se almacena en la colección
        ↓
main.py presenta el resultado
```

Durante el listado de productos, `main.py` recorre la colección única y ejecuta `producto.mostrar_informacion()` para cada elemento **sin verificar su tipo**: cada objeto ejecuta su propia versión del método (polimorfismo).

---

## 🛡️ Manejo de Errores

Todas las entradas del usuario están protegidas con `try/except`:

- Precio o volumen no numérico → error capturado, no se registra el objeto.
- Nombre o categoría vacíos → `ValueError` lanzado por el `setter` de `Producto`, capturado en `main.py`.
- Volumen de bebida menor o igual a cero → `ValueError` lanzado por el `setter` de `Bebida`.
- ID de cliente no numérico → capturado antes de crear el objeto.
- ID o correo de cliente repetido → `ValueError` lanzado por `Restaurante.registrar_cliente()`.
- Opción de menú inexistente → mensaje informativo, el programa continúa.

---

## ✅ Conceptos de POO Aplicados

| Concepto | Aplicación |
|---|---|
| **Herencia** | `Bebida(Producto)`, con `super().__init__(...)` |
| **Polimorfismo** | `mostrar_informacion()` sobrescrito en `Bebida`; se invoca igual para ambos tipos |
| **`@property` / `@setter`** | Validación de atributos en `Producto` y `Bebida` |
| **`@dataclass`** | Constructor automático en `Cliente` |
| **Encapsulamiento** | Atributos internos (`_nombre`, `_precio`, `_volumen_ml`) protegidos por propiedades |
| **Composición** | `Restaurante` administra colecciones de `Producto`/`Bebida` y `Cliente` |
| **Principios SOLID (S, O, L)** | Ver sección dedicada arriba |
| **Modularidad** | Separación en `modelos/` y `servicios/`, comunicados por importaciones |
| **Anotaciones de tipos** | Todos los métodos y funciones del proyecto declaran el tipo de sus parámetros y su valor de retorno (`-> None`, `-> str`, `-> List[Producto]`, etc.) |

---

