# ReconLite (mini escáner OSINT HTTP) - Juan Luis Bermejo

## Asegurarse de instalar pip

#### En mi caso solo tenia que activar venv ya que en la tarea de locos por los retos de docker en lo parte de las conexiones entre python y mongo.db

source venv/bin/activate

## Descargar lo que hay en requirements.txt 

pip install -r requirements.txt

(requests>=2.31.0)


python reconlite.py https://example.com

### El comando devuelve 

✅ Objetivo: https://example.com
✅ HEAD status: 200 (210.84 ms)
✅ Hallazgos guardados en: report.json
✅ Endpoints interesantes (con status): 1


### Tambien crea un .json

### Al cambiar de usuario al ejecutar reconlite.py

python reconlite.py example.com --ua "Mozilla/5.0 (ReconLite class)"

#### El .json cambia

{
  "target": "https://example.com",
  "timestamp_utc": "2025-12-17T10:34:48Z",
  "config": {
    "timeout_s": 8,
    "verify_tls": true,
    "max_paths": 40,
    "user_agent": "Mozilla/5.0 (ReconLite class)"
  },


### Añadir tu propio wordlist de rutas

#### Creamos un archivo Archivo "paths.txt"

sudo nano paths.txt 

#### se introduce:

admin
admin/
robots.txt
api/v1

#### Luego podemos ejecutar:

python reconlite.py https://midominio.com --paths-file paths.txt --max-paths 200

#### Devuelve que la operacion se ejecuta correctamente

#### El .json vuelve a cambiar

  {
  "target": "https://midominio.com",
  "timestamp_utc": "2025-12-17T10:37:48Z",
  "config": {
    "timeout_s": 8,
    "verify_tls": true,
    "max_paths": 200,
    "user_agent": "ReconLite/1.0 (+educational)"
  }

