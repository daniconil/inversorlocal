# Lectura de inversor Huawei en red local sobre distribución tipo Debian/Ubuntu

Este script sirve para leer, localmente, los datos ofrecidos por inversores Huawei de placas fotovoltaicas. Probablemente, si tienes una estructura montada de esta marca, uses Fusion Solar tanto en aplicación móvil como en navegador para acceder a tus datos de consumo, autoconsumo y exportación. Con este script, puedes obtener los datos en tiempo real.

## Versión terminal y versión web

Este repositorio, **inversorlocal**, permite consultar los datos del inversor desde la **terminal**. Si prefieres acceder a ellos desde el **navegador**, consulta [inversorlocal-web](https://github.com/daniconil/inversorlocal-web#readme), donde encontrarás las instrucciones de la versión web.

# Requisitos

## 1. Instalación de Python y dependencias

La librería **huawei-solar** requiere **Python 3.12 o superior**. Comprobamos la versión:

```
python3 --version
```

Si la versión es inferior a 3.12, actualízela antes de continuar. Se recomienda usar un entorno virtual:

```
python3 -m venv .venv && source .venv/bin/activate
```

1.a Si no tenemos python instalado:

```
sudo apt update && sudo apt install python3 python3-pip python3-venv
```

## 2. Instalación de wrapper huawei-solar

Instalamos la librería **huawei-solar** (versión 3.x) y **pytz** dentro del entorno activado:

```
pip install "huawei-solar>=3.0" pytz
```
Más información de huawei-solar en https://pypi.org/project/huawei-solar/
Más información de pytz en https://pypi.org/project/pytz/
Más información de pymodbus en https://pypi.org/project/pymodbus/

## 3. Modificación de IP

Debemos modificar **IP_LOCAL_INVERSOR** por la IP local del inversor Huawei. Accede al script:
```
nano inversorlocal.py
```
Y modifica la variable indicada:

```
HOST = "IP_LOCAL_INVERSOR"
```

## 4. Ejecución del script

Una vez modificado el script, ejecutamos el siguiente script y nos ofrece datos básicos. La comunicación ahora se realiza de forma asíncrona mediante `create_tcp_client`, `SUN2000Device` y `await device.get(...)`; al finalizar, se cierra la conexión con el inversor.

```
python3 inversorlocal.py
```
Para observar los datos en ciclos de 2 segundos, ejecuta el siguiente comando. Cambia la cifra a tu gusto:

```
watch -n2 python3 inversorlocal.py
```

## Ejemplo con valores en W (potencia instantánea):

Potencia entrada:     1307 W                            
 > Potencia que capta tu instalación fotovoltaica del lado de la red.

Potencia generada:    1280 W                           
 > Potencia generada por el inversor. Según condiciones (cableado, distancia), es normal que se pierda un pequeño porcentaje en el camino.
  
Potencia exportada:   1128 W                             
> Potencia que no consumimos y estamos vertiendo a la red (flujo hacia la red pública).

Potencia neta consumida:   152 W                              
> Potencia neta que consumimos en este momento (generación menos importación neta).

Fecha y hora:        DD/MM/AAAA y son las HH:MM:SS    
> Fecha y hora de la operación.

# Notas

- Se actualizó la comunicación con el inversor para adaptarla a la API asíncrona actual de `huawei-solar`, en lugar de usar la antigua interfaz `HuaweiSolar` y llamadas síncronas `.get()`. Así se crea y cierra correctamente el cliente TCP, y se leen los registros con `await device.get(...)`.
- **Importante:** si el script finaliza con un mensaje de error, el proceso de salida devuelve código 0. Para que automatizaciones (cron, systemd, etc.) detecten fallos, ejecute el script dentro de `|| echo 'fallo'` o revise el código de retorno.
- Este sencillo script puede ofrecerte multitud de posibilidades para crearte tu propia app ejecutado en local.

- Dentro del script puedes observar otros datos de interés que pueden publicarse en el resultado, tales como la eficiencia, el modelo del inversor o el número de serie.
