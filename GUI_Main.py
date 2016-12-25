'''
Created on Dec 25, 2016

@author: Sheldon Jatou
'''
from tkinter import *

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

    print(len(grades))

add = Button(top, text='ADD GRADE')
add.bind('<Button-1>', add_grade)
add.grid(row=0, columnspan=4)


def calculate_average():
    totals = []
    global f

    for i in range(len(grades)):
        try:
            if grades[i].get() != '' and weights[i].get() != '':
                total = (float(grades[i].get()) / 100) * \
                    (float(weights[i].get()) / 100)
                totals.append(total)
        except ValueError:
            pass

    f = round(sum(totals) * 100, 1)

    final.config(text='FINAL GRADE: {}'.format(f))

bottom = Frame(main)
bottom.pack(side=BOTTOM)

f = 0
final = Label(bottom, text='FINAL GRADE: {}'.format(f))
final.grid(column=1)


calc = Button(bottom, text='CALCULATE TOTAL', command=calculate_average)
calc.grid(columnspan=4, sticky=S)


main.mainloop()
