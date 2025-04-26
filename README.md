# API de Productos

Una API REST para la gestión de productos y categorías con autenticación JWT, desarrollada con Flask y SQLAlchemy.

## Características

- Autenticación JWT
- Gestión de usuarios
- CRUD completo para productos
- CRUD completo para categorías
- Documentación con Swagger
- CORS habilitado
- Base de datos SQL con SQLAlchemy

## Requisitos

- Python 3.x
- Flask
- Flask-RESTX
- Flask-CORS
- SQLAlchemy
- PyJWT

## Instalación

1. Clonar el repositorio
2. Instalar las dependencias:
```bash
pip install -r requirements.txt
```

## Configuración

1. Configurar la base de datos en el archivo `config.py`
2. Asegurarse de que las variables de entorno necesarias estén configuradas

## Estructura del Proyecto

```
├── main.py              # Punto de entrada de la aplicación
├── database.py          # Configuración de la base de datos
├── models.py           # Modelos de SQLAlchemy
├── schemas.py          # Esquemas Pydantic
├── crud.py            # Operaciones CRUD
├── auth.py            # Funciones de autenticación
└── config.py          # Configuración de la aplicación
```

## Endpoints de la API

### Autenticación

#### POST /auth/token
- Iniciar sesión y obtener token JWT
- Cuerpo de la petición: `{ "email": "usuario@ejemplo.com", "password": "contraseña123" }`

#### POST /auth/register
- Registrar nuevo usuario
- Cuerpo de la petición: `{ "email": "usuario@ejemplo.com", "password": "contraseña123", "full_name": "Juan Pérez" }`

### Productos

#### GET /productos/
- Listar todos los productos
- Parámetros opcionales: `nombre`, `categoria_id`

#### POST /productos/
- Crear nuevo producto (requiere autenticación)
- Cuerpo de la petición: `{ "nombre": "Smartphone XYZ", "precio": 999.99, "categoria_id": 1 }`

#### GET /productos/{id}
- Obtener producto específico

#### PUT /productos/{id}
- Actualizar producto (requiere autenticación)
- Cuerpo de la petición: `{ "nombre": "Smartphone XYZ", "precio": 999.99, "categoria_id": 1 }`

#### DELETE /productos/{id}
- Eliminar producto (requiere autenticación)

### Categorías

#### GET /categorias/
- Listar todas las categorías

#### POST /categorias/
- Crear nueva categoría (requiere autenticación)
- Cuerpo de la petición: `{ "nombre": "Electrónicos" }`

#### GET /categorias/{id}
- Obtener categoría específica

#### PUT /categorias/{id}
- Actualizar categoría (requiere autenticación)
- Cuerpo de la petición: `{ "nombre": "Electrónicos" }`

#### DELETE /categorias/{id}
- Eliminar categoría (requiere autenticación)

## Documentación Swagger

La documentación completa de la API está disponible en `/docs` cuando la aplicación está en ejecución.

## Seguridad

- Autenticación mediante JWT
- Contraseñas hasheadas
- CORS configurado para dominio específico
- Validación de datos de entrada

## Ejecución

```bash
python main.py
```

La aplicación se ejecutará en modo debug en `http://localhost:5000`

## Notas

- La aplicación está configurada para aceptar peticiones desde `https://main.dugkv90jvsln4.amplifyapp.com/`
- Los tokens JWT tienen un tiempo de expiración configurable
- Todas las operaciones de escritura requieren autenticación
