import os
import csv
import copy

def getResult(fileName):
    with open(fileName, mode='r') as inputFile:
        lines = inputFile.readline()
        results = lines.split('**')
        result = []

        for r in results:
            insList = r.split(',')
            result.append(copy.deepcopy(names))
        
            for i in insList:
                i = i.upper()

                if (i != ''):
                    if i in result[-1].keys():
                        result[-1][i] += 1

                    else:
                        result[-1][i] = 1
                        names[i] = 0
    return result

# read init1.csv / record initial instruction names
with open("init.csv", mode='r') as init:
    reader = csv.reader(init)
    names = {rows[0].upper():0 for rows in reader}

malware = getResult("opcode_malware.txt")
benign = getResult("opcode_benign.txt")

with open("result.csv", mode='w', newline='') as result:
    for name in names.keys():
        for m in range(len(malware)):
            if name not in malware[m].keys():
                malware[m][name] = 0
        
        for b in range(len(benign)):
            if name not in benign[b].keys():
                benign[b][name] = 0

    writer = csv.DictWriter(result, names.keys())
    result.write(",")
    writer.writeheader()

    for m in malware:
        result.write("m,")
        for n in names:
            result.write("%s," % m[n])
        result.write("\n")
    
    for b in benign:
        result.write("b,")
        for n in names:
            result.write("%s," % b[n])
        result.write("\n")
