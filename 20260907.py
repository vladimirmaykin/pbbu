from turtle import *

shape('turtle')
speed(0)
pensize(4)
colormode(255)
r = 255
g = 255
b = 0
#color('green', (r,g,b))
color((0, 255, 0), (r,g,b))

for j in range(150, 10, -25):
    fillcolor(r,g,b)
    for i in range(8):
        #fillcolor()
        begin_fill()
        circle(j)
        end_fill()
        right(45)
    r -= 30
    g -= 15
    b += 30

mainloop()