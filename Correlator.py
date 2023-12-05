import array
from asyncio.windows_events import NULL
from itertools import count
from locale import normalize
from re import split
import matplotlib.pyplot as plt
import numpy as np
import math
from array import *
import pathlib
from pathlib import Path
import scipy.stats as stats
from scipy.stats import ks_2samp

def calc_middle(mass):
    val = 0
    counter = 0
    
    for a in mass:
        val+=a
        counter+=1
    if not counter == 0 :
        val_print = val/counter
    print("Средний коэффициент корреляции ",val_print)

# Тело функции обработки точек

def append_point(Pointsarr , mass ):
    if len(Pointsarr) == 3:
        Pointsarr[0] = (float(Pointsarr[0]))
        Pointsarr[1] = (float(Pointsarr[1]))
    else:
        print(Pointsarr)
        return
    mass[0].append(Pointsarr[0])
    try:
        mass[1].append(Pointsarr[1])
    except:
        print("Ecxept \n")
    return mass  
    
def make_plot(first_fubction, second_function , i = 0 , modulationType=str()):
    modList = modulationType.split('\\')
    print(modList[0])
    modulationType = str()
    modulationType = modList[0]
    #plt.figure(i)
    plt.figure('КФ')
    stri = "Корреляционная функция"
    stri+=str(i)
    stri+=" "
    stri+=str(modulationType)
    plt.title(stri)
    #stri+=".png"
    result = list()
    KFK = np.correlate(first_fubction[1],second_function[1],mode = 'full')
    NormalizeVal = list()
    AFK1 = np.correlate(first_fubction[1],first_fubction[1],mode = 'full')
    AFK2 = np.correlate(second_function[1],second_function[1],mode = 'full')
    NormalizeVal.append(max(AFK1))
    NormalizeVal.append(max(AFK2))
    m = max(NormalizeVal)
    counter = 0
    for a in KFK:
        result.append(a/m)
        counter= counter+1
    x = list()
    maxval_x = max(first_fubction[0])
    counter = 0
    for b in (first_fubction[0]):
        x.append(b-maxval_x)
    for p in reversed(first_fubction[0]):
        if(counter==0):
            counter+=1
            continue
        x.append(maxval_x-p)
    plt.plot(x,result)
    maxval = max(result)
    #plt.scatter(len(result)/2-1,maxval)
    maxvalstr = 'Коэффициент корреляции '
    maxvalstr+=str(maxval)
    plt.text(0, 0,maxvalstr , fontsize=8,
 # Выравнивание по вертикали и горизонтали
    horizontalalignment='left', verticalalignment='center',
    bbox=dict(facecolor='pink', alpha=1.0))
    plt.xlabel("Частота Гц")
    plt.ylabel("")
    plt.grid()
    dir_path = pathlib.Path.cwd()
    print(stri)
    path = Path(dir_path,'results')
    pathsave = str(path)
    pathsave+='\\'
    pathsave+=(stri)
    print(pathsave)
    #plt.savefig(pathsave.rstrip())
    plt.show()
    return maxval


def meth_Manni_uitman(group1,group2):
    groupp1 = [24, 24, 21, 25, 21,21,23,20,19]
    groupp2 = [24, 24, 21, 25, 23,21,23,20,19]
    observed_data = [8, 6, 10, 7, 8, 11, 9] 
    expected_data = [9, 8, 11, 8, 10, 7, 6] 
    gr1 = list()
    gr2 = list()
    gra = []
    grb = []
    counter = 0
    for a in group1[1]:
        gr1.append(abs(a))
        gra.append(abs(a))
        counter+=1
        if counter == 50:
            break
    counter = 0
    for b in group2[1]:
        gr2.append(abs(b))
        grb.append(abs(b))
        counter+=1
        if counter == 50:
            break
    chi_square_test,pvalue = ks_2samp(gr1,gr2)
    print(f'chi test: U = {int(chi_square_test)}, p = {pvalue:6.4f}')
    df = len(gr1) - 1
    print(df)
    print(stats.chi2.ppf(1-0.05,df=6))
    return a


    


file_name = "base.txt"
file = open(file_name,"r",encoding="utf-8")
ModulationType = file.readline()
USRP =[[],[]]
OMEGA =[[],[]]
counter = 1
list_cor_val = list()
flag = file.readline()
for a in file:
    resultRead = a.split(" ")
    if len(resultRead) == 1:
        list_cor_val.append(make_plot(USRP,OMEGA,1,ModulationType))
        meth_Manni_uitman(USRP,OMEGA)
        USRP.clear()
        OMEGA.clear()
        USRP =[[],[]]
        OMEGA =[[],[]]
        ModulationType = a
    elif len(resultRead) == 2:
        flag = a
    else:
        if flag == "USPR \n":
            USRP = append_point(resultRead,USRP)
        else:
            OMEGA = append_point(resultRead,OMEGA)
calc_middle(list_cor_val)
file.close()  
