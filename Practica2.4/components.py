import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import star as ST

def readData(path = 'data.txt'):
    data = []
    with open(path, 'r') as dataShop:
        for line in dataShop:
            line = line.strip()
            line = line.split()
            data.append(line)
    return  data

def getStars( UVMag, blueMag,  AbsMag, type):
    stars = ST.star( UVMag, blueMag,  AbsMag, type)
    return stars

def Stars():
    data = readData()
    stars = {}
    for i in range(1,len(data)):
        #star = null
        star = getStars(data[i][0],data[i][1],data[i][2],ST.star.typeStar(float(data[i][1]),float(data[i][2])))
        stars[i] = star
    return stars

def seeStars(stars):
    print('ID     \t UV Magnitude:\t \t Blue Magnitude: \t Absolute Mag: \t\t Type:')
    for n in stars.keys():
        print(str(n)+'\t|\t'+str(stars[n].UVMag)+'\t\t|\t'+str(stars[n].blueMag)+'\t\t|\t'+str(stars[n].AbsMag)+'\t\t|\t'+str(stars[n].typeStar))

def groupStars(stars):
    groups = {'O5': 0,'BO':0,'B5':0,'AO':0,'A5':0,'F0':0,'F5':0,'GO':0,'G5':0,'KO':0,'K5':0,'MO':0,'M5':0,'M8':0}
    for n in stars.keys():
        if (stars[n].typeStar == 'O5'):
            groups['O5'] += 1
        elif (stars[n].typeStar == 'BO'):
            groups['BO']
        elif (stars[n].typeStar == 'B5'):
            groups['B5'] += 1
        elif (stars[n].typeStar == 'AO'):
            groups['AO'] += 1
        elif (stars[n].typeStar == 'A5'):
            groups['A5'] += 1
        elif (stars[n].typeStar == 'F0'):
            groups['F0'] += 1
        elif (stars[n].typeStar == 'F5'):
            groups['F5'] += 1
        elif (stars[n].typeStar == 'GO'):
            groups['GO'] += 1
        elif (stars[n].typeStar == 'G5'):
            groups['G5'] += 1
        elif (stars[n].typeStar == 'KO'):
            groups['KO'] += 1
        elif (stars[n].typeStar == 'K5'):
            groups['K5'] += 1
        elif (stars[n].typeStar == 'MO'):
            groups['MO'] += 1
        elif (stars[n].typeStar == 'M5'):
            groups['M5'] += 1
        else:
            groups['M8'] += 1
    #print(groups)
    return groups

def numType(stars):
    # typesSta = ['O5','BO','B5','AO','A5','F0','F5','GO','G5','KO','K5','MO','M5','M8']
    dataTyoe = []
    for n in stars.keys():
        if (stars[n].typeStar == 'O5'):
            dataTyoe.append(1)
        elif (stars[n].typeStar == 'BO'):
            dataTyoe.append(2)
        elif (stars[n].typeStar == 'B5'):
            dataTyoe.append(3)
        elif (stars[n].typeStar == 'AO'):
            dataTyoe.append(4)
        elif (stars[n].typeStar == 'A5'):
            dataTyoe.append(5)
        elif (stars[n].typeStar == 'F0'):
            dataTyoe.append(6)
        elif (stars[n].typeStar == 'F5'):
            dataTyoe.append(7)
        elif (stars[n].typeStar == 'GO'):
            dataTyoe.append(8)
        elif (stars[n].typeStar == 'G5'):
            dataTyoe.append(9)
        elif (stars[n].typeStar == 'KO'):
            dataTyoe.append(10)
        elif (stars[n].typeStar == 'K5'):
            dataTyoe.append(11)
        elif (stars[n].typeStar == 'MO'):
            dataTyoe.append(12)
        elif (stars[n].typeStar == 'M5'):
            dataTyoe.append(13)
        else:
            dataTyoe.append(14)
    #print(dataTyoe)
    return dataTyoe

def take_third(elem):
    return elem[2]

def Hertzsprung_Russell_Diagram(stars):
    plt.clf()
    data = []
    numtype = numType(stars)
    i = 0
    for n in stars.keys():
        data.append([stars[n].typeStar,stars[n].AbsMag,numtype[i]])
        i += 1
    data = sorted(data, key=take_third)
    x = []
    y = []
    #print(data[0][0])
    for j in range(len(data)):
        x.append(data[j][0])
        y.append(float(data[j][1]))
    
    #print(data[1][0])
    with plt.style.context('Solarize_Light2'):
        plt.scatter(x,y, 100)
        plt.ylim(max(y)+2,min(y)-2)
        plt.xlabel('Star type')
        plt.ylabel('Absolute Magnitude')
        plt.title('Hertzsprung-Russell Diagram of Data')
        plt.savefig("Hertzsprung-Russell.png")
    print("Diagrama de Hertzsprung-Russell guardado en la carpeta de ejecución.")

def freqPlot(stars):
    Hertzsprung_Russell_Diagram(stars)
    frec = groupStars(stars)
    with plt.style.context('Solarize_Light2'):
        plt.bar(frec.keys(),frec.values(),0.95)
        plt.xlabel('Star type')
        plt.ylabel('Frequency')
        plt.title('Frequency of star types')
        plt.savefig("Histograma.png")
    print("Histograma guardado en la carpeta de ejecución.")

        