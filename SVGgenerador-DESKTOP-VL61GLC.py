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
        
        name = re.sub(r'\W+', '-', line[0])
            
        with open(base_dir + f"Base_{len(line)}.svg", "r", encoding='utf8') as base_f, \
             open(output_dir + name + ".svg", 'w', encoding='utf8') as write:
            
            for base_line in base_f:
                for j in range(len(line)):
                    base_line = re.sub(f"CAMBIAR{j}AQUI", line[j], base_line)
                write.write(base_line)            
            
        drawing = svg2rlg(output_dir + name + ".svg")
        renderPDF.drawToFile(drawing, output_dir + name + ".pdf")
        os.remove(output_dir + name + ".svg")
        generated_files.append(name + ".pdf")

    # Display generated files, grouping them by 30 if there are more than 30
    num_files = len(generated_files)
    if num_files <= 30:
        messagebox.showinfo("PDF Generation", f"{num_files} PDFs were generated:\n" + "\n".join(generated_files))
    else:
        num_groups = num_files // 30 + (1 if num_files % 30 != 0 else 0)
        total = 0
        for i in range(num_groups):
            group_start = i * 30
            group_end = (i + 1) * 30
            group_files = generated_files[group_start:group_end]
            total = total + len(group_files)
            messagebox.showinfo("PDF Generation", f"{total} PDFs were generated (group {i+1}/{num_groups}):\n" + "\n".join(group_files))




# Example usage
input_file = "datos.txt"
num_columns = 7
output_dir = "C:/Users/Vadose/OneDrive/Documentos/TAGS/031023/TerceraParte77pz/"
base_dir = "bases/"
max_chars = 60

generate_svg_pdf_per_file(input_file, num_columns, output_dir, base_dir, max_chars)