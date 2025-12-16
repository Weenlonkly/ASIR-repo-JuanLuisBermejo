# Linux IA En la terminal - Juan Luis Bermejo


## Descargarlo en Linux

### El primer paso es descargarlo desde la terminal con el siguiente comando 

curl -sSL https://raw.githubusercontent.com/aandrew-me/tgpt/main/install | bash -s /usr/local/bin


#### La primera comprobacion es la que pide el funcionamiento de OSINT


    Te devuelve una explicacion breve y 12 tipos de fuentes 


#### La segunda comprobacion es la que pregunta sobre el comando grep

    Devuelve 10 casos de uso


#### La ultima comprobacion es la se los scripts 

    Devuelve el siguiente script 

```bash
#!/bin/bash

# Comprueba si el host está en blanco o no se proporciona
if [ -z "$1" ]; then
    echo "Usage: $0 <hostname_or_ip>"
    exit 1
fi

# Intenta hacer ping y comprueba el resultado
ping -c 4 "$1" > /dev/null 2>&1

# Si el comando terminó con éxito (código de salida 0), el host responde
if [ $? -eq 0 ]; then
    echo "$1 es alcanzable"
else
    echo "$1 no es alcanzable"
fi
```


### Tras estas comprobaciones se ve claramente que esta descargado
