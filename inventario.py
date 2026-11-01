"""Inventario sencillo de una tienda de ejemplo para probar Sentinels."""

from dataclasses import dataclass


@dataclass
class Producto:
    """Un producto con su nombre, precio y existencias."""

    nombre: str
    precio: float
    existencias: int


def valor_total(productos: list[Producto]) -> float:
    """Suma el valor de todo el inventario."""
    return sum(p.precio * p.existencias for p in productos)


def agotados(productos):
    return [p.nombre for p in productos if p.existencias == 0]