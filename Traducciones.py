import sys
import csv


SEPARADOR_CSV = ';'
SEPARADOR_LITERAL = '_'
URL_FICHERO_CSV = 'Traducciones.csv'

Resultado = {}

print ('Fichero: ' + URL_FICHERO_CSV)
url = input('Nueva url: ')
if url != '':
    URL_FICHERO_CSV = url

def anadirValor(valor,objJson,variable,index):

    if index == len(variable)-1:
        objJson[variable[index]] = valor
    else:
        if variable[index] in objJson:
            anadirValor(valor,objJson[variable[index]],variable,index+1)
        else:
            objJson[variable[index]] = {}
            anadirValor(valor,objJson[variable[index]],variable,index+1)

try:
    with open(URL_FICHERO_CSV, 'r') as csvfile:
        fichero = csv.reader(csvfile, delimiter=SEPARADOR_CSV)
        for idx,row in enumerate(fichero):
            if idx == 0:
                idiomas = row[1:]
                for idioma in idiomas:
                    Resultado[idioma] = {}
            else:
                for fila,idioma in enumerate(idiomas):
                    anadirValor(row[fila+1],Resultado[idioma],row[0].split(SEPARADOR_LITERAL),0)

    for idioma,contenido in Resultado.items():
        file = open(idioma + '.json', 'w+')
        file.write(str(contenido))
        file.close()

    input('Proceso finalizado...')

except:
    print("ERROR!!!!!", sys.exc_info()[0])
    input()