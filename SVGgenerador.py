import os
from os import remove
import re
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF

def dividir_strings(listaTotal, max_caracteres):
    dividers = [" ", "-", ","]

    for i, lista in enumerate(listaTotal):
        for j, string in enumerate(lista):
            if len(string) > max_caracteres:
                idx = -1
                for divider in dividers:
                    temp_idx = string[:max_caracteres].rfind(divider)
                    if temp_idx > idx:
                        idx = temp_idx
                if idx == -1:
                    idx = max_caracteres - 1
                listaTotal[i][j:j + 1] = [string[:idx+1], string[idx+1:]]
    
    return listaTotal

def generar_svg_pdf_por_archivo(input_file, numDeColumnas, directorio, directorioBases, max_caracteres):
    # Crear directorio de salida
    if not os.path.exists(directorio):
        os.makedirs(directorio)

    fi = open(input_file, "r", encoding='utf8')
    real = []

    for linea in fi:
        if linea != '\n':
            linea = re.sub("\\n", "", linea)
            linea = re.sub("\\t", "", linea)

            real.append(linea)

    # Primera extracción de datos
    listaTotal = []
    for i in range(0, len(real), numDeColumnas):
        listaTotal.append(real[i:i + numDeColumnas])

    # Dividir strings si superan los max_caracteres caracteres
    listaTotal = dividir_strings(listaTotal, max_caracteres)

    #Generar PDF
    for i, lista in enumerate(listaTotal):
        read = open(directorioBases + "Base_" +str(len(lista))+".svg", "r",  encoding='utf8')
        write= open(directorio + listaTotal[i][0].split(":")[1] +".svg", 'w', encoding='utf8')
        for linea in read:
            for j in range(len(lista)):
                linea = re.sub("CAMBIAR"+str(j)+"AQUI",lista[j],linea)
            write.write(linea)
        write.close()

        drawing = svg2rlg(directorio + listaTotal[i][0].split(":")[1] +".svg")
        renderPDF.drawToFile(drawing, directorio + listaTotal[i][0].split(":")[1] +".pdf")
        remove(directorio + listaTotal[i][0].split(":")[1] +".svg")

    fi.close()

# Ejemplo de uso
input_file = "datos.txt"
numDeColumnas = 10
directorio = "C:/Users/Vadose/OneDrive/Documentos/TAGS/prueba/"
directorioBases = "bases/"
max_caracteres = 60

generar_svg_pdf_por_archivo(input_file, numDeColumnas, directorio, directorioBases, max_caracteres)