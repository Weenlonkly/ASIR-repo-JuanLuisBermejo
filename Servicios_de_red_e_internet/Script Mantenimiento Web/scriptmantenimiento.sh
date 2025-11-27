#!/bin/bash

carpeta_backups="/var/www/copias_de_seguridad"
nombre_db="test"

date=$(date +%Y%m%d_%H%M%S)

copia_db="${nombre_db}_${date}.sql.gz"
copia_html="web_html_${date}.tar.gz"

# Crear carpeta si no existe
mkdir -p "$carpeta_backups"

# Backup web
tar -czf "${carpeta_backups}/${copia_html}" /var/www/html

# Backup base de datos
mysqldump "$nombre_db" | gzip > "${carpeta_backups}/${copia_db}"
