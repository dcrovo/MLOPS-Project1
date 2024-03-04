![alt text](https://github.com/c4ttivo/MLOpsTaller1/blob/main/mlopstaller1/imgs/logo.png?raw=true)

# MLOps - Proyecto
## Autores
*    Daniel Crovo (dcrovo@javeriana.edu.co)
*    Hugo Poveda (h.poveda@javeriana.edu.co)
*    Carlos Trujillo (ca.trujillo@javeriana.edu.co)

## Profesor
*    Cristian Diaz (diaz.cristian@javeriana.edu.co)

## Instrucciones
Clone el repositorio de git usando el siguiente comando en la consola de su sistema operativo:


```
# git clone git@github.com:dcrovo/MLOPS-Project1.git
```

Una vez ejecutado el comando anterior aparece el folder MLOPS-Project1 al cual debe dirigirse con el siguiente comando


```
# cd MLOPS-Project1
```

Ahora es necesario construir el contenedor y levantarlo con el siguiente comando


```
# docker-compose up 
```
En este paso se construye una imagen a partir de la última imagen disponible de tfx en docker en este caso  1.14.0, adicionalmente se instala en el contenedor dvc para poder acceder desde la terminal de jupyterlab.
para acceder al contenedor de desarrollo preste atención a la salida de la terminal en donde muestra un link similar al siguiente: 

```http://127.0.0.1:8888/lab?token=123e4b......```

copielo y péguelo en el navegador para poder acceder al notebook. 

