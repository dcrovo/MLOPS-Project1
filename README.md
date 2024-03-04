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

copielo y péguelo en el navegador para poder acceder al notebook. Verá lo siguiente en el navegador. ahora seleccione el archivo ProyectoMLOPS1.ipynb

![image](https://github.com/dcrovo/MLOPS-Project1/assets/26165926/9bc52bd9-8ffe-426d-9f2b-9ee352fa8a0e)

Una vez abierto puede ejecutar todo el notebook para verificar su correcto funcionamiento y desarrollo del proyecto. 
![image](https://github.com/dcrovo/MLOPS-Project1/assets/26165926/a66d05a4-1eae-49c8-8f6d-03dc9a891dfd)
Puede elegir dos formas de ejecutar el proyecto:
- Volver a correr todas la celdas, en este caso se generarán más artefactos adicionales en la carpeta pipeline.
- Eliminar la carpeta pipeline y correr todo el notebook
