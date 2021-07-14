# Lectura de inversor Huawei en red local sobre distribución tipo Debian/Ubuntu

Este script sirve para leer, localmente, los datos ofrecidos por inversores Huawei de placas fotovoltaicas. Probablemente, si tienes una estructura montada de esta marca, uses Fusion Solar tanto en aplicación móvil como en navegador para acceder a tus datos de consumo, autoconsumo y exportación. Con este script, puedes obtener los datos en tiempo real.

# Requisitos

## 1. Instalación de Python y dependencias

Con el siguiente comando, comprobamos la versión que tenemos instalada.

```
python3 --version
```

1.a Si no tenemos python instalado, haremos lo siguiente para hacerlo junto a las dependencias necesarias en el siguiente punto:

```
sudo apt install python3 pip
```

## 2. Instalación de wrapper huawei-solar

A través del siguiente comando, instalamos el *wrapper* huawei-solar, que servirá de conector entre el inversor Huawei y nuestro equipo. Esto hará que instale **pytz** y **pymodbus** que se encargarán de establecer la zona horaria y la comunicación asíncrona con el inversor:

```
pip install huawei-solar
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
h = huawei_solar.HuaweiSolar(host="IP_LOCAL_INVERSOR")
```

## 4. Ejecución del script

Una vez modificado el script, ejecutamos el siguiente script y nos ofrece datos básicos.

```
python3 inversorlocal.py
```
Para observar los datos en ciclos de 2 segundos, ejecuta el siguiente comando. Cambia la cifra a tu gusto:

```
watch -n2 python inversorlocal.py
```

## Ejemplo con valores en kWh:

Energía entrada:     1307                          
 > Energía que capta tu instalación fotovoltaica.

Energía generada:    1280                         
 > Energía que llega hasta tu sistema eléctrico. Según condiciones (cableado, distancia), es normal que se pierda un pequeño porcentaje en el camino.
  
Energía exportada:   1128                           
> Energía que no usamos y estamos vertiendo a la red.

Energía consumida:   152                            
> Energía que estamos en este momento.

Fecha y hora:        DD/MM/AAAA y son las HH:MM:SS  
> Fecha y hora de la operación.

# Notas

- Este sencillo script puede ofrecerte multitud de posibilidades para crearte tu propia app ejecutado en local.

- Dentro del script puedes observar otros datos de interés que pueden publicarse en el resultado, tales como la eficiencia, el modelo del inversor o el número de serie.
