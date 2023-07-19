# mylist = [10, 20, 30, 40]
# # print(mylist[0], mylist[1], mylist[2], mylist[3])
# index = 0
# while index < 4:
#     print(mylist[index])
#     index += 1
# mylist = [10, 20, 30, 40]
# print(mylist[-1], mylist[-2], mylist[-3], mylist[-4])
# index = -1
# while index > -5:
#     print(mylist[index])
#     index += -1
# index = 0
# while index < 5:
#     print(mylist[index])
#     index += 1

# mylist = [10, 20, 30, 40]
# index = 0
# while index < len(mylist):
#     print(mylist[index])
#     index += 1

# names = ['Jenny', 'Kelly', 'Chloya', 'Obry']
# for index in range(len(names)):
#     print(names[index])

# NUM_DAYS = 5
#
#
# def main():
#     sales = [2] * 5
#     print("Enter sales for each day.")
#     print(sales)
#
#     for index in range(len(sales)):
#         sales[index] = float(input(f'Enter sales for day {index + 1}: '))
#
#     # Show sales Value
#     for value in sales:
#         print(value)
#
#
# if __name__ == "__main__":
#     main()

# list = [1, 2, 3, 4]
# list[2] = 99
# print(list)

# numbers = list(range(1, 10, 2))
# print(numbers)
# for n in numbers:
#     print(n)

# numbers = [1, 2, 3, 4, 5]
# print(numbers)
# print(numbers[-2])

# numbers1 = [1, 2, 3, 4, 5]
# numbers2 = [1, 2, 3, 4, 5]
# numbers2 += numbers1
# print(numbers1)
# print(numbers2)

# Присваиваем список переменной numbers
# numbers = [1, 2, 3, 4, 5]
# print(numbers)
# print(numbers[:])
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(numbers[1:8:2])
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(numbers[5:-2])

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# my_list = numbers[-3:]
# print(my_list)

# def main():
#     prod_num = ['V451', 'F987', 'Q143', 'R688']
#     search = input("Enter the number of product: ")
#     if search not in prod_num:
#         print(f'{search} has been found!')
#     else:
#         print(f"{search} hasn't been found!")
#
#
# if __name__ == "__main__":
#     main()

# names = ['Jim', 'Jill', 'Jhon', 'Jasmin']
# if 'Jasmn' not in names:
#     print("Can't find Jasmin")
# else:
#     print("Jasmin's family:")
#     print(names)

# def main():
#     # Create empty list
#     name_list = []
#     # Создать переменную для управления списком
#     again = 'y'
#     # Add some names to the list
#     while again == 'y':
#         name = input("Enter a name: ")
#         name_list.append(name)
#         again = input("Do you want to continue (y/n)? ")
#         print()
#     # show the list
#     print("Here are the names: ")
#     for name in name_list:
#         print(name)
#
#
# if __name__ == "__main__":
#     main()

# def main():
#     food = ['Pizza', 'Burger', 'Chips']
#     print(food)
#     item = input("What product do you want to change? ")
#     # find index
#     item_index = food.index(item)
#     new_item = input("Enter new product: ")
#     # Change item
#     food[item_index] = new_item
#     print(food)
#
#
# if __name__ == "__main__":
#     main()

# def main():
#     names = ['Mike', 'Joe', 'Tom']
#     print(names)
#     # add new name to the list in the middle of the list
#     names.insert(0, 'Chloe')
#     print("List after 'insert':")
#     print(names)
#
#
# if __name__ == "__main__":
#     main()

# my_list = [1, 2, 6, 3, 7, 1, 4, 5, 9]
# print("Here is the list:", my_list)
# my_list.sort()
# print("Sorted list:", my_list)

# my_list = ['beta', 'alfa', 'gamma']
# print(my_list)
# my_list.sort()
# print(my_list)

# def main():
#     food = ['Pizza', 'Pasta', 'Burger', 'Chips']
#     print(food)
#     # Назовите продукт, который хотите удалить
#     item = input("What product do you want to remove? ")
#
#     try:
#         # Remove the item
#         food.remove(item)
#         print("Product was removed successfully!")
#     except ValueError:
#         print("This product wasn't found.")
#
#     print(food)
#
#
# if __name__ == "__main__":
#     main()

# my_list = [1, 2, 6, 3, 7, 1, 4, 5, 9]
# print("Initial order", my_list)
# my_list.reverse()
# print("Reversed order", my_list)

# my_list = [1, 2, 3, 4, 5]
# print("Initial list:", my_list)
# del my_list[2]
# print("Deleted element:", my_list)

# my_list = [1, 2, 6, 3, 7, 1, 4, 5, 9]
# print("Minimal number is: ", max(my_list))

# names = []
# names[0] = 'Vandy'
# print(names)

# list1 = [1, 2, 3, 4]
# list2 = list1
# print("list1: ", list1)
# print("list2: ", list2)
# print("First index was changed.")
# list1[0] = 99
# print("list1: ", list1)
# print("list2: ", list2)

# list1 = [1, 2, 3, 4]
# # Создаем пустой список
# list2 = []
# # Скопировать элементы списка1 в список2
# for item in list1:
#     list2.append(item)

# barist_pay.py
# NUM_EMPLOYEES = 6
#
#
# def main():
#     # Создать список с одним индексом и одним значением * NUM_EMPLOYEES
#     hours = [0] * NUM_EMPLOYEES
#     print(hours)
#     # Внести часы для каждого сотрудника
#     for index in range(NUM_EMPLOYEES):
#         hours[index] = float(input(f'Enter the number of spent hours '
#                                    f'by employee {index + 1}: '))
#     print("The list of hours: ", hours)
#     # Get payment per hour
#     pay_rate = float(input("Enter pay rate per hour: "))
#     # Show gross payment for each employee
#     for index in range(NUM_EMPLOYEES):
#         gross_pay = hours[index] * pay_rate
#         print(f'Gross payment of employee {index + 1} is ${gross_pay:,.2f}')
#
#
# if __name__ == "__main__":
#     main()

# def main():
#     numbers = [1, 2, 3, 4, 5]
#     # накопитель total
#     total = 0
#     for value in numbers:
#         total += value
#     print(f'The sum of all element is: {total}')
#
#
# if __name__ == "__main__":
#     main()

# def main():
#     total = 0
#     numbers = [2.5, 7.3, 6.5, 4.0, 5.2]
#     # считаем сумму
#     for value in numbers:
#         total += value
#
#     # вычисляем среднее арефметическое
#     average = total / len(numbers)
#     print(f'The average is: {average:,.2f}')
#
#
# if __name__ == "__main__":
#     main()

# def main():
#     numbers = [2, 4, 6, 7, 10]
#     # показать сумму значений элементов списка
#     # через функцию get_total
#     print(f'The sum is: {get_total(numbers)}')
#
#
# # Функция get_total принимает список в качестве аргумента
# # и возвращает сумму.
# def get_total(my_list):
#     total = 0
#     for value in my_list:
#         total += value
#     # Возвращаем сумму
#     return total
#
#
# if __name__ == "__main__":
#     main()

# def main():
#     # Получить список с хранящимися в нем значениями
#     # Переменная присваивает функцию, которая возвращает список
#     numbers = get_values()
#     print("Numbers in the list:")
#     print(numbers)
#
#
# def get_values():
#     # Создать пустой список
#     my_list = []
#     # Создать переменную для управления циклом
#     again = 'y'
#     # Добавить свои значения в список.
#     while again == 'y':
#         my_value = float(input("Enter your value: "))
#         my_list.append(my_value)
#         again = input("Do you want to add one more number? (y/n) ")
#         print()
#     # Вернуть список в функцию
#     return my_list
#
#
# if __name__ == "__main__":
#     main()

# def main():
#     # Получить от пользователя оценки.
#     scores = get_scores()
#     # Get total score
#     total = get_total(scores)
#     # Get lowest score
#     low_score = min(scores)
#     # Subtract the lowest score ftom total
#     total -= low_score
#     # Get average score minus lowest score
#     average = total / (len(scores) - 1)
#     # Show the average score.
#     print(f'The average score (minus lowest score) is: {average:,.1f}')
#
#
# # Define function get_scores()
# def get_scores():
#     # Create empty score list.
#     score_list = []
#     # Define repeat variable
#     again = 'y'
#     # Fill in the list
#     while again == 'y':
#         value = float(input("Enter the score: "))
#         score_list.append(value)
#         again = input("Do you want to add one more score? (y/n) ")
#     # return the list
#     return score_list
#
#
# # Define function get_total(scores)
# def get_total(value_list):
#     # define accumulator
#     total = 0
#     # calculate the sum of the elements in the list
#     for num in value_list:
#         total += num
#     return total
#
#
# if __name__ == "__main__":
#     main()

# import random
#
# names = ['Jenny', 'Kelly', 'Chloe', 'Obri']
# winner = random.choice(names)
# print(winner)

# import random
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# selected_list = random.choices(numbers, k=5)
# print(selected_list)

# import random
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# selected_list = random.sample(numbers, k=5)
# print(selected_list)

# def main():
#     # Create list
#     cities = ['Moscow', 'New-York', 'Boston', 'Atlanta', 'Dallas']
#     # open file
#     my_file = open('cities.txt', 'w')
#     # Write the list to the file
#     for value in cities:
#         my_file.write(value + '\n')
#     my_file.close()
#
#
# if __name__ == "__main__":
#     main()

# def main():
#     my_file = open("cities.txt", 'r')
#     # Read the line
#     cities = my_file.readlines()
#     print(cities)
#     my_file.close()
#
#     # Удаляем '\n'
#     index = 0
#     while index < len(cities):
#         cities[index] = cities[index].rstrip('\n')
#         index += 1
#     print(cities)
#
#
# if __name__ == "__main__":
#     main()

# def main():
#     # Create a list
#     numbers = [1, 2, 3, 4, 5, 6, 7, 8]
#     my_file = open("numberlist.txt", 'w')
#     # Use a loop 'for' to write the list to the file
#     for num in numbers:
#         # my_file.write(f'{num}\n')
#         my_file.write(str(num) + '\n')
#     my_file.close()
#
#
# if __name__ == "__main__":
#     main()

# def main():
#     my_file = open('numberlist.txt', 'r')
#     numbers = my_file.readlines()
#     print(numbers)
#     my_file.close()
#     sum = numbers[0] + numbers[1]
#     print(sum)
#
#     # convert sting to numbers using int
#     index = 0
#     while index < len(numbers):
#         numbers[index] = int(numbers[index])
#         index += 1
#     print(numbers)
#     sum = numbers[0] + numbers[1]
#     print(sum)
#
#
# if __name__ == "__main__":
#     main()

# list1 = [1, 2, 3, 4]
# list2 = []
# for item in list1:
#     list2.append(item)
# print(list1)
# print(list2)
# list2[1] = 99
# print(list1)
# print(list2)

# list1 = [1, 2, 3, 4]
# list2 = [item for item in list1]
# print(list1)
# print(list2)

# list1 = [1, 2, 3, 4]
# list2 = []
# for item in list1:
#     list2.append(item**2)
# print(list1)
# print(list2)

# list1 = [1, 2, 3, 4]
# list2 = [item**2 for item in list1]
# print(list1)
# print(list2)

# str_list = ['Mike', 'Jessy', 'Chloe']
# len_list = []
# for item in str_list:
#     len_list.append(len(item))
# print(str_list)
# print(len_list)

# str_list = ['Mike', 'Jessy', 'Chloe']
# len_list = [len(item) for item in str_list]
# print(str_list)
# print(len_list)

# list1 = [1, 12, 2, 20, 3, 15, 4]
# list2 = []
# for item in list1:
#     if item > 10:
#         list2.append(item)
# print(list1)
# print(list2)

# list1 = [1, 12, 2, 20, 3, 15, 4]
# list2 = [item for item in list1 if item < 10]
# print(list1)
# print(list2)
#
# list1 = ['Jackson', 'Smith', 'Hilderbrand', 'Jhons']
# list2 = [name for name in list1 if len(name) < 6]
# print(list1)
# print(list2)

# list1 = [1, 12, 2, 20, 3, 15, 4]
# list2 = [item*2 for item in list1]
# print(list1)
# print(list2)

# def main():
#     # Создать двумерный список.
#     values = [[1, 2, 3],
#               [10, 20, 30],
#               [100, 200, 300]]
#     # Вывести на экран элементы списка.
#     for row in values:
#         for element in row:
#             print(element)
#
#
# if __name__ == '__main__':
#     main()

# import random
# ROW = 2
# COL = 4
#
#
# def main():
#     # Создать двумерный список.
#     values = [[0, 0, 0, 0],
#               [0, 0, 0, 0]]
#     # Fill in two-demensional list with random numbers.
#     for r in range(ROW):
#         for c in range(COL):
#             values[r][c] = 0
#     print(values)
#
#
# if __name__ == '__main__':
#     main()
# my_tuple = (1, 2, 3, 4, 5)
# print(my_tuple)
# names = ('Tom', 'John', 'Chloe')
# for n in names:
#     print(n)

# names = ('Tom', 'John', 'Chloe')
# for n in range(len(names)):
#     print(names[n])
# number_tuple = (1, 2, 3)
# number_list = list(number_tuple)
# print(number_list)
#
# str_list = ['Tom', 'Mike', 'Chloe']
# str_tuple = tuple(str_list)
# print(str_tuple)

# import matplotlib.pyplot as plt
#
#
# def main():
#     x_coordinat = [0, 1, 2, 3, 4]
#     y_coordinat = [0, 3, 1, 5, 2]
#     # Вызывается функция 'plot'
#     # Функция 'plot' создала лин. граф. в оперативной памяти.
#     plt.plot(x_coordinat, y_coordinat, 's')
#
#     # Add title
#     plt.title('Образец данных')
#
#     # Добавить на оси описательные метки.
#     plt.xlabel('Год')
#     plt.ylabel('Объем продаж')
#
#     # Настроить метки данных
#     plt.xticks([0, 1, 2, 3, 4], ['2016', '2017', '2018', '2019', '2020'])
#     plt.yticks([0, 1, 2, 3, 4, 5], ['$0m', '$1m', '$2m', '$3m', '$4m', '$5m'])
#
#     # Add grid
#     plt.grid(True)
#
#     # Вывести график на экран show()
#     plt.show()
#
#
# if __name__ == '__main__':
#     main()

# import matplotlib.pyplot as plt
#
#
# def main():
#     # Создать список с координатами X левого края каждого столбика
#     left_edge = [0, 10, 20, 30, 40]
#     # Создать список с высотами каждого столбика
#     height = [100, 200, 300, 400, 500]
#
#     # bar width
#     bar_width = 5
#
#     # Построить гистограмму.
#     plt.bar(left_edge, height, bar_width,
#             color=('r', 'g', 'b', 'm', 'k'))
#
#     # Show bar chart
#     plt.show()
#
#
# if __name__ == '__main__':
#     main()

# import matplotlib.pyplot as plt
#
#
# def main():
#     # Координаты x, y
#     left_edge = [0, 10, 20, 30, 40]
#     height = [100, 200, 300, 400, 200]
#
#     # bar width
#     bar_width = 8
#
#     # create bar chat in memory
#     plt.bar(left_edge, height, bar_width,
#             color=('k', 'b', 'm', 'y', 'c'))
#
#     # title
#     plt.title('Продажи с разбивкой по годам')
#
#     # Подпиписать ось x , y
#     plt.xlabel('Год')
#     plt.ylabel('Объем продаж')
#
#     # Деления на оси x , y
#     plt.xticks([0, 10, 20, 30, 40],  # смещение тикета[5, 15, 25, 35, 45]
#                ['2016', '2017', '2018', '2019', '2020'])
#     plt.yticks([0, 100, 200, 300, 400, 500],  # деления на оси y
#                ['$0m', '$1m', '$2m', '$3m', '$4m', '$5m'])
#
#     # Show bar
#     plt.show()
#
#
# if __name__ == '__main__':
#     main()

# import matplotlib.pyplot as plt
#
#
# def main():
#     sales = [100, 400, 300, 600]
#
#     # Создать список меток
#     sales_labels = ['1 quater', '2 quater', '3 quater', '4 quater']
#
#     # Creat pie chart
#     plt.pie(sales, labels=sales_labels)
#
#     # Add title
#     plt.title('Sales by quater')
#
#     # Show pie chart
#     plt.show()
#
#
# if __name__ == '__main__':
#     main()
# my_list = [1, 2, 3, 4, 5, 6, 7, 8]
# print(my_list[-4:])
# value = [2] * 5
# print(value)
# names = ['Энштейн', 'Ньютон', 'Коперник', 'Кеплер']
# for name in names:
#     print(name)

# def main():
#     my_list = [1, 2, 3, 4, 5, 6, 7, 8]
#     print(my_function(my_list))
#
#
# def my_function(my_list2):
#     total = 0
#     for num in my_list2:
#         total += num
#     return total
#
#
# if __name__ == '__main__':
#     main()


# names = ['Энштейн', 'Ньютон', 'Коперник', 'Кеплер', 'Ruby']
# if 'Ruby' in names:
#     print("We found Ruby")
# else:
#     print("We didn't find Ruby")

# list1 = [3, 2, 4, 120, 84, 220, 500, 25]
# list2 = [item for item in list1 if (item % 2) == 0]
# print(list2)

# ROWS = 5
# COL = 3
#
# list1 = [[0, 0, 0],
#          [0, 0, 0],
#          [0, 0, 0],
#          [0, 0, 0],
#          [0, 0, 0]]
#
# for r in range(ROWS):
#     for c in range(COL):
#         list1[r][c] = int(input("Enter the number: "))
# print(list1)

# ex.7.1
# def main():
#     # создать пустой список
#     sales_week = []
#     total = 0
#     # список дней недели
#     week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
#             'Friday', 'Saturday', 'Sunday']
#
#     # продажи за день
#     for index in range(len(week)):
#         sales_per_day = int(input(f'Enter sales for {week[index]}: '))
#         sales_week.append(sales_per_day)
#
#     for num in sales_week:
#         total += num
#     print(f'The total amoun for week is: {total}')
#
#
# if __name__ == '__main__':
#     main()

# ex.7.2
# import random
#
#
# def main():
#     RANDOM_NUMBERS = 7
#     random_list = []
#
#     for count in range(RANDOM_NUMBERS):
#         rand_num = random.randint(0, 9)
#         random_list.append(rand_num)
#
#     for num in random_list:
#         print(num)
#
#     print(random_list)
#
#
# if __name__ == '__main__':
#     main()

# ex.7.3
# def main():
#     month_list = ['January', 'February', 'March', 'April',
#                   'May', 'June', 'July', 'August', 'September',
#                   'October', 'November', 'December']
#     rain_list = []
#
#     for index in range(len(month_list)):
#         rain_quantity = float(
#                 input(f'Enter raninfall amount for {month_list[index]}: '))
#
#         rain_list.append(rain_quantity)
#     avr_rain = grand_total(rain_list) / len(month_list)
#     max_rain = max(rain_list)
#     min_rain = min(rain_list)
#
#     print(f'The Total rainfall is: {grand_total(rain_list)}')
#     print(f'The average rainfall is: {avr_rain}')
#     print(f'The maximum rainfall is: {max_rain}')
#     print(f'The minimum rainfall is: {min_rain}')
#
#
# def grand_total(list_a):
#     total = 0
#     for num in list_a:
#         total += num
#     return total
#
#
# if __name__ == '__main__':
#     main()

# ex.7.4
# def main():
#     NUMBERS_QTY = 20
#     numbers_list = []
#
#     for count in range(NUMBERS_QTY):
#         your_num = float(input(f'Enter the number №{count + 1}: '))
#         numbers_list.append(your_num)
#
#     min_num = min(numbers_list)
#     max_num = max(numbers_list)
#     total_num = grand_total(numbers_list)
#     average_num = grand_total(numbers_list) / NUMBERS_QTY
#
#     print(f'Minimum number is {min_num}')
#     print(f'Maximum number is {max_num}')
#     print(f'Total amount is {total_num}')
#     print(f'Average amount is {average_num}')
#
#
# def grand_total(my_list):
#     total = 0
#     for num in my_list:
#         total += num
#     return total
#
#
# if __name__ == '__main__':
#     main()

# ex 7.5
# def main():
#     my_file = open('charge_accounts.txt', 'r')
#     your_account = int(input("Enter 7 digits number of the account: "))
#
#     # create a list from data from the file
#     my_list = my_file.readlines()
#     print(my_list)
#     # close the file
#     my_file.close()
#
#     # remove '\n' from the list
#     for index in range(len(my_list)):
#         my_list[index] = my_list[index].rstrip('\n')
#     print(my_list)
#
#     # convert strings to numbers
#     for index in range(len(my_list)):
#         my_list[index] = int(my_list[index])
#     print(my_list)
#
#     # searching your number from the list
#     if your_account in my_list:
#         print('The number is available.')
#     else:
#         print('The number is not available.')
#
#
# if __name__ == '__main__':
#     main()

# ex 7.6
# import random
#
#
# def main():
#     LIST_NUMBERS = 30
#     n = int(input("Enter any number: "))
#
#     # print new list
#     for num in my_function(random_list(LIST_NUMBERS), n):
#         print(num)
#
#
# # create a list with random elements
# def random_list(numbers_a):
#     list3 = []
#     for index in range(numbers_a):
#         list3.append(random.randint(1, 500))
#     print(list3)
#     return list3
#
#
# # list1 = [1, 3, 5, 6, 3, 33, 56, 40, 55, 768, 34, 124]
#
# # create a list with elements > n
# def my_function(my_list, n):
#     list2 = [item for item in my_list if item > n]
#     return list2
#
#
# if __name__ == '__main__':
#     main()

# ex 7.7
# def main():
#     # create tuple
#     right_answers_list = ('A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B',
#                           'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A')
#     # create a file
#     # student_solution_f(QUESTIONS)
#     # print(right_answers_list)
#
#     student_answers_list = solution_f()
#     # print(student_answers_list)
#     student_check_list = final_list_f(right_answers_list, student_answers_list)
#     # print(student_check_list)
#     right_answers = right_answers_f(student_check_list)
#     print(f'Right answers: {right_answers}')
#     wrong_answers = len(student_check_list) - right_answers
#     print(f'Wrong answers: {wrong_answers}')
#
#     for index in range(len(student_check_list)):
#         if student_check_list[index] != 0:
#             True
#         else:
#             print(f'Question № {index + 1} - wrong answer.')
#
#
# def right_answers_f(check_list):
#     total = 0
#     for num in check_list:
#         total += num
#     return total
#
#
# # function that creates check list
# def final_list_f(right_answers_list, student_answers_list):
#     # check the number of element in your lists
#     if len(right_answers_list) == len(student_answers_list):
#         True
#     else:
#         print('Check the number of elements in your lists!')
#
#     final_list = []
#     for index in range(len(right_answers_list)):
#         if right_answers_list[index] == student_answers_list[index]:
#             final_list.append(1)
#         else:
#             final_list.append(0)
#     return final_list
#
#
# # Function that opens file and download the list
# def solution_f():
#     student_file = open('student_solution.txt', 'r')
#     student_answers = []
#     # remove '\n' from the list
#     for answer in student_file:
#         answer = answer[:-1]
#         student_answers.append(answer)
#     student_file.close()
#     print(student_answers)
#     return student_answers
#
#     # # opent student_solution.txt with the list
#     # student_file = open('student_solution.txt', 'r')
#     # student_list = student_file.readlines()
#     # student_file.close()
#
#     # # remove '\n' from the list
#     # for index in range(len(student_list)):
#     #     student_list[index] = student_list[index].rstrip('\n')
#     # return student_list
#
#
# # Function that makes file with student's answers
# def student_solution_f(QUESTIONS):
#     # number of question in the test
#     QUESTIONS = 20
#
#     student_solution_file = open('student_solution.txt', 'w')
#     student_solution_list = []
#     for index in range(QUESTIONS):
#         student_solution = str(input(f'Enter student solution '
#                                      f'for the question number {index + 1}: '))
#         student_solution_list.append(student_solution)
#     for value in student_solution_list:
#         student_solution_file.write(value + '\n')
#     student_solution_file.close()
#
#
# if __name__ == '__main__':
#     main()

cities = open('cities.txt', 'r')
for value in cities:
    print(value[2])
