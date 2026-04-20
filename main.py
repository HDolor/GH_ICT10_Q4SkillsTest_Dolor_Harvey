from pyscript import display, document
import numpy as np
import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR)
import matplotlib.pyplot as plt
days=[]
abse=[]
def grap(i):
    i=0
    while i<5:
        d=document.getElementById('d').value
        a=float(document.getElementById('a').value)
        days.append(d)
        abse.append(a)
        i += 1
    plt.clf()
    plt.plot(days,abse)
    plt.grid(color="green",)
    plt.xlabel('Days')
    plt.ylabel('Absences')
    plt.title("Weekly Attendance (Absences)")
    display(plt.gcf(), target='out')