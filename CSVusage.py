from CSVtransform import *
from SVGgenerador import *
# Example usage
input_file = 'datos.txt'
output_dir = 'D:/Users/Vadose/OneDrive/Documentos/TAGS/260923/PT2/'
base_dir = 'bases/'
max_chars = 60
datos_csv = 'datos.csv'

num_columns = generate_txt(datos_csv, input_file)
generate_svg_pdf_per_file(input_file, num_columns, output_dir, base_dir, max_chars)

