# Introduccion a json

# Por Juan Luis Bermejo

# Como la clase no ha dado para toda la explicacion, el profesor ha dicho que entreguemos lo que hayamos hecho.

## Lo que se ha hecho durante la clase ha sido la creacion de un archivo .json con el siguiente contenido

{
  "nombre": "Ana",
  "edad": 30,
  "skills": ["bash", "python", "jq"],
  "direccion": { "ciudad": "Madrid", "cp": "28001" },
  "usuarios": [
    { "nombre": "Ana", "edad": 30 },
    { "nombre": "Luis", "edad": 22 }
  ]
}

# Despues se ha instalado jq que lee los archivos con estructura json en linux y macos

sudo apt install jq

# Teniendo jq y e larchivo .json hemos probado los comandos de jq para leer los datos del .json

## Despues se han probado y comprendido el funcionamiento de los siguientes 2 scripts 

------------------------------------------------------------------------------------------------

#!/usr/bin/env bash
file="datos.json"
nombre=$(jq -r '.nombre' "$file")
ciudad=$(jq -r '.direccion.ciudad' "$file")

mapfile -t skills < <(jq -r '.skills[]' "$file")

echo "Nombre: $nombre"
echo "Ciudad: $ciudad"
echo "Skills:"
for s in "${skills[@]}"; do
  echo " - $s"
done

------------------------------------------------------------------------------------------------

#!/usr/bin/env bash
# =============================================
# Script: leer_json.sh
# Descripción: Comprueba si jq está instalado.
#              Si no lo está, lo instala (Ubuntu/Raspbian)
#              y luego lee datos desde un archivo JSON.
# =============================================

# Colores para hacerlo más legible
verde="\e[32m"
rojo="\e[31m"
amarillo="\e[33m"
reset="\e[0m"

# --- 1) Comprobar si jq está instalado ---
echo -e "${amarillo}Comprobando si jq está instalado...${reset}"

if ! command -v jq &> /dev/null; then
    echo -e "${rojo}jq no está instalado.${reset}"

    # Detectar si es Ubuntu o Raspbian
    if grep -qi "ubuntu" /etc/os-release || grep -qi "raspbian" /etc/os-release; then
        echo -e "${amarillo}Sistema Ubuntu o Raspbian detectado.${reset}"
        echo "Instalando jq..."
        sudo apt update && sudo apt install -y jq
    else
        echo -e "${rojo}Este script solo instala jq automáticamente en Ubuntu o Raspbian.${reset}"
        echo "Instálalo manualmente con: sudo apt install jq"
        exit 1
    fi

    # Verificar que jq se haya instalado correctamente
    if ! command -v jq &> /dev/null; then
        echo -e "${rojo}Error: jq no se pudo instalar correctamente.${reset}"
        exit 1
    fi
else
    echo -e "${verde}jq ya está instalado.${reset}"
fi

# --- 2) Leer datos de un archivo JSON ---
json_file="datos.json"

if [ ! -f "$json_file" ]; then
    echo -e "${rojo}No se encuentra el archivo ${json_file}.${reset}"
    echo "Crea un archivo con contenido como este:"
    echo '{
  "nombre": "Ana",
  "edad": 30,
  "skills": ["bash", "python", "jq"],
  "direccion": { "ciudad": "Madrid", "cp": "28001" }
}'
    exit 1
fi

# --- 3) Extraer información usando jq ---
nombre=$(jq -r '.nombre' "$json_file")
edad=$(jq -r '.edad' "$json_file")
ciudad=$(jq -r '.direccion.ciudad' "$json_file")

# Leer array como lista
mapfile -t skills < <(jq -r '.skills[]' "$json_file")

# --- 4) Mostrar resultados ---
echo -e "\n${verde}=== Datos del archivo JSON ===${reset}"
echo "Nombre: $nombre"
echo "Edad: $edad"
echo "Ciudad: $ciudad"
echo "Skills:"
for s in "${skills[@]}"; do
  echo " - $s"
done

echo -e "\n${verde}Lectura completada correctamente.${reset}"

------------------------------------------------------------------------------------------------

## De entre lo mas importante esta el uso de

&> /dev/null

## Anula las respuestas del sistema 
