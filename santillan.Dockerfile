# Imagen base de Python
FROM python:3.10-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar todos los archivos del proyecto al contenedor
COPY . .

# Instalar dependencias
RUN pip install -r requirements.txt

# Exponer puerto si la app lo usa
EXPOSE 3000

# Comando para ejecutar la app
CMD ["python", "app.py"]
