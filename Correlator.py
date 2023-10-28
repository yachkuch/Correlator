# -*- coding: cp1251 -*-
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

# ���������� ����������

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
    plt.figure('���')
    stri = "�������������� ������� "
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
    plt.plot(result)
    maxval = max(result)
    plt.scatter(len(result)/2-1,maxval)
    maxvalstr = '����������� ���������� '
    maxvalstr+=str(maxval)
    plt.text(16, 0.9,maxvalstr , fontsize=8,
 # ������������ �� ��������� � �� �����������
    horizontalalignment='center', verticalalignment='center',
    bbox=dict(facecolor='pink', alpha=1.0))
    plt.xlabel("�������")
    plt.ylabel("")
    plt.grid()
    dir_path = pathlib.Path.cwd()
    print(stri)
    path = Path(dir_path,'results')
    pathsave = str(path)
    pathsave+='\\'
    pathsave+=(stri)
    print(pathsave)
    plt.savefig(pathsave.rstrip())
    plt.show()
    


file_name = "base.txt"
file = open(file_name,"r",encoding="utf-8")
ModulationType = file.readline()
USRP =[[],[]]
OMEGA =[[],[]]
counter = 1
flag = file.readline()
for a in file:
    resultRead = a.split(" ")
    if len(resultRead) == 1:
        make_plot(USRP,OMEGA,1,ModulationType)
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

file.close()  
