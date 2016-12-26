'''
Created on Dec 25, 2016

@author: Sheldon Jatou
'''
from tkinter import *


def gpa_calc(n):
    g = ''
    l = ''
    if len(n) == 2:
        if int(n[0]) < 5:
            g = '0.0'
            l = 'F'
            return g, l
        elif int(n[0]) == 5:
            if int(n[1]) in range(0, 3):
                g = '0.7'
                l = 'D-'
                return g, l
            else:
                g += '1.'
                l += 'D'
        elif int(n[0]) == 6 and int(n[1]) in range(0, 3):
            g = '1.7'
            l = 'C-'
            return g, l
        elif (int(n[0]) == 6 and int(n[1]) in range(3, 10)) or (int(n[0]) == 7 and int(n[1]) in range(0, 3)):
            g += '2.'
            if int(n[0]) != 7:
                l += 'C'
            else:
                l += 'B'
        elif (int(n[0]) == 7 and int(n[1]) in range(3, 10)) or (int(n[0]) == 8 and int(n[1]) in range(0, 5)):
            g += '3.'
            if int(n[0]) != 8:
                l += 'B'
            else:
                l += 'A'
        elif int(n[0]) == 8 and int(n[1]) >= 5:
            g += '4.0'
            l = 'A'
            return g, l
        if int(n[0]) < 8:
            if int(n[1]) in range(0, 3):
                g += '7'
                l += '-'
            elif int(n[1]) in range(3, 7):
                g += '0'
            elif int(n[1]) in range(7, 10):
                g += '3'
                l += '+'
        elif int(n[0]) == 8:
            if int(n[1]) in range(0, 5):
                g += '7'
                l += '-'
            elif int(n[1]) >= 5:
                g += '0'
                l += '+'
        elif int(n[0]) > 8:
            g = '4.0'
            l = 'A+'
            return g, l
        return g, l
    elif len(n) == 1:
        g = '0.0'
        l = 'F'
        return g, l


def calculate_average(grades, weights):
    totals = []
    global f, gpa, letter

    for i in range(len(grades)):
        try:
            if grades[i].get() != '' and weights[i].get() != '':
                total = (float(grades[i].get()) / 100) * \
                    (float(weights[i].get()) / 100)
                totals.append(total)
        except ValueError:
            pass

    f = round(sum(totals) * 100, 2)
    gpa, letter = gpa_calc(str(round(f)))

    return f, gpa, letter
