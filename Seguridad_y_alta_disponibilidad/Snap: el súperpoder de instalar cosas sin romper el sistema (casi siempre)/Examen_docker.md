# Bloque 1 – Gestión básica de imágenes y contenedores (3 puntos)

## 1 Muestra las imágenes que tienes actualmente en tu sistema Docker.

docker images

## 2 Descarga la imagen oficial de MySQL desde Docker Hub.

### El codigo viene de docker hub de donde se copia el codigo

docker pull mysql

## 3 Muestra todas las imágenes disponibles de nuevo para comprobar que la imagen de MySQL se ha descargado.

### Se vuleve a poner el mismo comando y mostrara la nueva imagen

odcker images

## 4 Muestra todos los contenedores en ejecución.

docker ps

## 5 Muestra todos los contenedores, incluyendo los detenidos.

docker ps -a

------------------------------------------------------------------------------------------------------------------------------

# Bloque 2 – Volúmenes y contenedores (3 puntos)


## 6 Crea un volumen llamado mysql_data.

docker volume create mysql_data

## 7 Muestra todos los volúmenes disponibles en tu sistema.

docker volume ls

## 8 Arranca un contenedor llamado mibasedatos usando la imagen mysql, montando el volumen mysql_data en /var/lib/mysql, y definiendo las variables de entorno:
MYSQL_ROOT_PASSWORD=admin123
MYSQL_DATABASE=tienda


### El comando para crearlo con todo a la vez:

docker run --name mibasedatos -it -v mysql_data:/var/lib/mysql mysql

### Los comandos que definen las variables no los se, desde docker desktop en el partado de variables se copia el siguiente texto en cada slot de variable y ya 

MYSQL_ROOT_PASSWORD=admin123
MYSQL_DATABASE=tienda

## 9 Comprueba que el contenedor está corriendo.

docker ps

### Muestra todos los contenedores que estan corriendo

## 10 Accede al contenedor con una terminal interactiva bash.

docker exec -it mibasedatos bash

## 11 Sal de la terminal sin detener el contenedor.

exit

## 12 Detén el contenedor.

docker stop mibasedatos

## 13 Elimina el contenedor.

docker rm mibasedatos

------------------------------------------------------------------------------------------------------------------------------

# Bloque 3 – Creación de imágenes personalizadas (2 puntos)

## 14 Crea un directorio llamado miimagen.

mkdir miimagen

## 15 Dentro de ese directorio, crea un archivo Dockerfile que:

Use ubuntu:latest como base.
Instale curl y vim.
Establezca /app como directorio de trabajo.
Copie un archivo index.html local a /app.
Ejecute bash por defecto.

### Primero hay que entrar en la carpeta

cd miimagen


## 16 Construye la imagen con el nombre mialumno/ubuntu_custom:1.0.

docker commit mialumno/ubuntu_custom:1.0 miimagen

## 17 Muestra todas las imágenes y comprueba que la nueva aparece.

docker images


------------------------------------------------------------------------------------------------------------------------------

# Bloque 4 – Publicación en Docker Hub (2 puntos)

## 18 Inicia sesión en Docker Hub desde la terminal.

docker login

## 19 Sube la imagen mialumno/ubuntu_custom:1.0 a tu cuenta de Docker Hub.

docker push mialumno/ubuntu_custom:1.0

## 20 Comprueba que la subida ha sido correcta listando tus imágenes locales.

docker images

------------------------------------------------------------------------------------------------------------------------------

# Bonus (0,5 puntos extra)
## 21 Muestra el tamaño total ocupado por tus imágenes y contenedores.

## 22 Elimina todas las imágenes y contenedores que no estén en uso.

docker images prune -a
docker container prune -a
