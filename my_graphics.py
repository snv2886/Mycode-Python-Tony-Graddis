import turtle

# Функция square рисует квадрат
# Параметры x, y - это координаты левого нижнего угла
# Параметр width - это ширина стороны квадрата
# Параметры color - цвет заливки в виде строки


def square(x, y, width, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()  # Начать заливку
    for count in range(4):  # Нарисовать квадрат
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()  # Закончить заливку


# Функция circle рисует круг
# Параметры x, y - это координаты центральной точки
# Параметр radius  - это радиус круга
# Параметр color - цвет заливки


def circle(x, y, radius, color):
    turtle.penup()
    turtle.goto(x, y - radius)  # Спозиционировать черепаху
    turtle.fillcolor(color)  # Задать цвет заливки
    turtle.pendown()
    turtle.begin_fill()  # Начать заливку
    turtle.circle(radius)
    turtle.end_fill()

# Функция line рисует линию от (startX, startY) до (endX, endY)


def line(startX, startY, endX, endY, color):
    turtle.penup()
    turtle.goto(startX, startY)
    turtle.pendown()
    turtle.pencolor(color)
    turtle.goto(endX, endY)
