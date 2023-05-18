# Backend Artesanías - Autómata Digital

## Descripción
Este proyecto es el backend para la plataforma web de gestión de pedidos de productos artesanales. Proporciona la funcionalidad necesaria para registrar usuarios, gestionar productos y realizar pedidos.

## Características del proyecto
- Registro e inicio de sesión de usuarios.
- Autenticación y generación de tokens JWT para mantener la seguridad de las sesiones de los usuarios.
- Gestión de usuarios administradores con capacidades de agregar nuevos productos.
- Usuarios regulares pueden realizar pedidos seleccionando productos disponibles.

## Tecnologías Utilizadas <a name="requisitos-previos"></a>
- Python 3.10.6
- Django (framework de desarrollo web en Python)
- Firebase (base de datos)

## Requisitos
- Python 3.10.6 instalado en tu sistema.
- Virtual Env (se recomienda usar venv para aislar las dependencias del proyecto).

## Instalación y Configuración
1. Clonar el repositorio
```bash
git clone https://github.com/EduardoIxen/Artesanias_Backend.git
```

2. Navegar al directorio del proyecto
```bash
cd Artesanias_Backend
```

3. Instalar virtualenv para crear el entorno virtual
```bash
pip install virtualenv
```

4. Crear el entorno virtual
```bash
virtualenv nombre_del_entorno
```

5. Activar el entorno virtual
- En Windows
```bash
nombre_del_entorno\Scripts\activate
```
- En Linux
```bash
source nombre_del_entorno/bin/activate
```

6. Instalar las dependencias del proyecto
```bash
pip install -r requirements.txt
```

## Ejectuar el proyecto
1. Dentro del directorio del proyecto, ejecutar el comando
```bash
python manage.py runserver
```
Esto iniciará el servidor de desarrollo en http://localhost:8000/


# Estructura de la base de datos
La base de datos se creó en firebase, y se compone de 4 colecciones:
- **administradores**: Contiene la información de los usuarios administradores. Por defecto solo hay uno. ("email":admin@automatadg.com, "password":admin)
- **pedidos**: Contiene la información de los pedidos realizados por los usuarios. Consta de una lista de los **sku** de los productos seleccionados, el total del pedido, el usuario que realizó el pedido y el estado del pedido.
- **productos**: Contiene la información de los productos disponibles. Cada producto tiene un **sku** único, un nombre, un precio, una imagen y el nombre del artesano que lo creó.
- **usuarios**: Contiene la información de los usuarios registrados en la plataforma.

```json
{
  "administradores": [
    {
      "contrasena": "8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918",
      "email": "admin@automatadg.com",
      "id": 1,
      "nombre": "Administrador"
    }
  ],
  "pedidos": {
    "-NVfqa0NBcFdG-SBfdMy": {
      "completado": false,
      "productos": [
        {
          "sku": "TS123456"
        },
        {
          "sku": "TS1234561"
        }
      ],
      "total": 100.77,
      "usuario": "ed@gmail.com"
    },...
  },
  "productos": {
    "-NVelT-SUAy5knQvPbWl": {
      "artesano": "Pedro Gomez",
      "imagen": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS4la4OcZziTBeJQ3bSqffkDYY0tvWRw6oHj61yke41u8vTOf5MBO1FvuQBRDosQYN2Fec",
      "nombre": "Jarro de porcelana",
      "precio": 200,
      "sku": "TS123456"
    },...
  },
  "usuarios": {
    "-NVfH4WfjD6hALbsOSK1": {
      "contrasena": "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad",
      "email": "ed@gmail.com",
      "nombre": "Eduardo Ixen"
    },...
  }
}
```