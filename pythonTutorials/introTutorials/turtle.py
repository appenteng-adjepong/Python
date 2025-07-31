import turtle
import math
t = turtle.Turtle()

# first turns of turtle
for i in range(4):
    t.forward(50)
    t.right(90)

for i in range(4):
    t.forward(100)
    t.right(90)

for i in range(4):
    t.forward(150)
    t.right(90)

for i in range(4):
    t.forward(200)
    t.right(90)

#re-orient turtle
t.left(90)  

# second set of turns
for i in range(4):
    t.forward(50)
    t.left(90)

for i in range(4):
    t.forward(100)
    t.left(90)

for i in range(4):
    t.forward(150)
    t.left(90)

for i in range(4):
    t.forward(200)
    t.left(90)

# third set of movements
for i in range(4):
    t.forward(50)
    t.right(90)

for i in range(4):
    t.forward(100)
    t.right(90)

for i in range(4):
    t.forward(150)
    t.right(90)

for i in range(4):
    t.forward(200)
    t.right(90)

# re-orient turtle
t.right(180)

# final set of motions
for i in range(4):
    t.forward(50)
    t.right(90)

for i in range(4):
    t.forward(100)
    t.right(90)

for i in range(4):
    t.forward(150)
    t.right(90)

for i in range(4):
    t.forward(200)
    t.right(90)

t.right(45)
t.forward(math.sqrt(80_000))
t.right(180)
t.forward(math.sqrt(80_000))
for i in range(3):
    t.right(90)
    t.forward(math.sqrt(80_000))
    t.right(180)
    t.forward(math.sqrt(80_000))

for i in range(17):
    t.right(5)
    for j in range(4):
        t.right(90)
        t.forward(math.sqrt(80_000)*math.cos(85))
        t.right(180)
        t.forward(math.sqrt(80_000)*math.cos(85))
turtle.done()