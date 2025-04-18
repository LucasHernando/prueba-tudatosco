# 1. Imagen base ligera de Python
FROM python:3.12

## 2) Directorio de trabajo
WORKDIR /src/src

# 3) Instala dependencias primero para cachear
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4) Copia el resto del código
COPY . .

# 5) Variables de entorno para Flask CLI y runtime
#    - FLASK_APP=app:create_app → importa app.py y ejecuta create_app()
#    - FLASK_ENV=production  → modo prod
ENV FLASK_APP=app:create_app \
    FLASK_ENV=production \
    FLASK_RUN_HOST=0.0.0.0 \
    FLASK_RUN_PORT=8082 \
    PYTHONUNBUFFERED=1

# 6) Exponer el puerto
EXPOSE 8082

# 7) Al iniciar:
#    a) flask db upgrade  → aplica las migraciones
#    b) flask seed        → ejecuta tu comando custom de seed
#    c) flask run         → levanta la aplicación
#CMD ["sh", "-c", "\
#    flask db upgrade && \
#    flask seed && \
#    flask run --host=${FLASK_RUN_HOST} --port=${FLASK_RUN_PORT} \
#"]

CMD ["sh", "-c", "flask run --host=${FLASK_RUN_HOST} --port=${FLASK_RUN_PORT}"]