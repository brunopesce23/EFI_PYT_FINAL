## DOCUMENTACION DE LA API

# Endpoints de la API

A continuación se describen los principales endpoints de la API con ejemplos de solicitud y respuesta.

## Autenticación

### Obtener token de autenticación
- **Método**: POST  
- **Endpoint**: `/api/token/`  
- **Cuerpo de la solicitud**:
  ```json
  {
    "username": "Admin",
    "password": "admin"
  }
  ```
- **Ejemplo de respuesta**:
  ```json
  {
    "token": "tu_token_de_autenticacion"
  }
  ```

## Usuarios

### Crear Usuario
- **Método**: POST  
- **Endpoint**: `/api/usuarios/`  
- **Cabecera de la solicitud**: `Authorization: Bearer <tu_token_de_autenticacion>`  
- **Cuerpo de la solicitud**:
  ```json
  {
    "username": "nuevo_usuario",
    "password": "contrasena123"
  }
  ```
- **Ejemplo de respuesta**:
  ```json
  {
    "id": 1,
    "username": "nuevo_usuario"
  }
  ```

### Obtener Usuarios
- **Método**: GET  
- **Endpoint**: `/api/usuarios/`  
- **Cabecera de la solicitud**: `Authorization: Bearer <tu_token_de_autenticacion>`  
- **Ejemplo de respuesta**:
  ```json
  [
    {
      "id": 1,
      "username": "usuario1"
    },
    {
      "id": 2,
      "username": "usuario2"
    }
  ]
  ```

## Equipos

### Crear Equipos de Celulares
- **Método**: POST  
- **Endpoint**: `/api/equipos/`  
- **Cabecera de la solicitud**: `Authorization: Bearer <tu_token_de_autenticacion>`  
- **Cuerpo de la solicitud**:
  ```json
  {
    "modelo": "Galaxy S22",
    "almacenamiento": "128GB",
    "color": "Negro",
    "bateria": "4000mAh",
    "precio": 999.99,
    "stock": 10,
    "imei": "123456789012345",
    "accesorio": "Cargador"
  }
  ```
- **Ejemplo de respuesta**:
  ```json
  {
    "id": 1,
    "modelo": "Galaxy S22",
    "almacenamiento": "128GB",
    "color": "Negro",
    "bateria": "4000mAh",
    "precio": 999.99,
    "stock": 10,
    "imei": "123456789012345",
    "accesorio": "Cargador"
  }
  ```

### Obtener Equipos
- **Método**: GET  
- **Endpoint**: `/api/equipos/`  
- **Cabecera de la solicitud**: `Authorization: Bearer <tu_token_de_autenticacion>`  
- **Ejemplo de respuesta**:
  ```json
  [
    {
      "id": 1,
      "modelo": "Galaxy S22",
      "almacenamiento": "128GB",
      "color": "Negro",
      "bateria": "4000mAh",
      "precio": 999.99,
      "stock": 10,
      "imei": "123456789012345",
      "accesorio": "Cargador"
    }
  ]
  ```
