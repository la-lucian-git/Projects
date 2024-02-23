from random import randint
import turtle


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if (rectangle.point1.x < self.x < rectangle.point2.x and
                rectangle.point1.y < self.y < rectangle.point2.y):
            return True
        else:
            return False


class Rectangle:

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return (self.point2.x - self.point1.x) * (self.point2.y - self.point1.y)


class GuiRectangle(Rectangle):

    def draw(self, canvas):
        canvas.penup()
        canvas.goto(self.point1.x, self.point1.y)
        canvas.pendown()
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)


class GuiPoint(Point):

    def draw(self, canvas, size=5, color="green"):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)


random_rectangle = GuiRectangle(
    Point(randint(0, 400), randint(0, 400)),
    Point(randint(10, 400), randint(10, 400))
)

# Interface
print("Rectangle Coordinates: ",
      random_rectangle.point1.x, ",",
      random_rectangle.point1.y, "and",
      random_rectangle.point2.x, ",",
      random_rectangle.point2.y)

user_point = GuiPoint(
    float(input("Guess X: ")),
    float(input("Guess Y: "))
)

user_area = float(input("Guess rectangle area: "))

print("Your point was inside rectangle: ",
      user_point.falls_in_rectangle(random_rectangle))

print("Your area was off by: ",
      random_rectangle.area() - user_area)

my_turtle = turtle.Turtle()
random_rectangle.draw(canvas=my_turtle)
user_point.draw(canvas=my_turtle)
turtle.done()
