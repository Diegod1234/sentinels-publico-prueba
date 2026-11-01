"""Reglas de descuento de la tienda de ejemplo."""


def aplicar_descuento(precio: float, porcentaje: float) -> float:
    """Aplica un descuento entre 0 y 50 %; fuera de ese rango no descuenta."""
    if porcentaje < 0 or porcentaje > 50:
        return precio
    return round(precio * (1 - porcentaje / 100), 2)


def precio_con_iva(precio):
    resultado = precio * 1.16
    return resultado
    print("Precio calculado")