import os
import re
from os import remove
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
from tkinter import messagebox

def split_strings(data, max_chars):
    dividers = [" ", "-", ","]
    for i, line in enumerate(data):
        for j, string in enumerate(line):
            if len(string) > max_chars:
                idx = -1
                for divider in dividers:
                    temp_idx = string[:max_chars].rfind(divider)
                    if temp_idx > idx:
                        idx = temp_idx
                if idx == -1:
                    idx = max_chars - 1
                data[i][j:j + 1] = [string[:idx+1], string[idx+1:]]
    return data

def generate_svg_pdf_per_file(input_file, num_columns, output_dir, base_dir, max_chars):
    # Create output directory
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(input_file, "r", encoding='utf8') as f:
        real = [line.strip() for line in f if line.strip()]

    # First data extraction
    data = [real[i:i + num_columns] for i in range(0, len(real), num_columns)]

    # Split strings if they exceed max_chars characters
    data = split_strings(data, max_chars)

    # Generate PDF
    generated_files = []
    for i, line in enumerate(data):
        # Name generation
        # Name will be the first and fifth column
        name = re.sub(r'\W+', '-', line[0] + "-" + line[5])
        print(name)
        with open(base_dir + f"Base_{len(line)}.svg", "r", encoding='utf8') as base_f, \
             open(output_dir + name + ".svg", 'w', encoding='utf8') as write:
                 
            # Agregar línea de codificación de caracteres
            write.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n')
                 

            for base_line in base_f:
                for j in range(len(line)):
                    base_line = re.sub(f"CAMBIAR{j}AQUI", line[j], base_line)
                write.write(base_line)            
            
        drawing = svg2rlg(output_dir + name + ".svg")
        renderPDF.drawToFile(drawing, output_dir + name + ".pdf")
        os.remove(output_dir + name + ".svg")
        generated_files.append(name + ".pdf")
