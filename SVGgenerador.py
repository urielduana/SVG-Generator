from os import remove
import re
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF

directorio = "C:/Users/Vadose/OneDrive/Documentos/TAGS/1max_caracteres2/"
numDeColumnas = 10
fi = open("datos.txt", "r", encoding='utf8')
max_caracteres = 60
real = []
multiArray = []


# Función para modificar el contenido
def modificarArray(x, y):
    if x == 0:
        multiArray[x][y] = re.sub('', "", multiArray[x][y])
    if x == 2:
        multiArray[x][y] = re.sub("", "", multiArray[x][y])


for linea in fi:
    print(linea)
    if linea != '\n':
        linea = re.sub("\\n", "", linea)
        linea = re.sub("\\t", "", linea)

        real.append(linea)

# Primera extracción de datos
listaTotal = []
for i in range(0, len(real), numDeColumnas):
    listaTotal.append(real[i:i + numDeColumnas])

# Dividir strings si superan los max_caracteres caracteres
for i, lista in enumerate(listaTotal):
    for j, string in enumerate(lista):
        if len(string) > max_caracteres:
            idx = string[:max_caracteres].rfind(" ")
            if idx == -1:
                idx = string[:max_caracteres].rfind("-")
            if idx == -1:
                idx = string[:max_caracteres].rfind(",")
            if idx == -1:
                idx = 59
            listaTotal[i][j:j + 1] = [string[:idx+1], string[idx+1:]]

# Imprimir resultados
print("Longitud de listaTotal:", len(listaTotal))
for i, lista in enumerate(listaTotal):
    print("-----------------")
    print("Array", i+1, "- longitud:", len(lista))
    print("-----------------")
    for j, string in enumerate(lista):
        print("Elemento", j+1, "-", string)

# y=0

# for f in multiArray[0]:
#     read = open(directorio + "Base.svg", "r",  encoding='utf8')

#     write= open(directorio + str(f) +".svg", 'w', encoding='utf8')

#     for linea in read:
#         for x in range(len(multiArray)):
#                             #CAMBIAR[NUM]AQUI CLAVE
#             linea = re.sub("CAMBIAR"+str(x)+"AQUI",multiArray[x][y],linea)
#         write.write(linea)
#     y=y+1
#     write.close()

#     drawing = svg2rlg(directorio + str(f) +".svg")
#     renderPDF.drawToFile(drawing, directorio + str(f) +".pdf")
#     remove(directorio + str(f) +".svg")