# GameStonks

## Integrantes

- Juan Carlos Couselo Fernández
    - GitHub: [juancouselo](https://github.com/juancouselo)
    - Correo UDC: <juan.couselo@udc.es>
- Iago Domínguez Cameán
    - GitHub: [iagoDominguezCamean](https://github.com/iagoDominguezCamean)
    - Correo UDC: <iago.dominguez.camean@udc.es>
- Íker García Calviño
    - GitHub: [ikergcalvino](https://github.com/ikergcalvino)
    - Correo UDC: <iker.gcalvino@udc.es>

## Cómo ejecutar

Para ejecutar la web, debemos de tener instalado el servidor de despliegue de [Docker](https://www.docker.com/).

Una vez instalado, podemos ejecutar Docker desde Visual Studio Code:

```
> Remote-Containers: Rebuild and Reopen in Container
```

Desde dentro del contenedor, podemos ejecutar el siguiente script por primera vez para arrancar el servidor:

```
sh start.sh
```

## Problemas conocidos

Hemos desactivado la funcionalidad de compartir las ofertas, debido a que el uso de las APIs de RRSS están enfocadas a empresas privadas, y no a usuarios finales.
El uso de ellas nos obliga a crearnos una cuenta de empresa después de haber usado los "tokens" de prueba (los cuáles tienen un uso limitado).
En el caso del API de Twitter, no permite usar el método "POST" porque no pertenece a los endpoints de Twitter API v2.
