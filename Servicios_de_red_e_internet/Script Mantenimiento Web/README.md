# Para hecer que funcione el script de forma diaria

## Crontab 

Crontab es una servicio de ubuntu/devian para hacer que se ejecuten cosas de forma periodica

### Entrar en crontab

sudo crontab -e

### Añadir la nueva regla a crontab para que lo ejecute cada dia

0 0 * * * /ruta/backup.sh

## 
