# Pokédex con Python y PokeAPI

### Link del repositorio ###

https://github.com/00HB/proyecto-m4-python

## Índice

1. [Descripción del proyecto](#descripción-del-proyecto)
2. [¿Cómo hice el programa?](#cómo-hice-el-programa)
3. [Bibliotecas utilizadas](#bibliotecas-utilizadas)
4. [Función para consultar la PokeAPI](#función-para-consultar-la-pokeapi)
5. [Función para extraer los datos del Pokémon](#función-para-extraer-los-datos-del-pokémon)
6. [Función para mostrar la información](#función-para-mostrar-la-información)
7. [Función para guardar el archivo JSON](#función-para-guardar-el-archivo-json)
8. [Ejecución del proyecto](#ejecución-del-proyecto)
9. [Requisitos cumplidos](#requisitos-cumplidos)
10. [Resultado observado](#resultado-observado)
11. [Estructura del repositorio](#estructura-del-repositorio)
12. [Reflexión](#reflexión)

## Descripción del proyecto

Este proyecto consiste en construir una Pokédex usando Python y la API pública llamada PokeAPI.

El programa solicita al usuario el nombre de un Pokémon. Después realiza una petición HTTP a la página `https://pokeapi.co/` para buscar la información del Pokémon escrito.

Si el Pokémon no existe, el programa muestra un mensaje de error. Si el Pokémon sí existe, el programa muestra información importante como su peso, tamaño, tipos, habilidades, movimientos, estadísticas y el link de su imagen frontal.

Además, el programa guarda toda la información obtenida en un archivo `.json` dentro de una carpeta llamada `pokedex`.

El objetivo del proyecto es practicar el consumo de APIs, el manejo de status codes, el uso de archivos JSON y la organización de información obtenida desde internet.

## ¿Cómo hice el programa?

Primero importé las bibliotecas necesarias:

```python
import json
import os
from typing import Any, Dict, Optional

import requests
```

La biblioteca `requests` se utilizó para hacer peticiones HTTP a la PokeAPI.

La biblioteca `json` se utilizó para guardar la información del Pokémon en un archivo con formato `.json`.

La biblioteca `os` se utilizó para crear la carpeta `pokedex` en caso de que todavía no existiera.

El programa se divide en varias funciones para que el código sea más ordenado y fácil de entender.

## Bibliotecas utilizadas

Para ejecutar este proyecto se necesita tener instalado Python y la biblioteca `requests`.

La instalación de `requests` se puede hacer con el siguiente comando:

```bash
pip install requests
```

También se usan bibliotecas incluidas con Python, por lo que no es necesario instalarlas aparte:

- `json`
- `os`
- `typing`

## Función para consultar la PokeAPI

```python
obtener_pokemon()
```

Esta función recibe el nombre del Pokémon que escribe el usuario.

Primero limpia el texto usando `.strip()` y `.lower()` para evitar errores por espacios o mayúsculas. Después construye la URL de consulta usando la dirección base de PokeAPI.

El programa realiza la petición con:

```python
requests.get(url, timeout=10)
```

También se utiliza `timeout=10` para evitar que el programa se quede esperando indefinidamente si hay un problema de conexión.

Esta función valida los status codes de la respuesta:

- Si el status code es `200`, significa que el Pokémon fue encontrado correctamente.
- Si el status code es `404`, significa que el Pokémon no existe.
- Si llega otro status code, el programa muestra un mensaje indicando el código recibido.

También se usa `try` y `except` para manejar errores de conexión con la API.

## Función para extraer los datos del Pokémon

```python
extraer_datos_pokemon()
```

Esta función recibe toda la información que devuelve la PokeAPI y selecciona solamente los datos necesarios para la Pokédex.

Los datos que se extraen son:

- ID del Pokémon.
- Nombre.
- Peso.
- Altura o tamaño.
- Tipos.
- Habilidades.
- Movimientos.
- Estadísticas base.
- Link de la imagen frontal.

La PokeAPI devuelve mucha información en listas y diccionarios anidados. Por eso, esta función transforma esos datos en un diccionario más limpio y fácil de leer.

Por ejemplo, los tipos, habilidades y movimientos se guardan como listas de texto.

## Función para mostrar la información

```python
mostrar_pokemon()
```

Esta función recibe el diccionario con los datos ya organizados y muestra la información en consola.

El programa muestra los datos principales del Pokémon, sus estadísticas y sus movimientos.

También muestra el link de la imagen frontal del Pokémon. En la consola no se puede ver la imagen directamente como en una página web, por eso se muestra el enlace del recurso.

Ejemplo del link de imagen frontal:

```text
https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png
```

## Función para guardar el archivo JSON

```python
guardar_json()
```

Esta función crea la carpeta `pokedex` si todavía no existe.

Para crear la carpeta se usa:

```python
os.makedirs(POKEDEX_FOLDER, exist_ok=True)
```

Después se crea un archivo `.json` con el nombre del Pokémon consultado.

Por ejemplo, si el usuario busca `pikachu`, el programa genera el archivo:

```text
pokedex/pikachu.json
```

La información se guarda usando:

```python
json.dump(pokemon, archivo, indent=4, ensure_ascii=False)
```

Se utiliza `indent=4` para que el archivo sea más fácil de leer y `ensure_ascii=False` para permitir caracteres especiales en caso de ser necesario.

## Ejecución del proyecto

Para ejecutar el programa, primero se debe instalar la biblioteca `requests`:

```bash
pip install requests
```

Después se ejecuta el archivo principal:

```bash
python pokedex_app.py
```

El programa pedirá el nombre de un Pokémon:

```text
Bienvenido a la Pokédex
Escribe el nombre de un Pokémon: pikachu
```

Si el Pokémon existe, se mostrará su información y se guardará el archivo JSON.

Si el Pokémon no existe, se mostrará un mensaje de error indicando que no fue encontrado.

## Requisitos cumplidos

- Se consume exitosamente la PokeAPI usando `requests`.
- Se obtiene información real desde `https://pokeapi.co/`.
- Se validan status codes HTTP como `200` y `404`.
- Se manejan errores de conexión usando `try` y `except`.
- Se muestra información del Pokémon en consola.
- Se muestra el link de la imagen frontal del Pokémon.
- Se muestran peso, altura, movimientos, habilidades, tipos y estadísticas.
- Se crea una carpeta llamada `pokedex`.
- Se guarda la información del Pokémon en un archivo `.json`.
- El código está dividido en funciones.
- El código contiene comentarios útiles para entender su funcionamiento.
- El README contiene título, índice, explicación del proyecto, instalación, ejecución, ejemplo y reflexión.

## Resultado observado

Al ejecutar el programa y buscar un Pokémon existente, se muestra la información obtenida desde la PokeAPI.

Ejemplo usando `pikachu`:

```text
========== RESULTADO DE BÚSQUEDA ==========
ID: 25
Nombre: Pikachu
Peso: 60
Altura: 4
Tipos: electric
Habilidades: static, lightning-rod

Estadísticas:
  - hp: 35
  - attack: 55
  - defense: 40
  - special-attack: 50
  - special-defense: 50
  - speed: 90

Movimientos:
mega-punch, pay-day, thunder-punch, slam, double-kick, mega-kick...

Imagen frontal: https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png
==========================================

Archivo JSON guardado correctamente en: pokedex/pikachu.json
```

Imagen frontal de muestra:

![Pikachu](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png)

También se genera un archivo `.json` dentro de la carpeta `pokedex`, demostrando que el programa puede crear archivos y guardar información correctamente.

## Estructura del repositorio

```text
pokedex-python/
│
├── README.md
├── pokedex_app.py
└── pokedex/
    └── pikachu.json
```

## Reflexión

Este proyecto me ayudó a comprender mejor cómo consumir una API web pública usando Python. Aprendí a realizar peticiones HTTP con la biblioteca `requests` y a validar los status codes que devuelve un servidor.

También reforcé el manejo de datos en formato JSON, ya que la PokeAPI devuelve información en diccionarios y listas. Para poder mostrar los datos correctamente, tuve que aprender a recorrer estructuras anidadas y seleccionar solo la información necesaria.

Además, practiqué la creación de carpetas y archivos desde Python. Esto fue importante porque el proyecto no solo consulta información, también la guarda en una carpeta llamada `pokedex` para demostrar que los datos pueden conservarse después de ejecutar el programa.

Durante este módulo fortalecí mi lógica de programación, el uso de funciones, el manejo de errores, el consumo de APIs y la organización de proyectos para subirlos a GitHub.
