import json
from pathlib import Path

ARCHIVO = Path(__file__).resolve().parent / "inventario.json"


def guardar_inventario(inventario):
    with ARCHIVO.open("w", encoding="utf-8") as archivo:
        json.dump(inventario, archivo, ensure_ascii=False, indent=4)

def cargar_inventario():
    if not ARCHIVO.exists():
        return []

    try:
        with ARCHIVO.open("r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except json.JSONDecodeError:
        raise ValueError(
            "El archivo inventario.json está vacío o dañado. "
            "Revisalo antes de continuar."
        )