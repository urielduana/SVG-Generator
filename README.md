# SVG-Generator

Este script de Python genera archivos SVG y PDF a partir de una plantilla base SVG y un archivo de entrada que contiene datos a reemplazar en la plantilla. Los datos de entrada deben estar en formato de tabla y se pueden dividir en varias páginas en función del número de columnas.

## Uso

1. Crea un archivo de entrada con los datos que se utilizarán para generar los archivos SVG y PDF. Los datos deben estar en formato de tabla y separados por comas o tabulaciones. Un ejemplo de archivo de entrada puede verse en el archivo `datos.txt`.

2. Crea una plantilla base SVG para el archivo de salida. Para ello, puedes utilizar cualquier software de edición de gráficos vectoriales compatible con SVG, como Inkscape.

- En la plantilla SVG, incluye las variables que se reemplazarán con los datos de entrada en el formato `CAMBIAR{j}AQUI`, donde `{j}` es el número de la columna de datos correspondiente.

- Para crear una plantilla base, guarda el archivo SVG con las variables en el directorio `bases/` en el repositorio de SVG-Generator.

- La plantilla base debe tener una estructura consistente y ser coherente con los datos de entrada. Por ejemplo, si se desea generar un archivo PDF para una factura, la plantilla base debe tener una estructura que coincida con los datos de entrada para una factura.

3. Abre el archivo `generador.py` en un editor de texto y modifica los siguientes parámetros:

- `input_file`: ruta y nombre del archivo de entrada con los datos en formato de tabla.

- `num_columns`: número de columnas de datos en la tabla.

- `output_dir`: ruta del directorio donde se generarán los archivos PDF.

- `base_dir`: ruta del directorio que contiene las plantillas base SVG.

- `max_chars`: longitud máxima de los datos en cada celda de la tabla antes de dividirse en varias líneas.

4. Ejecuta el script `generador.py` en la terminal con el siguiente comando:

python generador.py


5. Los archivos PDF se generarán en el directorio especificado en `output_dir`.

## Contribución

Las contribuciones son bienvenidas en forma de solicitudes de extracción. Para cambios importantes, primero abra un problema para discutir qué le gustaría cambiar.

Asegúrese de actualizar las pruebas según corresponda.

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.
