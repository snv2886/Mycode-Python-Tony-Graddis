# # []
# print("I will show numbers from 1 - 5.")
# for num in [1,2,3,4,5]:
#    print(num)
#
# #range
# print("range")
# for num1 in range(5):
#    print(num1)
#
# print(" ")
# for x in range(5):
#     print("Hello World!")
# #range with two arguments
# print(" ")
# for x in range(1,5):
#     print(x)
# #range with three arguments
# print(" ")
# for x in range(1,10,2):
#     print(x)

# target variable in loop
# print("Number\tSquare")
# print('---------------')
# for number in range(1,11):
#     square = number**2 #target variable
#     print(f'{number}\t{square}')

# #KPH in MPH
# print('KPH\tMPH')
# print('---------------')
# START_SPEED = 60
# END_SPEED = 131
# INCREMENT = 10
# CONVERSION_FACTOR = 0.6214
# for kph in range(START_SPEED,END_SPEED,INCREMENT):
#     mph = kph * CONVERSION_FACTOR
#     print(f'{kph}\t{mph:.2f}')

# KPH in MPH + input
# end = int(input('Enter the final number in range: '))

# print('Number\tSquare')
# print('---------------')

# for number in range(1, end + 1):
#     square = number**2
#     print(f'{number}\t{square}')

# # Get number of students
# num_students = int(input('How many students do you have?: '))
# # Get number of test score
# num_test_score = int(input('How many scores per student?: '))
# # Determine the average score for each student
# for student in range(num_students):
#     # Initialised score storage
#     total = 0.0
#     # Get student number
#     print('Student number', student + 1)
#     print('----------------')
#     # Get scores for laboratory works
#     for test_num in range(num_test_score):
#         print(f'The number of laboratory work {test_num + 1}', end='')
#         score = float(input(': '))
#         # Add score to storage
#         total += score
#     # calculate the average score of this student
#     average = total / num_test_score
#     print(f'Average score of student number {student + 1}'
#           f' is {average:.1f}')
#     print()

# for row in range(8):
#     for col in range(6):
#         print('*', end='')
#     print()

# ROW_RATE = 8
# for r in range(ROW_RATE):  # var 'r' has following values: (0,1,2,3,4,5,6,7)
#     for c in range(r):
#         print(' ', end='')
#     print('#')

# import turtle
# # Именованные константы.
# # Количество рисуемых кругов.
# NUM_CIRCLES = 36
# # Радиус каждого круга.
# RADIUS = 100
# # Угол поворота.
# ANGLE = 10
# # Скорость анимации.

# ANIМATION_SPEED = 1

# # Задать скорость анимации.
# turtle.speed(ANIМATION_SPEED)

# # Нарисовать 36 кругов, наклоняя черепаху на
# # 10 градусов после того, как каждьм круг бьиr нарисован.
# for х in range(NUM_CIRCLES):
#     turtle.circle(RADIUS)
#     turtle.left(ANGLE)
# turtle.done()

# for row in range(8):
#     print(row)
# print()
# print(row)

# x = 1
# while x > 0:
#     y = int(input("Enter any number: "))

# product = 0

# while product < 100:
#     number1 = int(input("Enter a number: "))
#     product = number1 * 10
#     print("One more time")
# print("Over")

# another = 'y'
# while another == 'y':
#     number1 = int(input("Enter first number: "))
#     number2 = int(input("Enter second number: "))
#     sum = number1 + number2
#     print(f'The sum is:{sum}')
#     another = input("Do you want to repeat this operation?"
#                     "(Enter 'y'/'n'): ").lower()
# print("Over")

# for number in range(0, 1001, 10):
#     print(number)
# MAX = 5
# total = 0

# for counter in range(MAX):  # counter
#     number = int(input("Enter a number: "))
#     total = number + total
# print(f'Your total amount is: {total}')


# # Chapter-4 - ex.(4)
# n = 0
# total = 0
# for number in range(30, 0, -1): # from 30 to 1
#     n = n + 1
#     print(n)
#     division = n / number
#     print(division)
#     total = total + division
#     print(f'{total:.5f}')
# print(f'The sum is: {total:.5f}')


#  Chapter-4 ex.(7)
# for s1 in range(10):
#     for s2 in range(15):
#         print('#', end='')
#     print()


# Chapter-4 ex.(8)
# number = int(input("Enter any positive non-zero number: "))
# while number <= 0:
#     print("Enter only positive numbers")
#     number = int(input("Try one more time: "))
# print(f'This is your number: {number}')


# Chapter-4 ex.(9)
# number = int(input("Enter a number between 1 and 100: "))
# while number < 1 or number > 100:
#     print("Enter only numbers between 1 and 100.")
#     number = int(input("Try one more time: "))
# print(f'This is your number: {number}')


# Chapter-4 ex.(2.1)
# DAYS = 5
# cumulative_total = 0
#
# for counter in range(DAYS):
#     error = int(input(f'Enter the number of errors on day-{counter + 1}: '))
#     cumulative_total = cumulative_total + error
# print(f'The total amount of errors is: {cumulative_total}')


# Chapter-4 ex.(2.2)
# cal_per_min = 4.2
#
# for minutes in range(10, 31, 5):
#     total_cal = cal_per_min * minutes
#     print(f'Calories burnt after {minutes} minutes are: {total_cal}')


# Chapter-4 ex.(2.3)
# budget_items = 5
# total = 0
# one_month_amount = float(input("Enter an amount of money for one month: "))
#
# for counter in range(budget_items):
#     item = str(input("Enter the budget item: "))
#     item_amount = float(input("Enter the sum of this budget item: "))
#     total = total + item_amount
#     print(f'{item} = {item_amount}')
#
# balance = one_month_amount - total
# if balance < 0:
#     print(f'You have overspending: {balance:.2f}')
# else:
#     print(f'You have savings: {balance:.2f}')


# Chapter-4 ex.(2.4)
# speed = int(input("Enter the speed of vehicle in km/h: "))
# time = int(input("Enter the quantity of hours: "))
# print('Hours\tDistance')
# print('---------------')
#
# for counter in range(time):
#     distance = (counter + 1) * speed
#     print(f'{counter + 1} \t {distance}')


# Chapter-4 ex.(2.5)
# MONTHS = 12
# total = 0
# years = int(input("Enter the number of years: "))
# total_months = MONTHS * years
#
# for counter in range(years):
#     for month in range(MONTHS):
#         rain = int(input(f'Enter a milimetrs of precipitation: '
#                          f'year {counter + 1}, month {month + 1}: '))
#         total = total + rain
# mp_per_month = total / total_months
# print(f'months = {total_months},total milimetrs of precipitations = {total},'
#       f' everage mp per month = {mp_per_month:.2f}.')


# Chapter-4 ex.(2.6)
# print('Celsius\tFahrenheit')
# print('-------------------')
# for celsius in range(0, 20, 1):
#     fahrenheit = (9 / 5) * celsius + 32
#     print(f'{celsius}\t{fahrenheit:.2f}')


# Chapter-4 ex.(2.7)
# days = int(input("Enter the amount of days: "))
# wage = 1
# print('Day\tWage(penny)')
# print('-------------------')
#
# for counter in range(days):
#     if counter == 0:
#         wage = wage * 1
#     else:
#         wage = wage * 2
#     print(f'{counter + 1}\t{wage}')
# print(f'total wage is: {wage / 100:,}(rub)')


# Chapter-4 ex.(2.8)
# total = 0
# positive_number = int(input("Enter positive number: "))
# while positive_number > 0:
#     total = total + positive_number
#     positive_number = int(input("Enter positive number: "))
# print(f'Total amount is: {total}')


# Chapter-4 ex.(2.9)
# ocean_up = 1.6
# YEARS = 25
# total = 0
# print('Year\tOcean_level')
# print('-------------------')
#
# for counter in range(YEARS):
#     total = total + ocean_up
#     print(f'{counter + 1}\t{total:.2f}(mm)')


# Chapter-4 ex.(2.10)
# education_price = 145000
# RATE = 0.03
# YEARS = 5
# print('Years\tPrice')
# print('--------------')
#
# for counter in range(YEARS):
#     education_price = education_price + (education_price * RATE)
#     print(f'{counter + 1}\t{education_price:,.2f}$')


# Chapter-4 ex.(2.11)
# weight_red_pm = 1.5
# period = 6
# your_weight = float(input("Enter your weight in kg: "))
# print()
# print('Months\tWeight')
# print('---------------')
#
# for counter in range(period):
#     your_weight = your_weight - weight_red_pm
#     print(f'{counter + 1}\t{your_weight}(kg)')


# Chapter-4 ex.(2.12)
# factorial = 1
# positive_number = int(input("Enter positiv natural number: "))
# print()
# print('number\tfactorial')
# print('------------------')
#
# while positive_number <= 0:
#     positive_number = int(input("You entered negative number!"
#                                 "Enter positive: "))
# for counter in range(positive_number):
#     factorial = factorial * (counter + 1)
# print(f'{positive_number}\t{factorial}')


# Chapter-4 ex.(2.13)
# start_quantity = int(input("Enter start quantity of population"
#                            " of organisms: "))
# avr_daily_inc = float(input("Enter average daily increase of population"
#                             " of organisms (%): "))
# days_quantity = int(input("Enter quantity of days for reproduction: "))
# print('Day\tPopulation')
# print('----------------')
#
# for counter in range(days_quantity):
#     if counter == 0:
#         start_quantity = start_quantity
#     else:
#         start_quantity = start_quantity+(start_quantity * avr_daily_inc/100)
#     print(f'{counter + 1}\t{start_quantity:.5f}')


# Chapter-4 ex.(2.14)
# for r in range(7, 0, -1):
#     for c in range(r):
#         print('*', end='')
#     print()


# Chapter-4 ex.(2.15)
# NUM_STEP = 6
# for counter in range(NUM_STEP):
#     print('#', end='')
#     for c in range(counter):
#         print(' ', end='')
#     print('#')


# Local var 
# def main():
#     get_name()
#     print(f'Hello {name}.')  # Error - local var from different function
#
#
# # define function get_name.
# def get_name():
#     name = input('Enter your name: ')
#
#
# # call main() function
# main()


# def main():
#     texas()
#     california()
#
#
# def texas():
#     birds = 500
#     print(f'Texas has {birds} birds.')
#
#
# def california():
#     birds = 1000
#     print(f'California has {birds} birds.')
#
#
# main()

# def main():
#     intro()
#     cups_needed = int(input('Enter the number of cups: '))
#     cups_to_ounces(cups_needed)
#
#
# def intro():
#     print('This programm convert measurements')
#     print('from caps to liquid ounces. Here is the')
#     print(' formula for reference  : ')
#     print('1 cap = 8 liquid ounces.')
#     print()
#
#
# def cups_to_ounces(cups):
#     ounces = cups * 8
#     print(f'This number converts to {ounces} ounces.')
#
#
# main()

# def main():
#     print('Sum of the numbers equals')
#     show_sum(12, 44)
#
#
# def show_sum(num1, num2):
#     result = num1 + num2
#     print(result)
#
#
# main()

# def main():
#     value = 99
#     print(f'The value is equal {value}.')
#     change_me(value)
#     print(f'After the return to function "main" the value is equal {value}.')
#
#
# def change_me(arg):
#     print('I am changing the value')
#     arg = 0
#     print(f'Now the value is equal {arg}.')
#
#
# main()


# def main():
#     # Показать сумму простого процентного дохода, используя
#     # 0.01 как процентной ставки за период, 10 как количество
#     # периодов и $10 000 как основную сумму на счете.
#     show_interest(rate=0.01, periods=10, principal=10000.0)
#
# # Функция show_interest показывает сумму простого процентного
# # дохода для заданной основной суммы, процентной ставки
# # за период и количество периодов.
#
#
# def show_interest(principal, rate, periods):
#     interest = principal * rate * periods
#     print(f'Простой процентный доход составит ${interest:,.2f}')
#
#
# main()

# CONTRIBUTION_RATE = 0.05
#
#
# def main():
#     gross_pay = float(input("Enter gross payment: "))
#     bonus = float(input("Enter bounus amount: "))
#     show_pay_contrib(gross_pay)
#     show_bonus_contrib(bonus)
#
#
# def show_pay_contrib(gross):
#     contrib = gross * CONTRIBUTION_RATE
#     print(f'Contribution based on gross payment: ${contrib}')
#
#
# def show_bonus_contrib(bonus):
#     contrib = bonus * CONTRIBUTION_RATE
#     print(f'Contribution based on bonus: ${contrib}')
#
#
# main()

# import random
#
#
# def main():
#     number = random.randint(1, 10)
#     print(f'The number is equal: {number}')
#
#
# main()

# import random
#
#
# def main():
#     for count in range(5):
#         number = random.randint(1, 100)
#         print(number)
#
#
# main()

# import random
#
#
# def main():
#     for count in range(5):
#         print(f'the number is equal: {random.randint(1, 100)}')
#
#
# main()

# import random
# print(f'{random.randint(1, 1000):^10d}.')

# import random
#
# # константы для макс и мин случайных чисел
# MIN = 1
# MAX = 6


# def main():
#     # Создаем переменную, которая управляет циклом
#     again = 'y'
#
#     # Имитировать бросание кубика
#     while again == 'y' or again == 'Y':
#         print('Бросаем кубики...')
#         print('Значение граней:')
#         print(random.randint(MIN, MAX))
#         print(random.randint(MIN, MAX))
#
#         # Сделать еще один бросок кубика?
#         again = input('Roll the dices again? (y/n): ')
#
#
# main()
# import random
#
# HEAD = 1
# TAILS = 2
# TOSSES = 10  # number of tosses
#
#
# def main():
#     for toss in range(TOSSES):
#         if random.randint(HEAD, TAILS) == HEAD:
#             print('HEAD')
#         else:
#             print('TAILS')
#
#
# main()
# import random
#
# random.seed(10)
# print(random.random())

# def main():
#     first_age = int(input('Enter your age: '))
#     second_age = int(input('Enter the age of your best friend: '))
#
# # Вызывается функция sum. Ей передаются два значения в качестве аргументов
# # Значение, которое возвращается из функции sum, присваивается переменной total
#     total = sum(first_age, second_age)
#     print(f'Total age is {total} years')
#
#
# def sum(num1, num2):
#     return num1 + num2
#
#
# main()

# DISCOUNT_PERCENTAGE = 0.02


# def main():
#     reg_price = get_regular_price()
#     sales_price = reg_price - discount(reg_price)
#     print(f'Your sales price is: ${sales_price:.2f}')


# def get_regular_price():
#     price = float(input('Enter regular price: '))
#     return price


# def discount(price):
#     return price * DISCOUNT_PERCENTAGE


# main()

# def main():
#     sales = get_sales()
#     advanced_pay = get_advanced_pay()
#     comm_rate = determine_comm_rate(sales)
#     pay = sales * comm_rate - advanced_pay
#     print(f'Your overall payment is: {pay:,.2f}.')
#     if pay < 0:
#         print('You have to pay the difference to the company')
#
#
# def get_sales():
#     monthly_sales = float(input('Enter your monthly sales: '))
#     return monthly_sales
#
#
# def get_advanced_pay():
#     print('Enter the amount of advanced payment')
#     print('or enter 0 if there is no advanced payment')
#     advanced = float(input('Advanced payment: '))
#     return advanced
#
#
# def determine_comm_rate(sales):
#     if sales < 10000.0:
#         rate = 0.10
#     elif sales >= 10000.0 and sales <= 14999.9:
#         rate = 0.12
#     elif sales >= 15000.0 and sales <= 17999.9:
#         rate = 0.14
#     elif sales >= 18000.0 and sales <= 21999.9:
#         rate = 0.16
#     else:
#         rate = 0.18
#     return rate
#
#
# main()

# def is_even(number):
#     if (number % 2) == 0:
#         status = True
#     else:
#         status = False
#     return status
#
#
# number = int(input('Enter the number: '))
# if is_even(number):
#     print('This number is even.')
# else:
#     print('This number is odd.')

# def main():
#
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#
#     quotient = divide(num1, num2)
#     if quotient is None:
#         print("You can't divide by zero")
#     else:
#         print(f'{num1} divided by {num2} iquals {quotient}.')
#
#
# def divide(num1, num2):
#     if num2 == 0:
#         result = None
#     else:
#         result = num1 / num2
#     return result
#
#
# main()

# Chapter-5 exc.1
# number = int(input("Enter any integer: "))


# def times_ten(number):
#     print(f'{number * 10}')


# times_ten(number)


# Chapter-5 exc.2
# quantity = 20


# def show_value(number):
#     print(number)


# show_value(quantity)


# Chapter-5 exc.3
# def my_function(a, b, c):
#     print(b, a, c)
#
#
# my_function(5, 2, 34)


# Chapter-5 exc.4
# def main():
#     x = 1
#     y = 3.4
#     print(x, y)
#     change_us(x, y)
#     print(x, y)
#
#
# def change_us(a, b):
#     a = 0
#     b = 0
#     print(a, b)
#
#
# main()


# Chapter-5 exc.5
# def my_function(a, b, c):
#     d = (a + c) / b
#     print(d)
#
#
# my_function(b=4, a=8, c=8)


# Chapter-5 exc.6
# import random
#
# rand = random.randint(1, 100)
# print(rand)


# Chapter-5 exc.6
# def half(number):
#     return number / 2
#
#
# number = float(input("Enter any number: "))
# result = half(number)
# print(result)


# Chapter-5 exc.8
# def main():
#     number = 4
#     result = cube(number)
#     print(result)
#
#
# def cube(num):  # Определение функции
#     return num * num * num
#
#
# main()


# Chapter-5 exc.9
# def main():
#     number = int(input("Enter any number: "))
#     print(times_ten(number))
#
#
# def times_ten(x):
#     return x * 10
#
#
# main()


# Chapter-5 exc.10
# def get_first_name():
#     name = input("Enter your name: ")
#     return name
#
#
# result = get_first_name()
# print(result)


# Chapter-5 exc.1
# def main():
#     kilometer = float(input("Enter the number of kilometers: "))
#     print(f'{kilometer} kilometers equals {km_to_miles(kilometer):.2f} miles')
#
#
# def km_to_miles(km):
#     return km * 0.6214
#
#
# main()


# Chapter-5 exc.2
# FED_TAX_RATE = 0.05
# REG_TAX_RATE = 0.025
#
#
# def main():
#     purchase = float(input("Enter the value of purchase: "))
#     fed_tax = federal_tax(purchase)
#     reg_tax = regional_tax(purchase)
#     print()
#     print(f'Overall purchase: {purchase}')
#     print(f'Federal tax: {fed_tax}')
#     print(f'Regional tax: {reg_tax}')
#     print(f'Total taxes: {fed_tax + reg_tax}')
#     print(f'Total purchase value: {purchase + fed_tax + reg_tax}')
#
#
# def federal_tax(value):
#     return value * FED_TAX_RATE
#
#
# def regional_tax(value):
#     return value * REG_TAX_RATE
#
#
# main()


# Chapter-5 exc.3
# MIN_INSUR_RATE = 0.8
#
#
# def main():
#     house_price = float(input("Enter the price of your house: "))
#     result = min_sum_insur(house_price)
#     print(f'Your minimal sum insured is: ${result:,.1f}')
#
#
# def min_sum_insur(price):
#     return price * MIN_INSUR_RATE
#
#
# main()


# Chapter-5 exs.4
# MONTHS = 12
#
#
# def main():
#     month_expenses = month_exps()
#     print()
#     print(f'Total monthly car expenses are: ${month_expenses:,.2f}')
#     print(f'Total annual car expenses are:'
#           f' ${annual_exps(month_expenses):,.2f}')
#
#
# def month_exps():
#     loan_pay = float(input("Enter your monthly loan payment: "))
#     insurance = float(input("Enter your monthly insurance payment: "))
#     fuel = float(input("Enter your monthly fuel expenses: "))
#     engine_oil = float(input("Enter your monthly engine oil expenses: "))
#     tires = float(input("Enter your monthly tires expenses: "))
#     maintenance = float(input("Enter your monthly maintenance expenses: "))
#     result = loan_pay + insurance + fuel + engine_oil + tires + maintenance
#     return result
#
#
# def annual_exps(value):
#     return value * MONTHS
#
#
# main()


# Chapter-5 ex.5
# ESTIMATED_RE_RATE = 0.6
# PROPERTY_TAX = 0.72 / 100
#
#
# def main():
#     actual_real_estate = float(input('Enter the actual value of '
#                                      'your real estate: '))
#     assesed_value = actual_real_estate * ESTIMATED_RE_RATE
#     print(f"Your assesed value is ${assesed_value:,.0f}.\n"
#           f"Your property tax is ${tax(actual_real_estate):,.0f}")
#
#
# def tax(value):
#     return value * PROPERTY_TAX
#
#
# main()


# Chapter-5 ex.6
# def main():
#
#     fat_grams = float(input("Enter your daily fat "
#                             "consumption: "))
#     carb_grams = float(input("Enter your daily carb "
#                              "consumption: "))
#     print()
#     print(f'You daily calories from fat: {fat_calories(fat_grams):.2f}')
#     print('Your daily calories from carbs : '
#           f'{carb_calories(carb_grams):.2f}')
# 
# 
# def fat_calories(value):
#     return value * 9
# 
# 
# def carb_calories(value):
#     return value * 4
# 
# 
# main()


# Chapter-5 ex.7
# A = 20
# B = 15
# C = 10
#
#
# def main():
#     class_A = int(input("Enter the number of seat A sold: "))
#     class_B = int(input("Enter the number of seat B sold: "))
#     class_C = int(input("Enter the number of seat C sold: "))
#     seat_classes(class_A, class_B, class_C)
#
#
# def seat_classes(a, b, c):
#     profit = a * A + b * B + c * C
#     print(f'The overall profit is: ${profit}')
#
#
# main()


# Chapter-5 ex.8

# LITERS_IN_CAN = 5
# METERS_PER_CAN = 10
# MIN_PER_METER = (8 * 60) / 10
# WORK_PRICE_MIN = 2000 / 60
#
#
# def main():
#     wall_square = int(input("Enter the wall square in m^2: "))
#     paint_price = float(input("Enter your 5 liter paint price: "))
#     paint_quantity = quantity_of_paint(wall_square)
#     time_spent = time_needed(wall_square)
#     paint_cost = cost_of_paint(paint_price, wall_square)
#     cost_of_work = labor_cost(wall_square)
#     total_cost = cost_of_work + paint_cost
#     print(f'Amount of paint: {paint_quantity} liters')
#     print(f'Hours spent: {time_spent} hours')
#     print(f'Cost of paint: ${paint_cost:,.0f}')
#     print(f'Cost of work: ${cost_of_work:,.0f}')
#     print(f'Total cost: ${total_cost:,.0f}')
#
#
# def time_needed(value):
#     return value * MIN_PER_METER / 60
#
#
# def quantity_of_paint(value):
#     return value * (LITERS_IN_CAN / METERS_PER_CAN)
#
#
# def cost_of_paint(value1, value2):
#     value = value1 / LITERS_IN_CAN * value2
#     return value
#
#
# def labor_cost(value):
#     time_spent = value * MIN_PER_METER
#     work_cost = time_spent * WORK_PRICE_MIN
#     return work_cost
#
#
# main()


# Chapter-5 ex.9
# FEDERAL_TAX_RATE = 0.05
# COUNCIL_TAX_RATE = 0.025
#
#
# def main():
#     sales_volume = float(input("Enter the sales volume for current month: "))
#     fed_tax = federal_tax_f(sales_volume)
#     council_tax = council_tax_f(sales_volume)
#     total_taxes = fed_tax + council_tax
#     print(f'Federal tax amount is: ${fed_tax:,.0f}')
#     print(f'Council tax amount is: ${council_tax:,.0f}')
#     print(f'Total taxes amount is: ${total_taxes:,.0f}')
#
#
# def council_tax_f(value):
#     return value * COUNCIL_TAX_RATE
#
#
# def federal_tax_f(value):
#     return value * FEDERAL_TAX_RATE
#
#
# main()


# Chapter-5 ex.10
# INCHES_IN_FEET = 12
#
#
# def main():
#     feets = int(input("Enter amount of feets: "))
#     print(f'In {feets} feets {feet_to_inches(feets)} inches')
#
#
# def feet_to_inches(value):
#     return value * INCHES_IN_FEET
#
#
# main()


# Chapter-5 ex.11
# import random
#
# random1 = random.randint(0, 1001)
# random2 = random.randint(0, 1001)
# random_sum = random1 + random2
# print(f'{random1:6d}')
# print(f'+ {random2:4d}')
# answer = int(input("Enter your answer: "))
#
# if answer == random_sum:
#     print('Rigth answer!')
# else:
#     print('Wrong answer!')


# Chapter-5 ex.12
# def main():
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#     max(num1, num2)
#
#
# def max(number1, number2):
#     if number1 > number2:
#         print(number1)
#     elif number1 < number2:
#         print(number2)
#     else:
#         print('numbers are equal.')
#
#
# main()


# Chapter-5 ex.13
# import random
# G = 9.8  # время падения тела в секундах
#
#
# def main():
#     status = 'y'
#     while status == 'y' or status == 'yes':
#         time = random.randint(1, 10)
#         print(f'time = {time} seconds')
#         falling_distance_f = falling_distance(time)
#         print(f'Your falling distance is: {falling_distance_f:.0f} meters')
#         status = input("Do you want to continue? (y/n) ")
#     print('Stop')
#
#
# def falling_distance(time):
#     x = 1 / 2 * G * time ** 2
#     return x
#
#
# main()


# Chapter-5 ex.14
# def main():
#     mass = float(input("Enter a mass of body: "))
#     speed = float(input("Enter a speed of body: "))
#     print(f'The kinetic energy is: {kinetic_energy(mass, speed):,.0f}J')
#
#
# def kinetic_energy(mass, velocity):
#     x = 1 / 2 * mass * velocity ** 2
#     return x
#
#
# main()


# Chapter-5 ex.15

# def main():
#     total = 0
#     for count in range(0, 5):
#         score_n = int(input(f'Enter your score number {count + 1}: '))
#         total = total + score_n
#         average = calc_average(total, count)
#         print('Scr number |\tGrade |\tAverage')
#         print('------------------------------')
#         print(f'Number {count + 1}|\t{determin_grade(score_n)}|\t{average}')
#         print()
#
#
# def calc_average(value, number):
#     average = value / (number + 1)
#     return average
#
#
# def determin_grade(value):
#     if value >= 90:
#         score = "Grade A"
#     elif value >= 80 and value <= 89:
#         score = "Grade B"
#     elif value >= 70 and value <= 79:
#         score = "Grade C"
#     elif value >= 60 and value <= 69:
#         score = "Grade D"
#     elif value < 60:
#         score = "Grade F"
#     else:
#         score = "Wrond value!"
#     return score
#
#
# main()


# Chapter-5 ex.16
# import random
#
#
# def main():
#     even = 0
#     odd = 0
#
#     for count in range(100):
#         number = random.randrange(1000)
#         print(number)
#         if number % 2 == 0:
#             even = even + 1
#         else:
#             odd = odd + 1
#     print(f'Even numbers = {even}\n Odd numbers = {odd}')
#
#
# main()


# Chapter-5 ex.17
# def main():
#     number = int(input("Enter any integer number: "))
#     prime_number = is_prime(number)
#     if prime_number > 2:
#         print("The number is not prime.")
#     else:
#         print("The number is prime.")
#
#
# def is_prime(number):
#     x = 0
#     for count in range(number):
#         if number % (count + 1) == 0:
#             x = x + 1
#         else:
#             x = x
#     return x
#
#
# main()


# Chapter-5 ex.18

# def main():
#     for count in range(1, 101):
#         prime_number = is_prime(count)
#         if prime_number <= 2:
#             print(count)
#         else:
#             False
#
#
# def is_prime(number):
#     x = 0
#     for count in range(number):
#         if number % (count + 1) == 0:
#             x = x + 1
#         else:
#             False
#     return x
#
#
# main()


# Chapter-5 ex.19
# def main():
#     present_sum = float(input("Enter present sum on your account: "))
#     interest_rate = float(input("Enter monthly interest rate(%): ")) / 100
#     months = int(input("Enter the amount of months: "))
#     print('Your future sum will be: '
#           f'${future_sum(present_sum, interest_rate, months):,.0f}')
#
#
# def future_sum(sum, rate, period):
#     future = sum * (1 + rate) ** period
#     return future
#
#
# main()


# Chapter-5 ex.20
# import random
#
#
# def main():
#     ask = 'y'
#     count = 1
#     y = int(input("Guess a number from 1 to 10: "))
#     while ask == 'y':
#         x = random.randint(1, 10)
#         if y > x:
#             y = int(input("Too big number! Try one more time: "))
#             count = count + 1
#         elif y < x:
#             y = int(input("Too small number! Try one more time: "))
#             count = count + 1
#         else:
#             print("Well done!")
#             print(f'You have guessed {count} times')
#             ask = input("Do you want to continue (y/n): ")
#             count = 1
#             if ask == 'y':
#                 y = int(input("Guess a number from 1 to 10: "))
#             else:
#                 False
#
#
# main()


# Chapter-5 ex.21
# import random
#
#
# def main():
#     computer()
#
#
# def computer():
#     x = random.randint(1, 3)
#     y = input("Enter 'rock' or 'scissors' or 'paper': ")
#     if x == 1:
#         comp = 'rock'
#         print(f'Computer selected: {comp}')
#         rock_scissors(comp, y)
#     elif x == 2:
#         comp = 'scissors'
#         print(f'Computer selected: {comp}')
#         rock_scissors(comp, y)
#     else:
#         comp = 'paper'
#         print(f'Computer selected: {comp}')
#         rock_scissors(comp, y)
#
#
# def rock_scissors(x, y):
#     if x == 'rock' and y == 'scissors':
#         print(f'Computer wins! <{x}> beats <{y}>')
#     elif x == 'scissors' and y == 'rock':
#         print(f'Player wins! <{y}> beats <{x}>')
#     elif x == 'rock' and y == 'paper':
#         print(f'Player wins! <{y}> beats <{x}>')
#     elif x == 'paper' and y == 'rock':
#         print(f'Computer wins! <{x}> beats <{y}>')
#     elif x == 'paper' and y == 'scissors':
#         print(f'Player wins! <{y}> beats <{x}>')
#     elif x == 'scissors' and y == 'paper':
#         print(f'Computer wins! <{x}> beats <{y}>')
#     elif x == y:
#         print('Draw! One more round')
#         computer()
#
#
# main()

# def main():
#     outfile = open('philosophers.txt', 'w')
#
#     outfile.write('Jhon Locke\n')
#     outfile.write('David Hume\n')
#     outfile.write('Admund Berk\n')
#
#     outfile.close()
#
#
# if __name__ == '__main__':
#     main()
# def main():
#     infile = open('philosophers.txt', 'r')
#     file_contents = infile.read()
#     infile.close()
#     print(file_contents)
#
#
# if __name__ == '__main__':
#     main()


# def main():
#     infile = open('philosophers.txt', 'r')
#     line1 = infile.readline()
#     line2 = infile.readline()
#     line3 = infile.readline()
#     infile.close()
#
#     print(line1)
#     print(line2)
#     print(line3)
#
#
# if __name__ == '__main__':
#     main()


# def main():
#     print('Enter the names of three friends.')
#     name1 = input("Friend # 1: ")
#     name2 = input("Friend # 2: ")
#     name3 = input("Friend # 3: ")
#
#     my_friends = open('friends.txt', 'w')
#     my_friends.write(name1 + '\n')
#     my_friends.write(name2 + '\n')
#     my_friends.write(name3 + '\n')
#     my_friends.close()
#     print('Names have been writen to friends.txt')
#
#
# if __name__ == '__main__':
#     main()

# def main():
#     myfile = open('friends.txt', 'r')
#     line1 = myfile.readline()
#     line2 = myfile.readline()
#     line3 = myfile.readline()
#     line1 = line1.rstrip('\n')
#     line2 = line2.rstrip('\n')
#     line3 = line3.rstrip('\n')
#     myfile.close()
#     print(line1)
#     print(line2)
#     print(line3)
#
#
# if __name__ == '__main__':
#     main()

# def main():
#     myfile = open('friends.txt', 'a')
#     myfile.write('Mike\n')
#     myfile.write('Kriss\n')
#     myfile.write('Sussi\n')
#     myfile.close()
#
#
# if __name__ == '__main__':
#     main()

# def main():
#     outfile = open('numbers.txt', 'w')
#     num1 = int(input('Enter number: '))
#     num2 = int(input('Enter one more number: '))
#     num3 = int(input('Enter one more number: '))
#     outfile.write(str(num1) + '\n')
#     outfile.write(str(num2) + '\n')
#     outfile.write(str(num3) + '\n')
#     outfile.close()
#
#
# if __name__ == '__main__':
#     main()

# def main():
#     infile = open('numbers.txt', 'r')
#     num1 = int(infile.readline())
#     num2 = int(infile.readline())
#     num3 = int(infile.readline())
#     infile.close()
#
#     total = num1 + num2 + num3
#
#     print(f'Numbers: {num1}, {num2}, {num3}')
#     print(f'Total sum: {total}')
#
#
# if __name__ == '__main__':
#     main()

# def main():
#     num_days = int(input('How many days ' +
#                          'do you have sales: '))
#     sales_file = open('sales.txt', 'w')
#     # Get sum of sales for each day
#     for count in range(1, num_days + 1):
#         # Get sales for a day
#         sales = float(input(f'Enter sales for day {count}: '))
#         # Write this inf to the file (as a str)
#         sales_file.write(f'{sales}\n')
#         print('Data has been writen to sales.txt')
#     sales_file.close()
#
#
# if __name__ == '__main__':
#     main()
