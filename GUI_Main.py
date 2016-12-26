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


def reset_all():
    for i in range(len(grades)):
        grades[i].delete(0, END)
        weights[i].delete(0, END)


add = Button(top, text='ADD ROW', command=add_grade)
add.grid(row=0, columnspan=2, sticky=E)

reset = Button(top, text='   RESET   ', command=reset_all)
reset.grid(row=0, column=2, sticky=W)


def calculate_average():
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

    if f in range(0, 50):
        gpa = 0
        letter = 'F'
    elif f in range(50, 53):
        gpa = 0.7
        letter = 'D-'
    elif f in range(53, 57):
        gpa = 1.0
        letter = 'D'
    elif f in range(57, 60):
        gpa = 1.3
        letter = 'D+'
    elif f in range(60, 63):
        gpa = 1.7
        letter = 'C-'
    elif f in range(63, 67):
        gpa = 2.0
        letter = 'C'
    elif f in range(67, 70):
        gpa = 2.3
        letter = 'C+'
    elif f in range(70, 73):
        gpa = 2.7
        letter = 'B-'
    elif f in range(73, 77):
        gpa = 3.0
        letter = 'B'
    elif f in range(77, 80):
        gpa = 3.3
        letter = 'B+'
    elif f in range(80, 85):
        gpa = 3.7
        letter = 'A-'
    elif f in range(85, 90):
        gpa = 4.0
        letter = 'A'
    elif f >= 90:
        gpa = 4.0
        letter = 'A+'

    final.config(
        text='FINAL GRADE: {0}% GPA: {1} GRADE: {2}'.format(f, gpa, letter))

bottom = Frame(main)
bottom.pack(side=BOTTOM)

f = '-'
gpa = '-'
letter = '-'
final = Label(
    bottom, text='FINAL GRADE: {0}% GPA: {1} LETTER GRADE: {2}'.format(f, gpa, letter))
final.grid(column=1)


calc = Button(bottom, text='CALCULATE TOTAL', command=calculate_average)
calc.grid(columnspan=2, sticky=S)

for i in range(5):
    Grid.rowconfigure(main, i, weight=1)
    Grid.columnconfigure(main, i, weight=1)

    Grid.rowconfigure(top, i, weight=1)
    Grid.columnconfigure(top, i, weight=1)

    Grid.rowconfigure(bottom, i, weight=1)
    Grid.columnconfigure(bottom, i, weight=1)

main.mainloop()
