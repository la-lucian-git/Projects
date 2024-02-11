from random import randint


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if (rectangle.low_left.x < self.x < rectangle.up_right.x and
                rectangle.low_left.y < self.y < rectangle.up_right.y):
            return True
        else:
            return False


class Rectangle:

    def __init__(self, low_left, up_right):
        self.low_left = low_left
        self.up_right = up_right

    def area(self):
        return (self.up_right.x - self.low_left.x) * (self.up_right.y - self.low_left.y)


random_rectangle = Rectangle(
    Point(randint(0, 9), randint(0, 9)),
    Point(randint(10, 19), randint(10, 19))
)

# Interface
print("Rectangle Coordinates: ",
      random_rectangle.low_left.x, ",",
      random_rectangle.low_left.y, "and",
      random_rectangle.up_right.x, ",",
      random_rectangle.up_right.y)

user_point = Point(float(input("Guess X: ")),
                   float(input("Guess Y: "))
                   )

user_area = float(input("Guess rectangle area: "))

print("Your point was inside rectangle: ",
      user_point.falls_in_rectangle(random_rectangle))

print("Your area was off by: ",
      random_rectangle.area() - user_area)
