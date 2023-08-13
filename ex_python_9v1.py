# phonebook = {'Kris': '555-111', 'Katy': '555-222', 'Jhoanna': '555-333'}
# num_items = len(phonebook)
# print(num_items)
# Ключ- имя; значние- список
# test_score = {'Kayla': [88, 92, 100],
#               'Luis': [95, 74, 81],
#               'Sofi': [72, 88, 91],
#               'Itan': [79, 75, 78]}
# print(test_score['Sofi'])
# kayla_score = test_score['Kayla']
# print(kayla_score)
# mixed_up = {'abc': 1, 999: 'tada tada', (3, 6, 9): [3, 6, 9]}
# employee = {'name': 'Kevin Smith', 'ID': 12345, 'rate': 25.75}
# print(employee['ID'])
# phonebook = {}
# phonebook['Kris'] = '555-111'
# phonebook['Katy'] = '555-222'
# phonebook['Chloe'] = '555-333'
# print(phonebook)


# Эта программа применяет словарь для хранения
# имен и дней рождений друзей

# Глобальные константы для пунктов меню
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5


# Главная функция
def main():
    # Создать пустой словарь
    birthdays = {}

    # Инициализировать переменную для выбора пользователя
    choice = 0

    while choice != QUIT:
        # получить выбранный пользователем пункт меню
        choice = get_menu_choice()

        # обработать выбранный вариант действий.
        if choice == LOOK_UP:
            look_up(birthdays)
        elif choice == ADD:
            add(birthdays)
        elif choice == CHANGE:
            change(birthdays)
        elif choice == DELETE:
            delete(birthdays)

def get_menu_choice():
    print()
    print('Друзья и их дни рождения')
    print('------------------------')
    print('1. Найти день рождения')
    print('2. Добавить новый день рождения')
    print('3. Изменить день рождения')
    print('4. Удалить день рождения')
    print('5. Выйти из программы')
    print()

    # Получить выбранный пользователем пункт
    choice = int(input('Введите выбранный пункт: '))

    # Проверить выбранный пункт на допустимость
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Введите выбранный пункт: '))

    # вернуть выбранный пользователем пункт
    return choice


def look_up(birthdays):
    # получить искомое имя
    name = input('Введите имя: ')
    # отыскать его в словаре
    print(birthdays.get(name, 'Не найдено.'))


def add(birthdays):
    # Получить имя и день рождения
    name = input('Введите имя: ')
    bday = input('Введите день рождения: ')

    # Если имя не существует, то его добавить
    if name not in birthdays:
        birthdays[name] = bday
    else:
        print('Эта запись уже существует.')


def change(birthdays):
    # Получить искомое имя
    name = input('Введите имя: ')

    if name in birthdays:
        # Получить новый день рождения
        bday = input('Введите день рождения: ')
        # обновить запись
        birthdays[name] = bday
    else:
        print('Это имя не найдено.')


def delete(birthdays):
    name = input('Введите имя: ')
    if name in birthdays:
        del birthdays[name]
    else:
        print('Это имя не найдено.')


if __name__ == '__main__':
    main()
