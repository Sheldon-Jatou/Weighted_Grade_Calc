'''
Created on Dec 25, 2016

@author: Sheldon Jatou
'''
from tkinter import *
import Calculations as cal

main = Tk()

top = Frame(main)
top.pack()

g = Label(top, text='GRADE')
w = Label(top, text='WEIGHT')

g.grid(row=0, sticky=W)
w.grid(row=0, column=2, sticky=E)

grades = [Entry(top), Entry(top), Entry(top)]
weights = [Entry(top), Entry(top), Entry(top)]

for i in range(len(grades)):
    grades[i].grid(row=i + 1)

for i in range(len(weights)):
    weights[i].grid(row=i + 1, column=2)


def add_grade():
    grades.append(Entry(top))
    weights.append(Entry(top))

    grades[-1].grid(row=len(grades))
    weights[-1].grid(row=len(weights), column=2)


def reset_all():
    for i in range(len(grades)):
        grades[i].delete(0, END)
        weights[i].delete(0, END)


add = Button(top, text='ADD ROW', command=add_grade)
add.grid(row=0, columnspan=2, sticky=E)

reset = Button(top, text='   RESET   ', command=reset_all)
reset.grid(row=0, column=2, sticky=W)


bottom = Frame(main)
bottom.pack(side=BOTTOM)
f = '-'
gpa = '-'
letter = '-'
final = Label(
    bottom, text='FINAL GRADE: {0}% GPA: {1} LETTER GRADE: {2}'.format(f, gpa, letter))
final.grid(column=1)


def update_mark():
    f, gpa, letter = cal.calculate_average(grades, weights)
    final.config(
        text='FINAL GRADE: {0}% GPA: {1} GRADE: {2}'.format(f, gpa, letter))

calc = Button(bottom, text='CALCULATE TOTAL',
              command=update_mark)
calc.grid(columnspan=2, sticky=S)

main.mainloop()
