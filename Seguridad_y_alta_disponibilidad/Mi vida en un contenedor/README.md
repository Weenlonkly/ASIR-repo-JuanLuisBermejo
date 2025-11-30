# Mi vida en un contenedor (Retos Docker)
Juan luis bermejo


## Reto 1

### Crear un contenedor docker de ubuntu.

#### Primero asegurar que tienes la imagen de ubuntu necesaria

docker images

#### Si no la tenemos hay que descargarla

docker pull ubuntu:latest

#### Y se crea el contenedor

docker run -it --name contenedor-reto1 ubuntu:latest


### Instalar python, la libreria request y de mysql

#### Dentro del contenedor hay que descargar lo que pide el reto

#### Python

apt install python3 -y

- A parte pyzon pide una configuracion extra sobre tzdata

#### Librerias

apt install python3-pip -y
apt install python3-requests -y

#### Mysql

apt install mysql-client -y
apt install python3-mysql.connector -y
apt install python3-mysqldb -y

### Crear una imgane personalizada con el contenedor

#### Para el segundo reto creamos una carpeta llamada python con la siguiente ruta:

/home/ubuntu/python

#### Salimos del contenedor

docker commit contenedor-reto1 imagen-reto1

## Reto 2

### Crear un contenedor nuevo con la imagen personalizada  de docker
### Este contenedor tendra un volumen con una ruta en el disco del anfitrión (Bind)

#### Fuera del contenedor

docker run --name  reto_ubuntu_python -it -v /home/juanl/volumenes/contenedor-reto1:/home/ubuntu/python imagen-reto1

## Reto 3

### Crear un repositorio git en la carpeta del anfitrión y unirlo con un repositorio en Github

touch hola.txt
echo "Hola Mundo" > hola.txt

### Descargamos git

apt install git -y

### Hacemos la configuracion inicial de global y luego lo iniciamos 

- Tambien es importante tener la carpeta python como directorio seguro para git para que no haga preguntas innecesarias a la hora de subirlo

git config --global --add safe.directory /home/ubuntu/python
git init 

### Y subir el archivo a github

git add hola.txt
git commit -m "reto3 contenedor"
git branch -M main
git remote add origin https://github.com/Weenlonkly/ASIR-repo-JuanLuisBermejo/tree/main/Seguridad_y_alta_disponibilidad/Mi%20vida%20en%20un%20contenedor/python

#### No se porque pero despues de unos cuantos errores y consultas en la IA he podido hacer el push

git push -u origin main

## Reto 4

### Crear un contenedor mysql.

docker pull mysql:latest

docker run --name mysql_server -d \
-e MYSQL_ROOT_PASSWORD=Abcd1234 \
-e MYSQL_DATABASE=bdcoches \
-p 3307:3306 \
-v mysql_data:/var/lib/mysql \
mysql:latest

### Crear una base de datos, para almacenar Coches. Los campos seran id, marca, modelo, color, km y precio

docker exec -it mysql_server bash
mysql -u root -p

CREATE TABLE vehiculos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    marca VARCHAR(50) NOT NULL,
    modelo VARCHAR(50) NOT NULL,
    color VARCHAR(30),
    km INT,
    precio DECIMAL(10,2)
);

### añadir almenos 10 coches a modo de contenido de muestra.

INSERT INTO vehiculos (marca, modelo, color, km, precio) VALUES
('Toyota', 'Corolla', 'Blanco', 45000, 12500.00),
('Honda', 'Civic', 'Negro', 38000, 13800.00),
('Ford', 'Focus', 'Azul', 60000, 9900.00),
('Chevrolet', 'Cruze', 'Gris', 52000, 11200.00),
('Nissan', 'Sentra', 'Rojo', 47000, 11900.00),
('Volkswagen', 'Jetta', 'Plata', 41000, 13400.00),
('Hyundai', 'Elantra', 'Verde', 55000, 10800.00),
('Kia', 'Rio', 'Blanco', 30000, 10200.00),
('Mazda', '3', 'Negro', 36000, 14200.00),
('Renault', 'Megane', 'Azul', 65000, 8800.00);

## Reto 5

### Tener python instalado

sudo apt install python3-pip -y

### Para instalar el conector de python hay que hacer un par de pasos

sudo apt install python3-venv python3-full -y
python3 -m venv venv
source venv/bin/activate

### Despues de activarlo se vera:

(venv) juanl@juanl:~$

### Instalamos el conector

pip install mysql-connector-python

### Se crea el archivo python

nano mostrar_coches.py

### El archivo es el mismo que el anexo llamado "mostrar_coches.py"

### Despues de ejecutarlo se puede ver la consulta a la tabla de la base de datos

## Reto 6

### se crea el archivo .json

nano config.json

### El archivo es el mismo que el anexo llamado "config.json"

#### commit 1
git add config.json
git commit -m "Agregar archivo config.json con datos de conexión"

### se crea un archivo similar a "mostrar_coches.py" llamado "mostrar_coches_json.py"

nano mostrar_coches_json.json

### El archivo es el mismo que el anexo llamado "mostrar_coches_json.py"

#### commit 2
git add mostrar_coches_json.py
git commit -m "Programa Python que lee configuración desde archivo JSON"

### Cree el archivo .gitignore
### El archivo es el mismo que el anexo llamado ".gitignore"

#### commit 3
git add .gitignore
git commit -m "Agregar .gitignore para excluir archivo config.json y entorno virtual"

### Eliminar "config.json"

git rm --cached config.json
git commit -m "Eliminar config.json del repositorio por seguridad"

### Despues se puede probar que funciona

python mostrar_coches_json.py


## Reto 7

### El ultimo "mostrar_coches_json.py" ya ha sido cambiado, al igual que el archivo "mostrar_coches.py"

## Reto 8

### Crear un conetenedor Mongo y conectarse desde la terminal y utilizando MongoDB

#### Primero se hace un pull de la imagen de mongo

docker pull mongo:latest

#### Se hace un run de la imagen

docker run -d \
--name mongo_retos \
-p 27017:27017 \
-v mongo_data:/data/db \
mongo:latest

#### Abrimos el contenedor

docker exec -it mongo_retos bash

### Crea la una bd e inserta en una colecci'on coches con el criterio de de campos del reto anterior

#### Creamos la base de datos

use bdcoches

#### Se insertan los datos

db.coches.insertMany([
  {marca: "Toyota", modelo: "Corolla", color: "Blanco", km: 45000, precio: 12500},
  {marca: "Honda", modelo: "Civic", color: "Negro", km: 38000, precio: 13800},
  {marca: "Ford", modelo: "Focus", color: "Azul", km: 60000, precio: 9900},
  {marca: "Chevrolet", modelo: "Cruze", color: "Gris", km: 52000, precio: 11200},
  {marca: "Nissan", modelo: "Sentra", color: "Rojo", km: 47000, precio: 11900},
  {marca: "Volkswagen", modelo: "Jetta", color: "Plata", km: 41000, precio: 13400},
  {marca: "Hyundai", modelo: "Elantra", color: "Verde", km: 55000, precio: 10800},
  {marca: "Kia", modelo: "Rio", color: "Blanco", km: 30000, precio: 10200},
  {marca: "Mazda", modelo: "3", color: "Negro", km: 36000, precio: 14200},
  {marca: "Renault", modelo: "Megane", color: "Azul", km: 65000, precio: 8800}
])


#### Comprobacion

db.coches.find().pretty()

### Crear un Script de Python  para leer los datos de colecciones de MongoDB y los imprima en una tabla.

nano mostrar_coches_mongo.py

#### El archivo es el mismo que el anexo llamado "mostrar_coches_mongo.py"

#### Al ejecutarlo nos devuelve 

+------------+---------+--------+-------+--------+
|   Marca    |  Modelo | Color  |   KM  | Precio |
+------------+---------+--------+-------+--------+
|   Toyota   | Corolla | Blanco | 45000 | 12500  |
|   Honda    |  Civic  | Negro  | 38000 | 13800  |
|    Ford    |  Focus  |  Azul  | 60000 |  9900  |
| Chevrolet  |  Cruze  |  Gris  | 52000 | 11200  |
|   Nissan   |  Sentra |  Rojo  | 47000 | 11900  |
| Volkswagen |  Jetta  | Plata  | 41000 | 13400  |
|  Hyundai   | Elantra | Verde  | 55000 | 10800  |
|    Kia     |   Rio   | Blanco | 30000 | 10200  |
|   Mazda    |    3    | Negro  | 36000 | 14200  |
|  Renault   |  Megane |  Azul  | 65000 |  8800  |
+------------+---------+--------+-------+--------+


## Reto 9



### No tenia parrot asi que lo he descargado en kali

### Descargado docker he hecho un pull de la imagen subida a docker
