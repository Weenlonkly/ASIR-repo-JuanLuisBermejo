# 10 [OSINT] Reconocimiento de dominios por terminal y scripting - Juan Luis Bermejo


## 1 AMASS – Descubrimiento de subdominios (OSINT real)

### Instalamos en ubuntu amass

sudo apt install amass

### En mi caso no ha funcionado asi que lo he descargado con snap 

sudo snap install amass

#### Se puede comprobar con:

amass version

Saldra un dibujo y una lista de subcomandos de ayuda

#### Un uso basioco puede ser

amass enum -passive -d ejemplo.com

#### Devuelve una ristra de dominios muy larga, estos son unos pocos que me han salido

sql.ejemplo.com
imap.ejemplo.com
zimbra8.ejemplo.com
ejemplo.ejemplo.com
tuempresa.ejemplo.com

#### Tambien puedes almacenarlo en un archivo de texto 

amass enum -passive -d ejemplo.com -o subdominios.txt

#### En caso de que se quiera enumerar mas dominios

amass enum -passive -df dominios.txt -o resultados.txt

#### En dominios hay que poner en texto los dominios que se quieran enumerar



## 2 Subfinder – Enumeración rápida y minimalista

### Instalar subfinder 

## Problema!
### No me ha dejado descargar subfinder de ninguna manera asi que no lo he podido hacer (no va ni con snap)


## 3 Geolocalización – Poniendo los pies en la Tierra

### 3.1 Geolocalización de IP con whois

#### Primero descargamos whois y preguntamos quien es 8.8.8.8 que deveria ser google

sudo apt install whois

whois 8.8.8.8

#### El problema es que aun con varios intentos me sale:

connect: Network is unreachable

### 3.2 Uso de geoiplookup

#### instalamos geoiplookup

sudo apt install geoip-bin

#### Luego lo probamos de nuevo con 8.8.8.8

geoiplookup 8.8.8.8

#### Este si que funciona, y devuelve:

GeoIP Country Edition: US, United States

### 3.3 Geolocalización con APIs desde terminal

#### Pegamos el siguiente comando

curl ipinfo.io/8.8.8.8

#### Devuelve el siguiente .json

{
  "ip": "8.8.8.8",
  "hostname": "dns.google",
  "city": "Mountain View",
  "region": "California",
  "country": "US",
  "loc": "38.0088,-122.1175",
  "org": "AS15169 Google LLC",
  "postal": "94043",
  "timezone": "America/Los_Angeles",
  "readme": "https://ipinfo.io/missingauth",
  "anycast": true
}


## 4 Uniendo piezas: OSINT como proceso

Ejemplo de flujo real:

    1 Amass descubre subdominios
    2 Subfinder confirma y amplía
    3 Se resuelven IPs
    4 Se geolocalizan
    5 Se detecta:
        - Infraestructura cloud
        - Distribución geográfica
        - Entornos de desarrollo expuestos

## 5 Ejemplo

### Un ejemplo practico puede ser 

amass enum -passive -d ejemplo.com -o amass.txt
subfinder -d ejemplo.com -o subfinder.txt
sort amass.txt subfinder.txt | uniq > subdominios_finales.txt

#### El problema de este es que el comando subfinder no lo va a ejecutar por que no puedo descargarlo
