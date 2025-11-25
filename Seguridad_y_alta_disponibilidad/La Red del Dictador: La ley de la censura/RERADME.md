# La Red del Dictador: La ley de la censura Sergio Chamba y Juan Luis Bermejo
1. Instalar Docker
## Lo primero será actualizarlo
sudo apt update && sudo apt upgrade -y
## Descargamos docker
curl -sSL https://get.docker.com | sh
## Creamos el usuario
sudo usermod -aG docker $USER
## Le haremos reboot para aplicar permisos
sudo reboot
## Comprobaremos que funciona correctamente
docker run hello-world
2. Crear el volumen y red para Pi-hole
docker volume create pihole_etc
docker volume create pihole_dnsmasq
3. Ejecutar Pi-hole con Docker (modo manual)
## Nos conectamos dentro del volumen
docker ecex -it "nombre_archivo" bash
## Cuando estemos dentro ejecutaremos todo el siguiente código juntos
docker run -d \
	--name pihole \
	--restart=unless-stopped \
	-e TZ="Europe/Madrid" \
	-e WEBPASSWORD="tu_contraseña_segura" \
	-e DNSMASQ_LISTENING=all \
	-v pihole_etc:/etc/pihole \
	-v pihole_dnsmasq:/etc/dnsmasq.d \
	-p 53:53/tcp -p 53:53/udp \
	-p 80:80/tcp \
	--hostname pi-hole \
	--dns=127.0.0.1 --dns=1.1.1.1 \
	pihole/pihole:latest
## Continuaremos abriendo la app en el navegador con nuestra ip en este caso: 192.168.1.132
http://192.168.1.132/admin
4. Configurar IP estática
## Nos meteremos dentro del archivo para modificar la IP
sudo nano /etc/dhcpcd.conf
## Le añadiremos esta linea de código para cambiarle la IP
interface eth0 static ip_address=192.168.0.200/24 static routers=192.168.0.1 static domain_name_servers=1.1.1.1
