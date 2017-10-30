import sys
import csv
import json

SEPARATOR_CSV = ';'
SEPARATOR_LITERAL = '_'
URL_FILE_CSV = 'translate.csv'

Result = {}

print ('File: ' + URL_FILE_CSV)

def addValue(value,objJson,variable,index):

    if index == len(variable)-1:
        objJson[variable[index]] = value
    else:
        if variable[index] in objJson:
            addValue(value,objJson[variable[index]],variable,index+1)
        else:
            objJson[variable[index]] = {}
            addValue(value,objJson[variable[index]],variable,index+1)

try:
    with open(URL_FILE_CSV, 'r') as csvfile:
        fileReaded = csv.reader(csvfile, delimiter=SEPARATOR_CSV)
        for idx,row in enumerate(fileReaded):
            if idx == 0:
                languages = row[1:]
                for language in languages:
                    Result[language] = {}
            else:
                for fila,language in enumerate(languages):
                    addValue(row[fila+1],Result[language],row[0].split(SEPARATOR_LITERAL),0)

    for language,content in Result.items():
        file = open(language + '.json', 'w+')
        file.write(json.dumps(content))
        file.close()

    input('Process completed...')

except:
    print("ERROR!!!!!", sys.exc_info()[0])
    input()
