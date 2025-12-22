# Usar imagen oficial de Python 3.11
FROM python:3.11-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Actualizar pip
RUN pip install --upgrade pip

# Copiar requirements.txt
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación
COPY . .

# Exponer puerto 8000
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["python", "main.py"]
