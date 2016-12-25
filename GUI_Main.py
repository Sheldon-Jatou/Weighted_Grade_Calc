'''
Created on Dec 25, 2016

@author: Sheldon Jatou
'''
from tkinter import *

main = Tk()

g = Label(main, text='GRADE')
w = Label(main, text='WEIGHT')

g.grid(row=0, sticky=W)
w.grid(row=0, column=2, sticky=W)

grades = [Entry(main), Entry(main), Entry(main)]
weights = [Entry(main), Entry(main), Entry(main)]

for i in range(len(grades)):
    grades[i].grid(row=i + 1)

for i in range(len(weights)):
    weights[i].grid(row=i + 1, column=2)

f = 0
final = Label(main, text='FINAL GRADE: {}'.format(f))
final.grid(column=1)


def calculate_average():
    totals = []
    global f

    for i in range(len(grades)):
        if grades[i].get() != '' and weights[i].get() != '':
            total = (float(grades[i].get()) / 100) * \
                (float(weights[i].get()) / 100)
            totals.append(total)
        elif (grades[i].get() == '' or weights[i].get() == '') and (grades[i].get() != '' and weights[i].get() != ''):
            pass

    f = round(sum(totals) * 100, 1)
    final.config(text='FINAL GRADE: {}'.format(f))


calc = Button(main, text='CALCULATE TOTAL', command=calculate_average)
calc.grid(columnspan=4)


main.mainloop()
