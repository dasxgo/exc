## Usar una imagen base de Python
FROM python:3.8

## Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

## Copiar el archivo de requisitos al directorio de trabajo
COPY requirements.txt .

## Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

## Copiar el resto de los archivos al directorio de trabajo
COPY . .

## Exponer el puerto en el que la aplicación va a escuchar
EXPOSE 80

## Comando para ejecutar la aplicación cuando se inicie el contenedor
CMD ["python", "app.py"]
Asegúrate de tener un archivo llamado requirements.txt en el mismo directorio que este Dockerfile. En este archivo, listas las dependencias de Python necesarias para tu aplicación. Además, el ejemplo asume que tu archivo principal de la aplicación se llama app.py, por lo que debes ajustar el nombre si es diferente.

Luego, para construir la imagen de Docker, asegúrate de estar en el mismo directorio que el Dockerfile y ejecuta el siguiente comando en tu terminal:

bash
Copy code
docker build -t nombre-de-tu-imagen .
Reemplaza nombre-de-tu-imagen con el nombre que quieras darle a tu imagen.

Una vez que la imagen esté construida, puedes ejecutar un contenedor basado en ella con el siguiente comando:

bash
Copy code
docker run -p 8080:80 nombre-de-tu-imagen
Esto mapeará el puerto 8080 de tu máquina host al puerto 80 dentro del contenedor, donde tu aplicación Flask estará escuchando.

Recuerda ajustar el Dockerfile y los comandos según las necesidades específicas de tu aplicación.





