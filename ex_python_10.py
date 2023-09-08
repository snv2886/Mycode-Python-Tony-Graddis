# import random
#
#
# # Класс Coin имитирует монету,
# # которую можно подбрасывать.
# class Coin:
#     # Метод __init__ инициализирует
#     # атрибут данных sideup значение Heads
#     def __init__(self):
#         self.__sideup = 'Heads'
#
#     def toss(self):
#         if random.randint(0, 1) == 0:
#             self.__sideup = 'Heads'
#         else:
#             self.__sideup = 'Tails'
#
#     def get_sideup(self):
#         return self.__sideup
#
#
# # Главная функция
# def main():
#     # Создать объект на основе класса Coin.
#     my_coin = Coin()
#
#     # Показать обращенную вверх монету.
#     print('This side of the coin is facing up: ', my_coin.get_sideup())
#
#     # подбросить монету
#     print('Toss the coin ...')
#     for count in range(10):
#         my_coin.toss()
#         my_coin.sideup = 'Heads'
#
#         # Показать обращенную вверх монету
#         print(my_coin.get_sideup())
#
#
# if __name__ == "__main__":
#     main()

# import coin
#
#
# def main():
#     # Создать объект на основе класса Coin.
#     my_coin = coin.Coin()
#
#     # Показать обращенную вверх монету.
#     print('Эта сторона обращена вверх: ', my_coin.get_sideup())
#
#     # Подбросить монету.
#     print('Собираюсь подбросить монету 10 раз:')
#     for count in range(10):
#         my_coin.toss()
#         print(my_coin.get_sideup())
#
#
# if __name__ == "__main__":
#     main()

# import bankaccount
#
#
# def main():
#     # Получить наличный остаток.
#     start_bal = float(input('Введите свой начальный отстаток: '))
#
#     # Создать объект BankAccount.
#     savings = bankaccount.BankAccount(start_bal)
#
#     # Внести на счет зарплату пользователя.
#     pay = float(input('Сколько вы получили на этой неделе? '))
#     print('Вношу эту сумму на ваш счет.')
#     savings.deposit(pay)
#
#     # Показать остаток.
#     print(savings)
#
#     # Получить сумму для снятия с банковского счета.
#     cash = float(input('Какую сумму вы желаете снять? '))
#     print('Снимаю эту сумму с вашего банковского счета.')
#     savings.withdraw(cash)
#
#     # Показать остаток.
#     print(savings)
#
#     # account = bankaccount.BankAccount(1500)
#     # print(f'Остаток составляет ${account.get_balance():,.2f}')
#
#
# if __name__ == "__main__":
#     main()

# Эта программа импортирует имитационный модуль
# и создает три экземпляра класса Coin.
# import coin
#
#
# def main():
#     # Создать три объекта класса Coin.
#     coin1 = coin.Coin()
#     coin2 = coin.Coin()
#     coin3 = coin.Coin()
#
#     # Показать повернутую вверх сторону каждой монеты.
#     print('Вот три монеты, у которых эти стороны повернуты вверх:')
#     print(coin1.get_sideup())
#     print(coin2.get_sideup())
#     print(coin3.get_sideup())
#     print()
#
#     # Подбросить монету.
#     print('Подбрасываю все три монеты ...')
#     print()
#     coin1.toss()
#     coin2.toss()
#     coin3.toss()
#
#     # Показать повернутую вверх сторону.
#     print('Теперь обращены вот эти стороны:')
#     print(coin1.get_sideup())
#     print(coin2.get_sideup())
#     print(coin3.get_sideup())
#     print()
#
#
# if __name__ == "__main__":
#     main()

# This programm tests CellPhone class.
# import cellphone
#
#
# def main():
#     # Get data about telephone.
#     man = input('Enter manufacturer: ')
#     mod = input('Enter phone model: ')
#     retail = float(input('Enter phone retail price: '))
#
#     # Create instance(экземпляр) of the CellPhone class.
#     phone = cellphone.CellPhone(man, mod, retail)
#
#     # Show entered data.
#     print('Here is the data you entered:')
#     print(f'Manufacturer: {phone.get_manufact()}')
#     print(f'Model: {phone.get_model()}')
#     print(f'Phone retail price: {phone.get_retail_price():,.2f}')
#
#
# if __name__ == "__main__":
#     main()

# Создаем 5 объектов CellPhone
# и сохраняем их в списке.
import cellphone


def main():
    # Получить список объекта.
    phone = make_list()
    
    # Показать данные в списке.
    print('Вот введенные Вами данные:')
    display_list(phone)

    # Функция make_list() получает от пользователя данные
    # о пяти телефонах, а затем возвращает список
    # объектов CellPhone


def make_list():
    # Create empty list.
    phone_list = []

    # Добавить 5 объектов в множество.
    print('Enter data about 2 cellphones.')
    for count in range(1, 3):
        # Получить данные о телефоне.
        print('Phone number' + str(count) + ':')
        man = input('Enter manufacturer: ')
        mod = input('Enter model number: ')
        retail = float(input('Enter retail price: '))
        print()

        # Создание экземпляра через цикл for. Создается 5 экземпляров.
        # Создать новый объект в памяти
        # и присвоить его переменной phone.
        phone = cellphone.CellPhone(man, mod, retail)

        # Добавить объект в спиок. Создание списка из номеров экземпляров.
        phone_list.append(phone)

    # Вернуть список.
    return phone_list


# Функция display_list() принимает список с объектами CellPhone
# в качестве аргументов и показывает их данные.
# В списке хранятся номер экземпляров.
def display_list(phone_list):
    print(phone_list)
    # item - номер экземпляра
    for item in phone_list:
        print(item.get_manufact())
        print(item.get_model())
        print(item.get_retail_price())
        print()


if __name__ == "__main__":
    main()
