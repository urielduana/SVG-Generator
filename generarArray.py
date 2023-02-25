import re

numDeColumnas = 11
fi = open("datos.txt", "r",  encoding='utf8')

real  = []
multiArray = []

#Funcion para modificar el contenido
def modificarArray(x, y):
    if(x==0):
        multiArray[x][y] = re.sub('',"",multiArray[x][y])
    if(x==2):
        multiArray[x][y] = re.sub("","",multiArray[x][y])

#Quitar saltos de linea
for linea in fi:
    if linea != '\n':
        linea = re.sub("\\n","",linea)
        linea = re.sub("\\t","",linea)

        real.append(linea)

#Primera extraccion de datos
listaTotal = []
for i in range(0, len(real), numDeColumnas):
    listaTotal.append(real[i:i+numDeColumnas])

for tag in listaTotal:
    print(tag)