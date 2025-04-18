class MackupsSwagger:
        
    GET_SESSION = {
        'tags': ['Sesiones'],
        'summary': 'Obtener sesiones por ID de evento',
        'description': 'Este endpoint retorna una lista de sesiones asociadas a un evento específico.',
        'parameters': [
            {
                'name': 'event_id',
                'in': 'query',
                'type': 'integer',
                'required': True,
                'description': 'ID del evento del cual se desean obtener las sesiones'
            }
        ],
        'responses': {
            200: {
                'description': 'Sesiones obtenidas exitosamente',
                'examples': {
                    'application/json': {
                        "message": "Session data returned successfully",
                        "data": [
                            {
                                "id": 3,
                                "title": "Taller de Introducción a Flask",
                                "description": "Taller de Introducción a Flask",
                                "start_time": "2025-04-15T09:00:00",
                                "end_time": "2025-04-15T11:00:00",
                                "capacity": 40,
                                "event_id": 1,
                                "speaker_id": 10
                            }
                        ],
                        "errors": {},
                        "status": 200
                    }
                }
            },
            400: {
                'description': 'Solicitud inválida',
                'examples': {
                    'application/json': {
                        "message": "Parámetro event_id es requerido",
                        "data": {},
                        "errors": {"event_id": "Falta el parámetro"},
                        "status": 400
                    }
                }
            },
            401: {
                'description': 'No autorizado',
                'examples': {
                    'application/json': {
                        "message": "Token inválido o no proporcionado",
                        "data": {},
                        "errors": {"auth": "Token inválido"},
                        "status": 401
                    }
                }
            },
            500: {
                'description': 'Error interno del servidor',
                'examples': {
                    'application/json': {
                        "message": "Error inesperado del servidor",
                        "data": {},
                        "errors": {"server": "Ha ocurrido un error inesperado"},
                        "status": 500
                    }
                }
            }
        }
    }
        
    LOGIN = {
        'tags': ['Auth'],
        'summary': 'Login de usuario',
        'description': 'Este endpoint permite al usuario autenticarse y obtener un token JWT.',
        'parameters': [
            {
                'name': 'body',
                'in': 'body',
                'required': True,
                'schema': {
                    'type': 'object',
                    'properties': {
                        'email': {
                            'type': 'string',
                            'example': 'test@gmail.com'
                        },
                        'password': {
                            'type': 'string',
                            'example': 'password_1254521214'
                        }
                    },
                    'required': ['email', 'password']
                }
            }
        ],
        'responses': {
            200: {
                'description': 'Login exitoso',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'message': {
                            'type': 'string',
                            'example': 'Successful Login'
                        },
                        'data': {
                            'type': 'object',
                            'properties': {
                                'access_token': {
                                    'type': 'string',
                                    'example': 'JWT_TOKEN_AQUI'
                                },
                                'email': {
                                    'type': 'string',
                                    'example': 'test@gmail.com'
                                }
                            }
                        },
                        'errors': {
                            'type': 'object',
                            'example': {}
                        },
                        'status': {
                            'type': 'integer',
                            'example': 200
                        }
                    }
                }
            },
            400: {
                'description': 'Credenciales inválidas u otros errores',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'message': {
                            'type': 'string',
                            'example': 'Invalid credentials'
                        },
                        'data': {
                            'type': 'object',
                            'example': {}
                        },
                        'errors': {
                            'oneOf': [
                                {
                                    'type': 'object',
                                    'example': {
                                        'email': 'Correo no registrado'
                                    }
                                },
                                {
                                    'type': 'array',
                                    'items': {
                                        'type': 'string'
                                    },
                                    'example': ['Error 1', 'Error 2']
                                }
                            ]
                        },
                        'status': {
                            'type': 'integer',
                            'example': 400
                        }
                    }
                }
            }
        }
    }


    CREATE_USER = {
        'tags': ['Users'],
        'summary': 'Crear un nuevo usuario',
        'description': 'Este endpoint crea un nuevo usuario y devuelve la respuesta con un formato estructurado.',
        'parameters': [
            {
                'name': 'body',
                'in': 'body',
                'required': True,
                'schema': {
                    'type': 'object',
                    'properties': {
                        'email': {
                            'type': 'string',
                            'example': 'test1@gmail.com'
                        },
                        'password': {
                            'type': 'string',
                            'example': 'password_1254521214'
                        }
                    },
                    'required': ['email', 'password']
                }
            }
        ],
        'responses': {
            201: {
                'description': 'Usuario creado exitosamente',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'message': {
                            'type': 'string',
                            'example': 'User created successfully'
                        },
                        'data': {
                            'type': 'array',
                            'items': {
                                'type': 'object',
                                'properties': {
                                    'id': {
                                        'type': 'string',
                                        'example': 'test1@gmail.com'
                                    }
                                }
                            }
                        },
                        'errors': {
                            'type': 'object',
                            'example': {}
                        },
                        'status': {
                            'type': 'integer',
                            'example': 201
                        }
                    }
                }
            },
            400: {
                'description': 'Error de validación o datos incorrectos',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'message': {
                            'type': 'string',
                            'example': 'Validation failed'
                        },
                        'data': {
                            'type': 'object',
                            'example': {}
                        },
                        'errors': {
                            'oneOf': [
                                {
                                    'type': 'object',
                                    'example': {
                                        'email': 'El correo ya está en uso'
                                    }
                                },
                                {
                                    'type': 'array',
                                    'items': {
                                        'type': 'string'
                                    },
                                    'example': ['El campo email es obligatorio']
                                }
                            ]
                        },
                        'status': {
                            'type': 'integer',
                            'example': 400
                        }
                    }
                }
            },
            401: {
                'description': 'No autorizado',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'message': {
                            'type': 'string',
                            'example': 'Unauthorized'
                        },
                        'data': {
                            'type': 'object',
                            'example': {}
                        },
                        'errors': {
                            'type': 'object',
                            'example': {}
                        },
                        'status': {
                            'type': 'integer',
                            'example': 401
                        }
                    }
                }
            },
            500: {
                'description': 'Error interno del servidor',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'message': {
                            'type': 'string',
                            'example': 'Internal server error'
                        },
                        'data': {
                            'type': 'object',
                            'example': {}
                        },
                        'errors': {
                            'type': 'object',
                            'example': {
                                'trace': 'Stack trace o mensaje de error interno'
                            }
                        },
                        'status': {
                            'type': 'integer',
                            'example': 500
                        }
                    }
                }
            }
        }
    }

    LIST_EVENTS = {
        'tags': ['Events'],
        'summary': 'Obtener lista de eventos',
        'description': 'Este endpoint devuelve una lista paginada de eventos junto con información de paginación.',
        'responses': {
            200: {
                'description': 'Eventos obtenidos exitosamente',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'message': {
                            'type': 'string',
                            'example': 'Event data returned successfully'
                        },
                        'data': {
                            'type': 'object',
                            'properties': {
                                'data': {
                                    'type': 'array',
                                    'items': {
                                        'type': 'object',
                                        'properties': {
                                            'id': {'type': 'integer', 'example': 1},
                                            'title': {'type': 'string', 'example': 'Conferencia de Tecnología 2025'},
                                            'description': {'type': 'string', 'example': 'Descripción del evento'},
                                            'start_date': {'type': 'string', 'format': 'date-time', 'example': '2025-06-10T10:00:00'},
                                            'end_date': {'type': 'string', 'format': 'date-time', 'example': '2025-06-10T18:00:00'},
                                            'capacity': {'type': 'integer', 'example': 120},
                                            'status': {'type': 'string', 'example': 'en curso'}
                                        }
                                    }
                                },
                                'pagination': {
                                    'type': 'object',
                                    'properties': {
                                        'has_next': {'type': 'boolean', 'example': True},
                                        'has_prev': {'type': 'boolean', 'example': False},
                                        'page': {'type': 'integer', 'example': 1},
                                        'per_page': {'type': 'integer', 'example': 20},
                                        'total_items': {'type': 'integer', 'example': 29},
                                        'total_pages': {'type': 'integer', 'example': 2}
                                    }
                                }
                            }
                        },
                        'errors': {
                            'type': 'object',
                            'example': {}
                        },
                        'status': {
                            'type': 'integer',
                            'example': 200
                        }
                    }
                }
            },
            401: {
                'description': 'No autorizado',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'message': {'type': 'string', 'example': 'Unauthorized'},
                        'data': {'type': 'object', 'example': {}},
                        'errors': {'type': 'object', 'example': {}},
                        'status': {'type': 'integer', 'example': 401}
                    }
                }
            },
            500: {
                'description': 'Error interno del servidor',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'message': {'type': 'string', 'example': 'Internal server error'},
                        'data': {'type': 'object', 'example': {}},
                        'errors': {
                            'oneOf': [
                                {'type': 'object', 'example': {'trace': 'Stack trace o mensaje del error'}},
                                {'type': 'array', 'items': {'type': 'string'}, 'example': ['Error inesperado']}
                            ]
                        },
                        'status': {'type': 'integer', 'example': 500}
                    }
                }
            }
        }
    }

    CREATE_EVENT = {
        'tags': ['Events'],
        'summary': 'Crear un nuevo evento',
        'description': 'Este endpoint permite crear un nuevo evento enviando los datos requeridos.',
        'parameters': [
            {
                'name': 'body',
                'in': 'body',
                'required': True,
                'schema': {
                    'type': 'object',
                    'properties': {
                        'title': {'type': 'string', 'example': 'Taller práctico de Python para principiantes'},
                        'description': {'type': 'string', 'example': 'Curso intensivo de introducción a la programación con Python.'},
                        'status': {'type': 'string', 'example': 'programado'},
                        'capacity': {'type': 'integer', 'example': 50},
                        'start_date': {'type': 'string', 'format': 'date-time', 'example': '2025-08-01T09:00:00'},
                        'end_date': {'type': 'string', 'format': 'date-time', 'example': '2025-08-01T13:00:00'}
                    },
                    'required': ['title', 'description', 'status', 'capacity', 'start_date', 'end_date']
                }
            }
        ],
        'responses': {
            201: {
                'description': 'Evento creado exitosamente',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'message': {'type': 'string', 'example': 'Event created successfully'},
                        'data': {
                            'type': 'array',
                            'items': {
                                'type': 'object',
                                'properties': {
                                    'event_id': {'type': 'integer', 'example': 3}
                                }
                            }
                        },
                        'errors': {'type': 'object', 'example': {}},
                        'status': {'type': 'integer', 'example': 201}
                    }
                }
            },
            400: {
                'description': 'Solicitud inválida',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'message': {'type': 'string', 'example': 'Bad Request'},
                        'data': {'type': 'object', 'example': {}},
                        'errors': {
                            'oneOf': [
                                {'type': 'object', 'example': {'field': 'Este campo es obligatorio'}},
                                {'type': 'array', 'items': {'type': 'string'}, 'example': ['El título es obligatorio']}
                            ]
                        },
                        'status': {'type': 'integer', 'example': 400}
                    }
                }
            },
            401: {
                'description': 'No autorizado',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'message': {'type': 'string', 'example': 'Unauthorized'},
                        'data': {'type': 'object', 'example': {}},
                        'errors': {'type': 'object', 'example': {}},
                        'status': {'type': 'integer', 'example': 401}
                    }
                }
            },
            500: {
                'description': 'Error interno del servidor',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'message': {'type': 'string', 'example': 'Internal server error'},
                        'data': {'type': 'object', 'example': {}},
                        'errors': {
                            'oneOf': [
                                {'type': 'object', 'example': {'trace': 'Detalles del error'}},
                                {'type': 'array', 'items': {'type': 'string'}, 'example': ['Error inesperado']}
                            ]
                        },
                        'status': {'type': 'integer', 'example': 500}
                    }
                }
            }
        }
    }

    UPDATE_EVENT = {
        'tags': ['Events'],
        'summary': 'Actualizar un evento existente',
        'description': 'Este endpoint permite actualizar un evento existente mediante su ID.',
        'parameters': [
            {
                'name': 'event_id',
                'in': 'path',
                'type': 'integer',
                'required': True,
                'description': 'ID del evento a actualizar',
                'example': 1
            },
            {
                'name': 'body',
                'in': 'body',
                'required': True,
                'schema': {
                    'type': 'object',
                    'properties': {
                        'title': {'type': 'string', 'example': 'Conferencia de Tecnología 2025 - Edición Actualizada'},
                        'description': {'type': 'string', 'example': 'Actualización del evento con nuevos ponentes confirmados.'},
                        'status': {'type': 'string', 'example': 'en curso'},
                        'capacity': {'type': 'integer', 'example': 120},
                        'start_date': {'type': 'string', 'format': 'date-time', 'example': '2025-06-10T10:00:00'},
                        'end_date': {'type': 'string', 'format': 'date-time', 'example': '2025-06-10T18:00:00'}
                    },
                    'required': ['title', 'description', 'status', 'capacity', 'start_date', 'end_date']
                }
            }
        ],
        'responses': {
            200: {
                'description': 'Evento actualizado exitosamente',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'message': {'type': 'string', 'example': 'Event created successfully'},
                        'data': {
                            'type': 'array',
                            'items': {
                                'type': 'object',
                                'properties': {
                                    'title': {'type': 'string', 'example': 'Conferencia de Tecnología 2025 - Edición Actualizada'},
                                    'description': {'type': 'string', 'example': 'Actualización del evento con nuevos ponentes confirmados.'},
                                    'status': {'type': 'string', 'example': 'en curso'},
                                    'capacity': {'type': 'integer', 'example': 120},
                                    'start_date': {'type': 'string', 'format': 'date-time', 'example': '2025-06-10T10:00:00'},
                                    'end_date': {'type': 'string', 'format': 'date-time', 'example': '2025-06-10T18:00:00'}
                                }
                            }
                        },
                        'errors': {'type': 'object', 'example': {}},
                        'status': {'type': 'integer', 'example': 200}
                    }
                }
            },
            400: {
                'description': 'Solicitud inválida',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'message': {'type': 'string', 'example': 'Bad Request'},
                        'data': {'type': 'object', 'example': {}},
                        'errors': {
                            'oneOf': [
                                {'type': 'object', 'example': {'capacity': 'Debe ser mayor a 0'}},
                                {'type': 'array', 'items': {'type': 'string'}, 'example': ['Campo requerido: title']}
                            ]
                        },
                        'status': {'type': 'integer', 'example': 400}
                    }
                }
            },
            401: {
                'description': 'No autorizado',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'message': {'type': 'string', 'example': 'Unauthorized'},
                        'data': {'type': 'object', 'example': {}},
                        'errors': {'type': 'object', 'example': {}},
                        'status': {'type': 'integer', 'example': 401}
                    }
                }
            },
            500: {
                'description': 'Error interno del servidor',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'message': {'type': 'string', 'example': 'Internal server error'},
                        'data': {'type': 'object', 'example': {}},
                        'errors': {
                            'oneOf': [
                                {'type': 'object', 'example': {'trace': 'Excepción inesperada'}},
                                {'type': 'array', 'items': {'type': 'string'}, 'example': ['Error inesperado']}
                            ]
                        },
                        'status': {'type': 'integer', 'example': 500}
                    }
                }
            }
        }
    }
    DELETE_EVENT = {
        'tags': ['Events'],
        'summary': 'Eliminar un evento existente',
        'description': 'Este endpoint elimina un evento existente según su ID.',
        'parameters': [
            {
                'name': 'event_id',
                'in': 'path',
                'type': 'integer',
                'required': True,
                'description': 'ID del evento a eliminar',
                'example': 3
            }
        ],
        'responses': {
            200: {
                'description': 'Evento eliminado exitosamente',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'message': {'type': 'string', 'example': 'Event Successfully Deleted'},
                        'data': {'type': 'object', 'example': {}},
                        'errors': {'type': 'object', 'example': {}},
                        'status': {'type': 'integer', 'example': 200}
                    }
                }
            },
            400: {
                'description': 'Solicitud inválida',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'message': {'type': 'string', 'example': 'Bad Request'},
                        'data': {'type': 'object', 'example': {}},
                        'errors': {
                            'oneOf': [
                                {'type': 'object', 'example': {'event_id': 'ID no válido'}},
                                {'type': 'array', 'items': {'type': 'string'}, 'example': ['Error en parámetros']}
                            ]
                        },
                        'status': {'type': 'integer', 'example': 400}
                    }
                }
            },
            401: {
                'description': 'No autorizado',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'message': {'type': 'string', 'example': 'Unauthorized'},
                        'data': {'type': 'object', 'example': {}},
                        'errors': {'type': 'object', 'example': {}},
                        'status': {'type': 'integer', 'example': 401}
                    }
                }
            },
            500: {
                'description': 'Error interno del servidor',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'message': {'type': 'string', 'example': 'Internal server error'},
                        'data': {'type': 'object', 'example': {}},
                        'errors': {
                            'oneOf': [
                                {'type': 'object', 'example': {'trace': 'Excepción inesperada'}},
                                {'type': 'array', 'items': {'type': 'string'}, 'example': ['Error inesperado']}
                            ]
                        },
                        'status': {'type': 'integer', 'example': 500}
                    }
                }
            }
        }
    }


    CREATE_SESSION = {
        'tags': ['Sessions'],
        'summary': 'Crear una nueva sesión',
        'description': 'Este endpoint permite crear una nueva sesión asociada a un evento.',
        'requestBody': {
            'required': True,
            'content': {
                'application/json': {
                    'schema': {
                        'type': 'object',
                        'properties': {
                            'title': {'type': 'string', 'example': 'Bases de datos con SQLAlchemy'},
                            'description': {'type': 'string', 'example': 'Bases de datos con SQLAlchemy'},
                            'event_id': {'type': 'integer', 'example': 2},
                            'start_time': {'type': 'string', 'format': 'date-time', 'example': '2025-04-16T10:00:00'},
                            'end_time': {'type': 'string', 'format': 'date-time', 'example': '2025-04-16T12:00:00'},
                            'capacity': {'type': 'integer', 'example': 30},
                            'speaker_id': {'type': 'integer', 'example': 8}
                        },
                        'required': ['title', 'description', 'event_id', 'start_time', 'end_time', 'capacity', 'speaker_id']
                    }
                }
            }
        },
        'responses': {
            201: {
                'description': 'Sesión creada exitosamente',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'message': {'type': 'string', 'example': 'Session created successfully'},
                        'data': {
                            'type': 'array',
                            'items': {
                                'type': 'object',
                                'properties': {
                                    'id': {'type': 'integer', 'example': 4}
                                }
                            }
                        },
                        'errors': {'type': 'object', 'example': {}},
                        'status': {'type': 'integer', 'example': 201}
                    }
                }
            },
            400: {
                'description': 'Error en la solicitud',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'message': {'type': 'string', 'example': 'Bad Request'},
                        'data': {'type': 'object', 'example': {}},
                        'errors': {
                            'oneOf': [
                                {'type': 'object', 'example': {'field': 'Campo requerido faltante'}},
                                {'type': 'array', 'items': {'type': 'string'}, 'example': ['Campo X es obligatorio']}
                            ]
                        },
                        'status': {'type': 'integer', 'example': 400}
                    }
                }
            },
            401: {
                'description': 'No autorizado',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'message': {'type': 'string', 'example': 'Unauthorized'},
                        'data': {'type': 'object', 'example': {}},
                        'errors': {'type': 'object', 'example': {}},
                        'status': {'type': 'integer', 'example': 401}
                    }
                }
            },
            500: {
                'description': 'Error interno del servidor',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'message': {'type': 'string', 'example': 'Internal Server Error'},
                        'data': {'type': 'object', 'example': {}},
                        'errors': {
                            'oneOf': [
                                {'type': 'object', 'example': {'trace': 'Error inesperado'}},
                                {'type': 'array', 'items': {'type': 'string'}, 'example': ['Ocurrió un error inesperado']}
                            ]
                        },
                        'status': {'type': 'integer', 'example': 500}
                    }
                }
            }
        }
    }

    UPDATE_SESSION = {
        'tags': ['Sessions'],
        'summary': 'Actualizar una sesión existente',
        'description': 'Este endpoint actualiza la información de una sesión previamente creada.',
        'parameters': [
            {
                'name': 'session_id',
                'in': 'path',
                'required': True,
                'schema': {'type': 'integer'},
                'description': 'ID de la sesión a actualizar'
            }
        ],
        'requestBody': {
            'required': True,
            'content': {
                'application/json': {
                    'schema': {
                        'type': 'object',
                        'properties': {
                            'title': {'type': 'string', 'example': 'Taller avanzado de Flask'},
                            'start_time': {'type': 'string', 'format': 'date-time', 'example': '2025-04-15T14:00:00'},
                            'end_time': {'type': 'string', 'format': 'date-time', 'example': '2025-04-15T16:00:00'},
                            'event_id': {'type': 'integer', 'example': 1},
                            'speaker_id': {'type': 'integer', 'example': 10},
                            'capacity': {'type': 'integer', 'example': 40}
                        },
                        'required': ['title', 'start_time', 'end_time', 'event_id', 'speaker_id', 'capacity']
                    }
                }
            }
        },
        'responses': {
            200: {
                'description': 'Sesión actualizada exitosamente',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'message': {'type': 'string', 'example': 'Session updated successfully'},
                        'data': {
                            'oneOf': [
                                {'type': 'array', 'items': {'type': 'object', 'example': {}}},
                                {'type': 'object', 'example': {}}
                            ]
                        },
                        'errors': {'type': 'object', 'example': {}},
                        'status': {'type': 'integer', 'example': 200}
                    }
                }
            },
            400: {
                'description': 'Solicitud incorrecta',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'message': {'type': 'string', 'example': 'Bad Request'},
                        'data': {'type': 'object', 'example': {}},
                        'errors': {
                            'oneOf': [
                                {'type': 'object', 'example': {'title': 'Campo obligatorio'}},
                                {'type': 'array', 'items': {'type': 'string'}, 'example': ['Falta el campo title']}
                            ]
                        },
                        'status': {'type': 'integer', 'example': 400}
                    }
                }
            },
            401: {
                'description': 'No autorizado',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'message': {'type': 'string', 'example': 'Unauthorized'},
                        'data': {'type': 'object', 'example': {}},
                        'errors': {'type': 'object', 'example': {}},
                        'status': {'type': 'integer', 'example': 401}
                    }
                }
            },
            500: {
                'description': 'Error interno del servidor',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'message': {'type': 'string', 'example': 'Internal Server Error'},
                        'data': {'type': 'object', 'example': {}},
                        'errors': {
                            'oneOf': [
                                {'type': 'object', 'example': {'detail': 'Error inesperado en la base de datos'}},
                                {'type': 'array', 'items': {'type': 'string'}, 'example': ['Error inesperado']}
                            ]
                        },
                        'status': {'type': 'integer', 'example': 500}
                    }
                }
            }
        }
    }


    DELETE_SESSION = {
        'tags': ['Sessions'],
        'summary': 'Eliminar una sesión',
        'description': 'Elimina una sesión específica mediante su ID.',
        'parameters': [
            {
                'name': 'session_id',
                'in': 'path',
                'required': True,
                'schema': {'type': 'integer'},
                'description': 'ID de la sesión a eliminar'
            }
        ],
        'responses': {
            200: {
                'description': 'Sesión eliminada exitosamente',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'message': {'type': 'string', 'example': 'Session Successfully Deleted'},
                        'data': {
                            'oneOf': [
                                {'type': 'object', 'example': {}},
                                {'type': 'array', 'items': {'type': 'object'}, 'example': [{}]}
                            ]
                        },
                        'errors': {
                            'oneOf': [
                                {'type': 'object', 'example': {}},
                                {'type': 'array', 'items': {'type': 'object'}, 'example': []}
                            ]
                        },
                        'status': {'type': 'integer', 'example': 200}
                    }
                }
            },
            400: {
                'description': 'Solicitud incorrecta',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'message': {'type': 'string', 'example': 'Bad Request'},
                        'data': {'type': 'object', 'example': {}},
                        'errors': {
                            'oneOf': [
                                {'type': 'object', 'example': {'session_id': 'ID inválido'}},
                                {'type': 'array', 'items': {'type': 'string'}, 'example': ['ID inválido']}
                            ]
                        },
                        'status': {'type': 'integer', 'example': 400}
                    }
                }
            },
            401: {
                'description': 'No autorizado',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'message': {'type': 'string', 'example': 'Unauthorized'},
                        'data': {'type': 'object', 'example': {}},
                        'errors': {'type': 'object', 'example': {}},
                        'status': {'type': 'integer', 'example': 401}
                    }
                }
            },
            500: {
                'description': 'Error interno del servidor',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'message': {'type': 'string', 'example': 'Internal Server Error'},
                        'data': {'type': 'object', 'example': {}},
                        'errors': {
                            'oneOf': [
                                {'type': 'object', 'example': {'detail': 'Error inesperado al eliminar'}},
                                {'type': 'array', 'items': {'type': 'string'}, 'example': ['Error inesperado']}
                            ]
                        },
                        'status': {'type': 'integer', 'example': 500}
                    }
                }
            }
        }
    }


    LIST_REGISTERS = {
        'tags': ['Registrations'],
        'summary': 'Obtener registros de eventos',
        'description': 'Retorna una lista de eventos registrados por el usuario autenticado.',
        'responses': {
            200: {
                'description': 'Eventos registrados correctamente',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'message': {'type': 'string', 'example': 'Recorded events'},
                        'data': {
                            'oneOf': [
                                {
                                    'type': 'array',
                                    'items': {
                                        'type': 'object',
                                        'properties': {
                                            'event_id': {'type': 'integer', 'example': 2},
                                            'registered_at': {'type': 'string', 'format': 'date-time', 'example': '2025-04-14T00:46:55.987187'}
                                        }
                                    }
                                },
                                {
                                    'type': 'object',
                                    'example': {}
                                }
                            ]
                        },
                        'errors': {
                            'oneOf': [
                                {'type': 'object', 'example': {}},
                                {'type': 'array', 'items': {'type': 'object'}, 'example': []}
                            ]
                        },
                        'status': {'type': 'integer', 'example': 200}
                    }
                }
            },
            401: {
                'description': 'No autorizado',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'message': {'type': 'string', 'example': 'Unauthorized'},
                        'data': {'type': 'object', 'example': {}},
                        'errors': {'type': 'object', 'example': {}},
                        'status': {'type': 'integer', 'example': 401}
                    }
                }
            },
            500: {
                'description': 'Error interno del servidor',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'message': {'type': 'string', 'example': 'Internal Server Error'},
                        'data': {'type': 'object', 'example': {}},
                        'errors': {
                            'oneOf': [
                                {'type': 'object', 'example': {'detail': 'Error al recuperar registros'}},
                                {'type': 'array', 'items': {'type': 'string'}, 'example': ['Error inesperado']}
                            ]
                        },
                        'status': {'type': 'integer', 'example': 500}
                    }
                }
            }
        }
    }


    CREATE_REGISTERS = {
        'tags': ['Registrations'],
        'summary': 'Registrar usuario a un evento',
        'description': 'Este endpoint permite registrar a un usuario a un evento determinado.',
        'requestBody': {
            'required': True,
            'content': {
                'application/json': {
                    'example': {
                        'event_id': 2
                    }
                }
            }
        },
        'responses': {
            201: {
                'description': 'Registro exitoso',
                'examples': {
                    'application/json': {
                        "message": ["Event registration successful"],
                        "data": [
                            {
                                "id": 1
                            }
                        ],
                        "errors": {},
                        "status": 201
                    }
                }
            },
            400: {
                'description': 'Solicitud inválida',
                'examples': {
                    'application/json': {
                        "message": ["Parámetro event_id inválido"],
                        "data": {},
                        "errors": [{"event_id": "Debe ser un número positivo"}],
                        "status": 400
                    }
                }
            },
            401: {
                'description': 'No autorizado',
                'examples': {
                    'application/json': {
                        "message": ["Token inválido o no proporcionado"],
                        "data": {},
                        "errors": {"auth": "Token inválido"},
                        "status": 401
                    }
                }
            },
            500: {
                'description': 'Error interno del servidor',
                'examples': {
                    'application/json': {
                        "message": ["Error inesperado del servidor"],
                        "data": {},
                        "errors": {"server": "Ha ocurrido un error inesperado"},
                        "status": 500
                    }
                }
            }
        }
    }

    LIST_ROLES = {
        'tags': ['Roles'],
        'summary': 'Obtener lista de roles',
        'description': 'Este endpoint devuelve una lista de roles disponibles en el sistema.',
        'responses': {
            200: {
                'description': 'Roles obtenidos exitosamente',
                'examples': {
                    'application/json': {
                        "message": "Role data returned successfully",
                        "data": [
                            {
                                "id": 1,
                                "name": "ADMIN"
                            },
                            {
                                "id": 2,
                                "name": "ORGANIZER_TEST"
                            }
                        ],
                        "errors": {},
                        "status": 200
                    }
                }
            },
            401: {
                'description': 'No autorizado',
                'examples': {
                    'application/json': {
                        "message": "Token inválido o no proporcionado",
                        "data": {},
                        "errors": {"auth": "Token inválido"},
                        "status": 401
                    }
                }
            },
            500: {
                'description': 'Error interno del servidor',
                'examples': {
                    'application/json': {
                        "message": "Error inesperado del servidor",
                        "data": {},
                        "errors": {"server": "Ha ocurrido un error inesperado"},
                        "status": 500
                    }
                }
            }
        }
    }


    CREATE_ROLES = {
        'tags': ['Roles'],
        'summary': 'Crear un nuevo rol',
        'description': 'Este endpoint permite crear un nuevo rol en el sistema.',
        'requestBody': {
            'required': True,
            'content': {
                'application/json': {
                    'example': {
                        'name': 'TESTER'
                    }
                }
            }
        },
        'responses': {
            201: {
                'description': 'Rol creado exitosamente',
                'examples': {
                    'application/json': {
                        "message": "Role created successfully",
                        "data": [
                            {
                                "id": 3
                            }
                        ],
                        "errors": {},
                        "status": 201
                    }
                }
            },
            400: {
                'description': 'Datos inválidos o faltantes',
                'examples': {
                    'application/json': {
                        "message": "El campo name es obligatorio",
                        "data": {},
                        "errors": {"name": "Este campo no puede estar vacío"},
                        "status": 400
                    }
                }
            },
            401: {
                'description': 'No autorizado',
                'examples': {
                    'application/json': {
                        "message": "Token inválido o no proporcionado",
                        "data": {},
                        "errors": {"auth": "Token inválido"},
                        "status": 401
                    }
                }
            },
            500: {
                'description': 'Error interno del servidor',
                'examples': {
                    'application/json': {
                        "message": "Error inesperado del servidor",
                        "data": {},
                        "errors": {"server": "Ha ocurrido un error inesperado"},
                        "status": 500
                    }
                }
            }
        }
    }

    UPDATE_ROLES = {
        'tags': ['Roles'],
        'summary': 'Actualizar un rol existente',
        'description': 'Este endpoint permite actualizar la información de un rol específico por su ID.',
        'parameters': [
            {
                'name': 'role_id',
                'in': 'path',
                'type': 'integer',
                'required': True,
                'description': 'ID del rol que se desea actualizar'
            }
        ],
        'requestBody': {
            'required': True,
            'content': {
                'application/json': {
                    'example': {
                        'name': 'ORGANIZER_TEST'
                    }
                }
            }
        },
        'responses': {
            200: {
                'description': 'Rol actualizado exitosamente',
                'examples': {
                    'application/json': {
                        "message": "Role updated successfully",
                        "data": [
                            {
                                "id": 2,
                                "name": "ORGANIZER_TEST"
                            }
                        ],
                        "errors": {},
                        "status": 200
                    }
                }
            },
            400: {
                'description': 'Datos inválidos o faltantes',
                'examples': {
                    'application/json': {
                        "message": "El campo name es obligatorio",
                        "data": {},
                        "errors": {"name": "Este campo no puede estar vacío"},
                        "status": 400
                    }
                }
            },
            401: {
                'description': 'No autorizado',
                'examples': {
                    'application/json': {
                        "message": "Token inválido o no proporcionado",
                        "data": {},
                        "errors": {"auth": "Token inválido"},
                        "status": 401
                    }
                }
            },
            500: {
                'description': 'Error interno del servidor',
                'examples': {
                    'application/json': {
                        "message": "Error inesperado del servidor",
                        "data": {},
                        "errors": {"server": "Ha ocurrido un error inesperado"},
                        "status": 500
                    }
                }
            }
        }
    }

    DELETE_ROLES = {
        'tags': ['Roles'],
        'summary': 'Eliminar un rol por ID',
        'description': 'Este endpoint permite eliminar un rol existente del sistema utilizando su ID.',
        'parameters': [
            {
                'name': 'role_id',
                'in': 'path',
                'type': 'integer',
                'required': True,
                'description': 'ID del rol que se desea eliminar'
            },
            {
                'name': 'body',
                'in': 'body',
                'required': False,
                'schema': {
                    'type': 'object',
                    'properties': {
                        'name': {
                            'type': 'string',
                            'example': 'ORGANIZER_TEST'
                        }
                    }
                }
            }
        ],
        'responses': {
            200: {
                'description': 'Rol eliminado exitosamente',
                'examples': {
                    'application/json': {
                        "message": "Role Successfully Deleted",
                        "data": {},
                        "errors": {},
                        "status": 200
                    }
                }
            },
            400: {
                'description': 'Solicitud inválida',
                'examples': {
                    'application/json': {
                        "message": "ID de rol inválido o datos incorrectos",
                        "data": {},
                        "errors": {"role_id": "Debe ser un número válido"},
                        "status": 400
                    }
                }
            },
            401: {
                'description': 'No autorizado',
                'examples': {
                    'application/json': {
                        "message": "Token inválido o no proporcionado",
                        "data": {},
                        "errors": {"auth": "Token inválido"},
                        "status": 401
                    }
                }
            },
            500: {
                'description': 'Error interno del servidor',
                'examples': {
                    'application/json': {
                        "message": "Error inesperado del servidor",
                        "data": {},
                        "errors": {"server": "Ha ocurrido un error inesperado"},
                        "status": 500
                    }
                }
            }
        }
    }


    CREATE_USER_ROLE = {
        'tags': ['Roles'],
        'summary': 'Asociar usuarios a un rol',
        'description': 'Este endpoint asocia uno o más usuarios a un rol específico.',
        'requestBody': {
            'required': True,
            'content': {
                'application/json': {
                    'example': {
                        "role_id": 2,
                        "user_ids": [10]
                    }
                }
            }
        },
        'responses': {
            201: {
                'description': 'Usuarios asociados exitosamente',
                'examples': {
                    'application/json': {
                        "message": "Successfully associated users",
                        "data": [10],
                        "errors": {},
                        "status": 201
                    }
                }
            },
            400: {
                'description': 'Solicitud inválida',
                'examples': {
                    'application/json': {
                        "message": "Faltan campos requeridos",
                        "data": {},
                        "errors": {
                            "role_id": "Este campo es obligatorio",
                            "user_ids": "Debe proporcionar al menos un usuario"
                        },
                        "status": 400
                    }
                }
            },
            401: {
                'description': 'No autorizado',
                'examples': {
                    'application/json': {
                        "message": "Token inválido o no proporcionado",
                        "data": {},
                        "errors": {
                            "auth": "Token inválido"
                        },
                        "status": 401
                    }
                }
            },
            500: {
                'description': 'Error interno del servidor',
                'examples': {
                    'application/json': {
                        "message": "Error inesperado del servidor",
                        "data": {},
                        "errors": {
                            "server": "Ha ocurrido un error inesperado"
                        },
                        "status": 500
                    }
                }
            }
        }
    }


    LIST_USER_ROLE = {
        'tags': ['Roles'],
        'summary': 'Obtener usuarios asociados a un rol',
        'description': 'Este endpoint retorna los usuarios vinculados a un rol específico.',
        'parameters': [
            {
                'name': 'role_id',
                'in': 'query',
                'type': 'integer',
                'required': True,
                'description': 'ID del rol para consultar sus usuarios asociados'
            }
        ],
        'responses': {
            200: {
                'description': 'Listado de usuarios asociados al rol',
                'examples': {
                    'application/json': {
                        "message": "Return list of roles and users",
                        "data": [
                            {
                                "role_id": 1,
                                "role_name": "ADMIN",
                                "user_email": "test@gmail.com",
                                "user_id": 8
                            }
                        ],
                        "errors": {},
                        "status": 200
                    }
                }
            },
            400: {
                'description': 'Solicitud inválida',
                'examples': {
                    'application/json': {
                        "message": "Falta parámetro role_id",
                        "data": {},
                        "errors": {
                            "role_id": "Este parámetro es obligatorio"
                        },
                        "status": 400
                    }
                }
            },
            401: {
                'description': 'No autorizado',
                'examples': {
                    'application/json': {
                        "message": "Token inválido o no proporcionado",
                        "data": {},
                        "errors": {
                            "auth": "Token inválido"
                        },
                        "status": 401
                    }
                }
            },
            500: {
                'description': 'Error interno del servidor',
                'examples': {
                    'application/json': {
                        "message": "Error inesperado del servidor",
                        "data": {},
                        "errors": {
                            "server": "Ha ocurrido un error inesperado"
                        },
                        "status": 500
                    }
                }
            }
        }
    }


    DELETE_USER_ROLE = {
        'tags': ['Roles'],
        'summary': 'Eliminar la relación de usuarios con un rol',
        'description': 'Este endpoint elimina la relación de uno o más usuarios con un rol específico.',
        'requestBody': {
            'required': True,
            'content': {
                'application/json': {
                    'example': {
                        "role_id": 1,
                        "user_ids": [10]
                    }
                }
            }
        },
        'responses': {
            200: {
                'description': 'Relación de usuarios eliminada exitosamente',
                'examples': {
                    'application/json': {
                        "message": "Relationships successfully deleted",
                        "data": [10],
                        "errors": {},
                        "status": 200
                    }
                }
            },
            400: {
                'description': 'Solicitud inválida',
                'examples': {
                    'application/json': {
                        "message": "Faltan parámetros requeridos",
                        "data": {},
                        "errors": {
                            "role_id": "Este campo es obligatorio",
                            "user_ids": "Debe proporcionar al menos un usuario"
                        },
                        "status": 400
                    }
                }
            },
            401: {
                'description': 'No autorizado',
                'examples': {
                    'application/json': {
                        "message": "Token inválido o no proporcionado",
                        "data": {},
                        "errors": {
                            "auth": "Token inválido"
                        },
                        "status": 401
                    }
                }
            },
            500: {
                'description': 'Error interno del servidor',
                'examples': {
                    'application/json': {
                        "message": "Error inesperado del servidor",
                        "data": {},
                        "errors": {
                            "server": "Ha ocurrido un error inesperado"
                        },
                        "status": 500
                    }
                }
            }
        }
    }

    CREATE_ROLE_PERMISSIONS = {
        'tags': ['Roles'],
        'summary': 'Asociar permisos a un rol',
        'description': 'Este endpoint permite asociar uno o más permisos a un rol específico.',
        'requestBody': {
            'required': True,
            'content': {
                'application/json': {
                    'example': {
                        "role_id": 1,
                        "permission_ids": [1]
                    }
                }
            }
        },
        'responses': {
            201: {
                'description': 'Permisos asociados exitosamente al rol',
                'examples': {
                    'application/json': {
                        "message": "Successfully associated permissions",
                        "data": [1],
                        "errors": {},
                        "status": 201
                    }
                }
            },
            400: {
                'description': 'Solicitud inválida',
                'examples': {
                    'application/json': {
                        "message": "Faltan parámetros requeridos",
                        "data": {},
                        "errors": {
                            "role_id": "Este campo es obligatorio",
                            "permission_ids": "Debe proporcionar al menos un permiso"
                        },
                        "status": 400
                    }
                }
            },
            401: {
                'description': 'No autorizado',
                'examples': {
                    'application/json': {
                        "message": "Token inválido o no proporcionado",
                        "data": {},
                        "errors": {
                            "auth": "Token inválido"
                        },
                        "status": 401
                    }
                }
            },
            500: {
                'description': 'Error interno del servidor',
                'examples': {
                    'application/json': {
                        "message": "Error inesperado del servidor",
                        "data": {},
                        "errors": {
                            "server": "Ha ocurrido un error inesperado"
                        },
                        "status": 500
                    }
                }
            }
        }
    }

    DELETE_ROLE_PERMISSIONS = {
        'tags': ['Roles'],
        'summary': 'Eliminar permisos asociados a un rol',
        'description': 'Este endpoint elimina relaciones entre un rol específico y uno o más permisos.',
        'requestBody': {
            'required': True,
            'content': {
                'application/json': {
                    'example': {
                        "role_id": 1,
                        "permission_ids": [1]
                    }
                }
            }
        },
        'responses': {
            200: {
                'description': 'Relaciones eliminadas exitosamente',
                'examples': {
                    'application/json': {
                        "message": "Relationships successfully deleted",
                        "data": [1],
                        "errors": {},
                        "status": 200
                    }
                }
            },
            400: {
                'description': 'Solicitud inválida',
                'examples': {
                    'application/json': {
                        "message": "Parámetros requeridos faltantes",
                        "data": {},
                        "errors": {
                            "role_id": "El campo role_id es obligatorio",
                            "permission_ids": "Debe proporcionar una lista de permisos"
                        },
                        "status": 400
                    }
                }
            },
            401: {
                'description': 'No autorizado',
                'examples': {
                    'application/json': {
                        "message": "Token inválido o no proporcionado",
                        "data": {},
                        "errors": {
                            "auth": "Token inválido"
                        },
                        "status": 401
                    }
                }
            },
            500: {
                'description': 'Error interno del servidor',
                'examples': {
                    'application/json': {
                        "message": "Error inesperado del servidor",
                        "data": {},
                        "errors": {
                            "server": "Ha ocurrido un error inesperado"
                        },
                        "status": 500
                    }
                }
            }
        }
    }


    GET_DETAIL_USER = {
        'tags': ['Roles'],
        'summary': 'Obtener permisos, roles y eventos del usuario autenticado',
        'description': 'Retorna información del usuario autenticado, incluyendo correo, estado, roles y eventos relacionados.',
        'responses': {
            200: {
                'description': 'Información obtenida exitosamente',
                'examples': {
                    'application/json': {
                        "message": "User information obtained successfully",
                        "data": {
                            "active": True,
                            "email": "test@gmail.com",
                            "events": [
                                {
                                    "capacity": 80,
                                    "created_at": "2025-04-13T03:47:03.572038",
                                    "description": "Espacio para el networking entre startups y empresas consolidadas.",
                                    "end_date": "2025-07-15T21:00:00",
                                    "id": 2,
                                    "start_date": "2025-07-15T18:00:00",
                                    "status": "programmed",
                                    "title": "EV2 Encuentro de Empresarios Innovadores"
                                }
                            ],
                            "roles": [
                                {
                                    "name": "ADMIN"
                                }
                            ]
                        },
                        "errors": {},
                        "status": 200
                    }
                }
            },
            401: {
                'description': 'No autorizado',
                'examples': {
                    'application/json': {
                        "message": "Token inválido o no proporcionado",
                        "data": {},
                        "errors": {
                            "auth": "Token inválido"
                        },
                        "status": 401
                    }
                }
            },
            500: {
                'description': 'Error interno del servidor',
                'examples': {
                    'application/json': {
                        "message": "Error inesperado del servidor",
                        "data": {},
                        "errors": {
                            "server": "Ha ocurrido un error inesperado"
                        },
                        "status": 500
                    }
                }
            }
        }
    }
