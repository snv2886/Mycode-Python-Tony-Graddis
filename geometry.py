import circle
import rectangle

# Константы для элементов меню
AREA_CIRCLE_CHOICE = 1
CIRCUMFERENCE_CHOICE = 2
AREA_RECTANGLE_CHOICE = 3
PERIMETER_RECTANGLE_CHOICE = 4
QUIT_CHOICE = 5


def main():
    choice = 0

    while choice != QUIT_CHOICE:
        # Показать меню
        display_menu()
        # Получить вариант выбора пользователя
        choice = int(input("Choose the menu: "))

        # Выполнить выбранное действие
        if choice == AREA_CIRCLE_CHOICE:
            radius = float(input("Enter the radius of circle: "))
            print('The area is equal', circle.area(radius))
        elif choice == CIRCUMFERENCE_CHOICE:
            radius = float(input('Enter the radius of circle: '))
            print('The circuference is equal', circle.circumference(radius))
        elif choice == AREA_RECTANGLE_CHOICE:
            width = float(input("Enter the width of rectangle: "))
            length = float(input("Enter the length of rectagle: "))
            print('The area of rectagle is equal',
                  rectangle.area(width, length))
        elif choice == PERIMETER_RECTANGLE_CHOICE:
            width = float(input("Enter the width of rectangle: "))
            length = float(input("Enter the length of rectagle: "))
            print('The perimeter of rectangle is equal',
                  rectangle.perimeter(width, length))
        elif choice == QUIT_CHOICE:
            print('Exit the program...')
        else:
            print('Error: invalid choice')


def display_menu():
    print()
    print('MENU')
    print('1. Area of Circle')
    print('2. Circumference')
    print('3. Area of rectangle')
    print('4. Perimeter of rectangle')
    print('5. Exit')


main()
