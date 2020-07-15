from tkinter import *

canvas_width = 200
canvas_height =200
python_green = "#476042"

master = Tk()

w = Canvas(master, 
           width=canvas_width, 
           height=canvas_height)
w.pack()

points = [0,0,canvas_width,canvas_height/2, 0, canvas_height]
w.create_polygon(points, outline=python_green, 
            fill='yellow', width=3)

points = [100, 140, 110, 110, 140, 100, 110, 90, 100, 60, 90, 90, 60, 100, 90, 110]

w.create_polygon(points, outline=python_green, 
            fill='green', width=3)

mainloop()
