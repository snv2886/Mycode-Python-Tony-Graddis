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

list1 = [1, 12, 2, 20, 3, 15, 4]
list2 = [item*2 for item in list1]
print(list1)
print(list2)
