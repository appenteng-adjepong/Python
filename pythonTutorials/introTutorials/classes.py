numbers = [1, 2, 3]

class Point: # remember to use Pascal naming convention
    def move(self):
        print("move")

    def draw(self):
        print("draw")

point1 = Point()

point1.x = 10
point1.y = 20
print("{}, {}".format(point1.x, point1.y))

point2 = Point()
point2.x = 15
point2.y = 25
print("{}, {}".format(point2.x, point2.y))