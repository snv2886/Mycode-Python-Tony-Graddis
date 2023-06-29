import turtle


def main():
    turtle.hideturtle()
    square(100, 0, 50, 'red')
    square(-150, -100, 200, 'blue')
    square(-200, 150, 75, 'green')

    # Функция square рисует квадрат
    # Параметры x, y - это координаты левого нижнего угла.
    # width - ширина стороны квадрата.
    # color - цвет заливки в виде строки


def square(x, y, width, color):
    turtle.penup()  # поднять перо
    turtle.goto(x, y)  # Переместить в указанное место
    turtle.fillcolor(color)  # Задать цвет заливки
    turtle.pendown()  # опустить перо
    turtle.begin_fill()  # начать заливку
    for count in range(4):  # Нарисовать квадрат
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()  # Завершить заливку


main()
