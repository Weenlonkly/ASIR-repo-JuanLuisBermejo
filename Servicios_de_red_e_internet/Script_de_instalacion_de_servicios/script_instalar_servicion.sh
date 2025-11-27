#!/bin/bash

# Script de instalacion de servicios 

clear
echo ".-------------------------------------------------------------."
echo ".------------- MENU INSTALACIÓN DE SERVICIOS -----------------."
echo ".-------------------------------------------------------------."
echo "1) Instalar SSH"
echo "2) Instalar Apache2"
echo "3) Instalar MYSQL"
echo "4) Instalar PHP y extensiones comunes"
echo "5) Instalar FTP (vsftpd)"
echo "6) Copia seguridad WEB (/var/www/html)"
echo "7) Copia Bases de Datos (Todas)"
echo "8) Actualizar repositorio y paquetes"
echo "9) Apagar equipo"
echo "0) Salir del Script"
echo ".-------------------------------------------------------------."
echo "Dame una opción:"
read -p "Pon un numero del 0 al 9: " opcion

case $opcion in
    1)
        echo "Instalando SSH...."
        sudo apt install ssh -y
        echo "Instalación completa, pulse cualquier tecla para continuar"
        read
    ;;
    2)
        echo "Instalar servidor Web Apache2"
        sudo apt install apache2 -y
        echo "Instalación completa, pulse cualquier tecla para continuar"
        read
    ;;
    3)
        echo "Instalando MYSQL Server"
        sudo apt install mysql-server -y
        echo "Instalación completa. Recuerda ejecutar 'sudo mysql_secure_installation' para configurarlo."
        read
    ;;
    4)
        echo "Instalando PHP y extensiones comunes (para Apache y MySQL)"
        sudo apt install php libapache2-mod-php php-mysql -y
        echo "Instalación completa, pulse cualquier tecla para continuar"
        read
    ;;
    5)
        echo "Instalando Servidor FTP (vsftpd)"
        sudo apt install vsftpd -y
        echo "Instalación completa. Recuerda configurar el archivo /etc/vsftpd.conf"
        read
    ;;
    6)
        echo "Realizando Copia de seguridad de WEB (/var/www/html)"
        sudo tar -czvf ~/web_backup_.tar.gz /var/www/html
        echo "Copia de seguridad WEB completada. Guardada en: ~/web_backup_$.tar.gz"
        read
    ;;
    7)
        echo "Realizando Copia de seguridad de TODAS las Bases de Datos MySQL"
        read -sp "Introduce la contraseña de root de MySQL: " MYSQL_ROOT_PASSWORD
        echo ""
        sudo mysqldump -u root -p$MYSQL_ROOT_PASSWORD --all-databases | gzip > ~/mysql_all_dbs_.sql.gz
        echo "Copia de Bases de Datos completada. Guardada en: ~/mysql_all_dbs_.sql.gz"
        read
    ;;
    8)
        echo "Actualizando lista de repositorios (apt update)..."
        sudo apt update
        echo "Actualizando paquetes instalados (apt upgrade)..."
        sudo apt upgrade -y
        echo "Actualización completa, pulse cualquier tecla para continuar"
        read
    ;;
    9)
        echo "Apagando el equipo inmediatamente..."
        sudo shutdown
        read
    ;;
    0)
        echo "Saliendo del Script..."
        exit 0
    ;;
    *)
        echo "Opción no válida. Por favor, selecciona un número del 0 al 9."
        read
    ;;
esac
