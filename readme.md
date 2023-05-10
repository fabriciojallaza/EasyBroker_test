# Documentación del proyecto
## Descripción
Este proyecto consiste en consumir la API de EasyBroker para leer todas las propiedades de una cuenta de staging e imprimir sus títulos. Se ha implementado una clase EasyBrokerAPI que se encarga de hacer la solicitud HTTP GET a la API y retornar la información de las propiedades.

## Dependencias
- Python 3.x
- requests

## Uso
1. Para utilizar la clase EasyBrokerAPI es necesario instanciarla con un token de acceso válido:
~~~python
api = EasyBrokerAPI("access_token")
~~~

2. Una vez instanciada la clase, se puede llamar al método get_properties() para obtener la información de todas las propiedades de la cuenta de staging:
perl
~~~python
properties, keys = api.get_properties()
~~~

3. El método `get_properties()` retorna dos valores:
   - `properties`: una lista de diccionarios con la información de las propiedades.
   - `keys`: una lista con los nombres de las claves de los diccionarios de properties.
## Ejemplo

~~~python
from easy_broker_api import EasyBrokerAPI

api = EasyBrokerAPI("access_token")
properties, keys = api.get_properties()

for property in properties:
    print(property["title"])
~~~

## Pruebas unitarias
Se han incluido varias pruebas unitarias para verificar el correcto funcionamiento de la clase EasyBrokerAPI. Estas pruebas se encuentran en el archivo test_easy_broker_api.py. Para ejecutar las pruebas, se debe correr el comando:

~~~
python -m unittest test_easy_broker_api.py
~~~

Autor: Fabricio Jallaza