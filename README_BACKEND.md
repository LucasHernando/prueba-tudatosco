# README - Aplicación API con Flask (Dockerizada)

Este proyecto consiste en una API RESTful desarrollada en Flask para la gestión de eventos y sesiones, completamente dockerizada.

---

## ⚡ Requisitos Iniciales

Asegúrese de tener instalado:
- [Docker](https://www.docker.com/products/docker-desktop)
- [Docker Compose](https://docs.docker.com/compose/)

---

## ▶️ Inicialización del Proyecto

Desde la raíz del proyecto, levante los servicios usando:

```bash
docker-compose -f backend_events/docker-compose-backend.yml up --build
```

Una vez inicializado el contenedor, ingrese al contenedor y ejecute los siguientes comandos para configurar la base de datos:

```bash
# 1. Inicializar migraciones
flask db init

# 2. Detectar cambios
flask db migrate -m "Initial migration"

# 3. Aplicar cambios
flask db upgrade

# 4. Cargar datos iniciales (usuarios, roles, permisos, eventos, sesiones, etc.)
flask seed
```

---

## 🔑 Autenticación

**Login de Usuario**
- **URL**: `POST /api/login`
- **Body**:
```json
{
  "email": "test@gmail.com",
  "password": "password_1254521214"
}
```
- **Respuesta exitosa**: JWT Token para autenticación en endpoints protegidos.

---

## 📄 Endpoints Principales

### 👤 Usuarios
- `POST /api/users`: Crear usuario

### 🏛️ Eventos
- `GET /api/events`: Listar eventos
- `POST /api/events`: Crear evento
- `PUT /api/events/<id>`: Actualizar evento
- `DELETE /api/events/<id>`: Eliminar evento

### 📅 Sesiones
- `POST /api/sessions`: Crear sesión
- `PUT /api/sessions/<id>`: Actualizar sesión
- `DELETE /api/sessions/<id>`: Eliminar sesión

### 👥 Registros a Eventos
- `GET /api/registrations`: Listar eventos registrados
- `POST /api/registrations`: Registrar usuario a evento

### 👮‍♂️ Roles y Permisos
- `GET /api/roles`: Listar roles
- `POST /api/roles`: Crear rol
- `PUT /api/roles/<id>`: Actualizar rol
- `DELETE /api/roles/<id>`: Eliminar rol

#### 🧑 Asociación Roles - Usuarios
- `POST /api/role_users`: Asignar usuarios a un rol
- `GET /api/role_users?role_id=...`: Listar usuarios por rol
- `DELETE /api/role_users`: Eliminar usuarios de un rol

#### 🔒 Asociación Roles - Permisos
- `POST /api/role_permissions`: Asignar permisos a rol
- `DELETE /api/role_permissions`: Eliminar permisos de un rol

---

## 📊 Ejemplo de Uso (Login + Crear Evento)

1. Autenticarse con `POST /api/login` y obtener el `access_token`.
2. Usar el token en los headers:
```http
Authorization: Bearer <access_token>
```
3. Crear un evento:
```json
POST /api/events
{
  "title": "Taller de Python",
  "description": "Curso práctico",
  "status": "programado",
  "capacity": 50,
  "start_date": "2025-08-01T09:00:00",
  "end_date": "2025-08-01T13:00:00"
}
```

---


## ✅ Pruebas Unitarias

Puedes ejecutar las pruebas unitarias con `pytest`. Desde la raíz del proyecto (o dentro del contenedor si estás usando Docker), ejecuta el siguiente comando:

```bash
pytest tests/services/test_auth_services.py
```

Esto ejecutará las pruebas definidas en el archivo correspondiente. Puedes adaptar el path para correr todas las pruebas o pruebas específicas según lo necesites.

---

## 📅 Autor y Licencia

- Autor: Equipo de Desarrollo Backend Events
- Licencia: MIT
