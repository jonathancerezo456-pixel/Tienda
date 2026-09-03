# Sistema básico de una tienda

## Descripción

Este proyecto es un sistema básico de una tienda desarrollado en Python.
Fue realizado para aplicar los conceptos de Programación Orientada a Objetos
estudiados hasta la Semana 3.

El sistema permite representar productos, productos electrónicos, marcas y
diferentes tipos de clientes con sus respectivos descuentos.

## Objetivo

Aplicar los principales conceptos de Programación Orientada a Objetos mediante
un sistema de tienda sencillo, utilizando encapsulación, herencia, composición,
clases abstractas, sobrescritura de métodos y polimorfismo.

## Principales funcionalidades

- Crear productos con nombre, precio y cantidad.
- Crear productos electrónicos con garantía y marca.
- Utilizar atributos privados mediante encapsulación.
- Aplicar herencia entre Producto y ProductoElectronico.
- Relacionar ProductoElectronico con Marca.
- Crear diferentes tipos de clientes.
- Aplicar un descuento del 15% al ClienteMayorista.
- Aplicar un descuento del 5% al ClienteMinorista.
- Utilizar polimorfismo para calcular los descuentos.

## Estructura del proyecto

- `producto.py`: contiene la clase Producto.
- `producto_electronico.py`: contiene la clase ProductoElectronico.
- `marca.py`: contiene la clase Marca.
- `cliente.py`: contiene la clase abstracta Cliente.
- `cliente_mayorista.py`: contiene la clase ClienteMayorista.
- `cliente_minorista.py`: contiene la clase ClienteMinorista.
- `main.py`: contiene las pruebas y la ejecución principal del programa.

## Cómo ejecutar el proyecto

1. Tener Python instalado.
2. Descargar o clonar el repositorio.
3. Abrir la carpeta `tienda`.
4. Ejecutar:

python main.py

## Ejemplo de funcionamiento

Para un total de $100:

- Cliente Mayorista: aplica 15% de descuento → total final $85.
- Cliente Minorista: aplica 5% de descuento → total final $95.

## Lenguaje utilizado

Python
