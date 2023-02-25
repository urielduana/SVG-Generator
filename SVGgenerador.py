from os import remove
import re


from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF

directorio = "C:/Users/Vadose/OneDrive/Documentos/Tags/Resultados/prueba/"
numDeColumnas = 10
fileData = open("datos.txt", "r",  encoding='utf8')
fileTitle = open("titulo.txt", "r",  encoding='utf8')

multiArray = []


# Funcion para modificar el contenido
def modificarArray(x, y):
    if(x == 0):
        multiArray[x][y] = re.sub('', "", multiArray[x][y])
    if(x == 2):
        multiArray[x][y] = re.sub("", "", multiArray[x][y])


def generarTitulo():
    title = []

    for linea in fileTitle:
        if linea != '\n':
            linea = re.sub("\\n", "", linea)
            linea = re.sub("\\t", "", linea)

            title.append(linea)
    return title


def generarArray():
    real = []

    # Quitar saltos de linea
    for linea in fileData:
        if linea != '\n':
            linea = re.sub("\\n", "", linea)
            linea = re.sub("\\t", "", linea)

            real.append(linea)

    # Primera extraccion de datos
    listaTotal = []
    for i in range(0, len(real), numDeColumnas):
        listaTotal.append(real[i:i+numDeColumnas])

    return listaTotal


titulo = generarTitulo()
tag = generarArray()
newArray = []

for tags in tag:
    miniArray = []
    for linea, title in zip(tags, titulo):
        a = title + ": " + linea
        if len(a) > 66:
            print(a)
        miniArray.append(a)
    newArray.append(miniArray)


# #Acomodo de datos en Multi array
# for f in range(numDeColumnas):
#     multiArray.append([])
#     for i in range(len(listaTotal)):
#         multiArray[f].append(listaTotal[i][f])


# for y in range(len(multiArray[0])):
#     for x in range(len(multiArray)):
#         #MODIFICACION DE ARRAY
#         modificarArray(x, y)


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

#     drawing = svg2rlg(directorio+"/" +f+".svg")
#     renderPDF.drawToFile(drawing, directorio +"/"+ str(f) +".pdf")
#     remove(directorio + str(f) +".svg")

# print(real)
# print(multiArray)
