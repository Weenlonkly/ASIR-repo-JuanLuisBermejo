# Practica Grafana

## Monitorizacion con raspberrys
## Con un router + un switch + varias Raspberry Pi por cable puedes montar un mini-NOC en clase: una Pi “servidora” con Grafana (y Prometheus) y el resto como “nodos” a monitorizar.

# Autores: Sergio Chamba y Juan Luis Bermejo



# 1 Preparacion y pasos previos

## Router

### Saber el SSID y la contraseña para las raspberrys

## Raspberrys

### Estamos usando las Raspberrys PI 4
### Usando el programa 'Raspberry PI Imager' se instalan en las raspberrys los sistemas operativos

### De las configuraciones:

Nombre Raspberry        Ips(asignadas mediante DHCP)

Server1     rp1G3-srv   192.168.1.121
Cliente2    rp2G3       192.168.1.193
cliente3    rp3G3       192.168.1.160

### Todos los usuarios y las contraseñas son iguales

Usuario     pi
Contraseña  Asir_2025

### Configurar LAN inalambrica (se necesita el SSID y la contraseña de la red)

### Hablitar el servicio SSH



# 2 Raspberry Servidor

## Instalar Prometheus

sudo apt update sudo apt install prometheus

### Editar el archivo prometheus.yml para añadir los nodos que se quieran monitorizar

/etc/prometheus/prometheus.yml

  - job_name: 'rpi-nodes'
    static_configs:
      - targets: ['192.168.1.193:9100', '192.168.1.160:9100']

### Guardar y reiniciar el servidor

sudo systemctl restart prometheus && sudo systemctl status prometheus

### Comprobar que funciona correctamente desde el navegador

http://192.168.1.121:9090

## Instalar Grafana

sudo apt install -y apt-transport-https software-properties-common
sudo mkdir -p /etc/apt/keyrings/
wget -q -O - https://packages.grafana.com/gpg.key | sudo gpg --dearmor -o /etc/apt/keyrings/grafana.gpg
echo "deb [signed-by=/etc/apt/keyrings/grafana.gpg] https://packages.grafana.com/oss/deb stable main" | sudo tee /etc/apt/sources.list.d/grafana.list
sudo apt update
sudo apt install grafana

### Iniciar y habilitar grafana

sudo systemctl enable grafana-server
sudo systemctl start grafana-server

### Acceder desde el navegador

http://192.168.1.121:3000

### Ponerle el nombre de usuario y contraseña por defectos

admin/admin

### Conectar Grafana con Prometheus

Grafana → Data Sources → Prometheus
http://192.168.1.121:9090

# 3 Raspberry Cliente 

## Instalar Node Exporter

cd /tmp
wget https://github.com/prometheus/node_exporter/releases/download/v1.8.2/node_exporter-1.8.2.linux-armv7.tar.gz
tar xvf node_exporter-1.8.2.linux-armv7.tar.gz
sudo mv node_exporter-1.8.2.linux-armv7/node_exporter /usr/local/bin/

### Crea un usuario de sistema:

sudo useradd -rs /bin/false node_exporter 

### Crea el servicio systemd

sudo nano /etc/systemd/system/node_exporter.service

### Dentro de este nuevo archivo pegue lo siguiente

[Unit]
Description=Node Exporter
After=network.target

[Service]
User=node_exporter
ExecStart=/usr/local/bin/node_exporter
Restart=on-failure

[Install]
WantedBy=multi-user.target

### Una vez pegado, guarde y salga del archivo

### Despues reinicie el servicio

sudo systemctl daemon-reload
sudo systemctl enable node_exporter
sudo systemctl start node_exporter


## Comprobacion

### En el navegador introduzca la siguente URL

http://<IP_de_la_Pi>:9100/metrics

### En este caso hay que introducirlo con las IPs de los clientes, que son

pi@rp2G3

http://192.168.1.193:9100/metrics

pi@rp3G3

http://192.168.1.160:9100/metrics


### Lo que devuelve es una pagina en negro con un monton de metricas 

# Errores que nos hemos encontrado durante la instalación

1) En la guia original estaba este código el cual no funcionaba: sudo apt install -y apt-transport-https software-properties-common
    Y lo sustituimos por este otro: sudo apt install -y apt-transport-https software-properties-common
2) En el archivo de configuración prometheus.yml hay que añadir el código al final del archivo en lugar de sustituirlo, además que las ip debes ponerlas de esta forma: ['192.168.1.193:9100', '192.168.1.160:9100']
Y en el documento aparece de esta otra forma:   - `'localhost:9100'`
                                                - `'192.168.10.11:9100'`
                                                - `'192.168.10.12:9100'`
3) Intentar conectar desde internet con Prometheus poniendo ip diferentes a las del servidor

