import csv

def getDataandHeaders(archivo_csv):
    # Open the csv file and get the data
    with open(archivo_csv, encoding='utf-8') as archivo_csv:
        reader_csv = csv.reader(archivo_csv, delimiter=',')
        # Saving all the rows in a list
        content = []
        for header in reader_csv:
            content.append(header)
        # Getting headers of each column
        header = content.pop(0)
        size = len(header)
        return header, content, size
    

def addColon(header):
    # Adding ':' to the end of each header if it doesn't have it
    for i in range(len(header)):
        if not(header[i].endswith(": ") or header[i].endswith(":")):
            header[i] = header[i] + ": "
        elif header[i].endswith(": "):
            pass
        elif header[i].endswith(":"):
            header[i] = header[i] + " "
    return header


def setHeaders(header, content):
    # Adding the headers to the beginning of each row
    ordered_content = []
    for i in range(len(content)):
        for j in range(len(content[i])):
            ordered_content.append(f'{header[j]}{content[i][j]}')
    return ordered_content

    
def createTxtFile(ordered_content, output_dir):
    #Create a txt file with the ordered content
    with open(output_dir, 'w', encoding='utf-8') as archivo_txt:
        for i in range(len(ordered_content)):
            archivo_txt.write(ordered_content[i] + '\n')

# Main
def generate_txt(archivo_csv, output_dir):
    header, content, size = getDataandHeaders(archivo_csv)
    header = addColon(header)
    ordered_content = setHeaders(header, content)
    createTxtFile(ordered_content, output_dir)
    return size

