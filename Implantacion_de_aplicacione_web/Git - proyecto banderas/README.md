# Documentacion del Proyecto banderas
## Juan Luis Bermejo Nogueira

#### Aviso el proyecto banderas no ha podido ser completado 

# Se instala git

sudo apt install gitk -y

### Tambien hay que instalar apache2 pero mi sistema tenia ya instalado apache asi que solo habia que revisar el status

sudo apt install apache2
sudo systemctl status apache2

## Nos vamos a la carpeta de trabajo de apache

cd /var/www/html

### Se borra cualquier cosa que hubiese antes en esa carpeta

sudo rm -rf *

### Se le dan los derechos al usuario sobre la carpeta

sudo chown -R $USER:$USER /var/www/html

## Se inicia GIT 

sudo git init

# se añade esto al index.html en vez de lo que habia antes

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bandera</title>
    <style>
        body {
            margin: 0;
            padding: 0;
        }
        .franja {
            height: 100px;
            width: 100%;
        }
    </style>
</head>
<body>
    <div class="franja" style="background-color: red;"></div>
    <div class="franja" style="background-color: yellow;"></div>
    <div class="franja" style="background-color: red;"></div>
</body>
</html>


# Commits

## Empezamos a subir commits al git

### primero el de la bandera de españa

git add index.html

git commit -m "Añade la bandera inicial (España)"

### segundo el de la bandera de italia

<div class="franja" style="background-color: green;"></div>
<div class="franja" style="background-color: white;"></div>
<div class="franja" style="background-color: red;"></div>

git add index.html git commit -m "Cambia los colores para la bandera de Italia"

### tercero el de la bandera de francia

git add index.html git commit -m "Cambia los colores para la bandera de Francia"

### Creamos una branch para italia

#### Luego se repite para francia y alemania

git checkout -b italia

git add index.html git commit -m "Crea la bandera de Italia en la rama italia"





#### Al hacer los commit me ha dado unos errores que ni con la ayuda de la IA no he sabido solucionar

### De todas las maneras en la pagina de apache se pueden ver las distintas banderas añadidas por los distintos commit, pero me da error para subirlo a github
