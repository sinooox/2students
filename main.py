from tkinter import Tk, Canvas
from grid import Grid
from human import Human
import random

window = Tk()
canvas = Canvas(window, width=800, height=600)
canvas.pack()
grid = Grid(canvas)
grid.display()
group = "ИП-22"
f = open("students.txt", 'r', encoding='utf-8')
peoples = []

for i in f:
    g = i.split(";")
    id = int(g[0])
    name = g[1]
    number = g[2]
    gender = g[4]
    peoples.append({"id": id, 'full_name': name, 'gender': gender,
                    'number': number})

human1 = random.choice(peoples)
name = f"{human1['full_name'].split()[0]}. {human1['full_name'].split()[1][0]}. {human1['full_name'].split()[2][0]}, {group}, №{human1['number']}"
h1 = Human(canvas, name, 100, 500, human1['gender'])
h1.display()

human2 = random.choice(peoples)
name = f"{human2['full_name'].split()[0]}. {human2['full_name'].split()[1][0]}. {human2['full_name'].split()[2][0]}, {group}, №{human2['number']}"
h2 = Human(canvas, name, 500, 500, human2['gender'])
h2.display()

window.mainloop()
