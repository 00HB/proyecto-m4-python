"""
Pokédex con PokeAPI
-------------------
Proyecto individual para consumir una API web pública usando requests.

Funcionalidades principales:
- Solicita el nombre de un Pokémon al usuario.
- Consume la API pública https://pokeapi.co/.
- Valida códigos de estado HTTP.
- Muestra información relevante del Pokémon.
- Muestra el enlace de la imagen frontal oficial.
- Guarda los datos consultados en un archivo JSON dentro de la carpeta pokedex.
"""

import json
import os
from typing import Any, Dict, Optional

import requests


# URL base del recurso de Pokémon en PokeAPI.
POKEAPI_URL = "https://pokeapi.co/api/v2/pokemon/"

# Carpeta donde se guardarán los archivos JSON generados.
POKEDEX_FOLDER = "pokedex"



def obtener_pokemon(nombre_pokemon: str) -> Optional[Dict[str, Any]]:
    """
    Consulta la información de un Pokémon en PokeAPI.

    Args:
        nombre_pokemon: Nombre del Pokémon escrito por el usuario.

    Returns:
        Un diccionario con la respuesta JSON de la API si el Pokémon existe.
        None si ocurre un error, si no existe o si la API no responde correctamente.
    """
    # La API espera nombres en minúsculas y sin espacios al inicio o al final.
    nombre_limpio = nombre_pokemon.strip().lower()
    url = f"{POKEAPI_URL}{nombre_limpio}"

    try:
        # timeout evita que el programa se quede esperando indefinidamente.
        respuesta = requests.get(url, timeout=10)
    except requests.exceptions.RequestException as error:
        print("Error: no fue posible conectarse con PokeAPI.")
        print(f"Detalle técnico: {error}")
        return None

    # Validación explícita de status codes HTTP.
    if respuesta.status_code == 200:
        return respuesta.json()

    if respuesta.status_code == 404:
        print(f"Error: el Pokémon '{nombre_pokemon}' no existe en PokeAPI.")
        return None

    print(f"Error: PokeAPI respondió con status code {respuesta.status_code}.")
    return None



def extraer_datos_pokemon(datos_api: Dict[str, Any]) -> Dict[str, Any]:
    """
    Extrae y organiza únicamente la información solicitada para la Pokédex.

    Args:
        datos_api: Diccionario completo recibido desde PokeAPI.

    Returns:
        Diccionario limpio con datos importantes del Pokémon.
    """
    nombre = datos_api["name"]
    imagen_frontal = datos_api["sprites"]["front_default"]

    # Se convierten listas complejas de la API en listas simples de texto.
    tipos = [tipo["type"]["name"] for tipo in datos_api["types"]]
    habilidades = [habilidad["ability"]["name"] for habilidad in datos_api["abilities"]]
    movimientos = [movimiento["move"]["name"] for movimiento in datos_api["moves"]]

    estadisticas = {
        estadistica["stat"]["name"]: estadistica["base_stat"]
        for estadistica in datos_api["stats"]
    }

    pokemon = {
        "id": datos_api["id"],
        "nombre": nombre,
        "peso": datos_api["weight"],
        "altura": datos_api["height"],
        "tipos": tipos,
        "habilidades": habilidades,
        "movimientos": movimientos,
        "estadisticas": estadisticas,
        "imagen_frontal": imagen_frontal,
    }

    return pokemon



def mostrar_pokemon(pokemon: Dict[str, Any]) -> None:
    """
    Muestra en consola la información principal del Pokémon.

    Args:
        pokemon: Diccionario limpio con datos del Pokémon.
    """
    print("\n========== RESULTADO DE BÚSQUEDA ==========")
    print(f"ID: {pokemon['id']}")
    print(f"Nombre: {pokemon['nombre'].title()}")
    print(f"Peso: {pokemon['peso']}")
    print(f"Altura: {pokemon['altura']}")
    print(f"Tipos: {', '.join(pokemon['tipos'])}")
    print(f"Habilidades: {', '.join(pokemon['habilidades'])}")
    print("\nEstadísticas:")

    for nombre_estadistica, valor in pokemon["estadisticas"].items():
        print(f"  - {nombre_estadistica}: {valor}")

    print("\nMovimientos:")
    print(", ".join(pokemon["movimientos"]))

    # En consola no se renderiza la imagen, por eso se muestra el link directo.
    print(f"\nImagen frontal: {pokemon['imagen_frontal']}")
    print("==========================================\n")



def guardar_json(pokemon: Dict[str, Any]) -> str:
    """
    Guarda los datos del Pokémon en un archivo JSON dentro de la carpeta pokedex.

    Args:
        pokemon: Diccionario limpio con datos del Pokémon.

    Returns:
        Ruta del archivo JSON creado.
    """
    # exist_ok=True evita errores si la carpeta ya existe.
    os.makedirs(POKEDEX_FOLDER, exist_ok=True)

    ruta_archivo = os.path.join(POKEDEX_FOLDER, f"{pokemon['nombre']}.json")

    with open(ruta_archivo, "w", encoding="utf-8") as archivo:
        json.dump(pokemon, archivo, indent=4, ensure_ascii=False)

    return ruta_archivo



def main() -> None:
    """
    Función principal del programa.
    Controla el flujo completo: pedir datos, consultar API, mostrar y guardar.
    """
    print("Bienvenido a la Pokédex")
    nombre_pokemon = input("Escribe el nombre de un Pokémon: ")

    datos_api = obtener_pokemon(nombre_pokemon)

    if datos_api is None:
        print("No se pudo generar información para la Pokédex.")
        return

    pokemon = extraer_datos_pokemon(datos_api)
    mostrar_pokemon(pokemon)
    ruta_json = guardar_json(pokemon)

    print(f"Archivo JSON guardado correctamente en: {ruta_json}")


if __name__ == "__main__":
    main()
