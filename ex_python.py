# def main():
#     # Open sales.txt for reading
#     sales_file = open('sales.txt', 'r')
#     # Read first line but don't convert to number. At first we
#     # need to check blank lines
#     line = sales_file.readline()
#     # Continue processing file untill we get blank line
#     while line != '':
#         # Convert number to float
#         amount = float(line)
#         print(f'{amount:.2f}')
#         # Read next line
#         line = sales_file.readline()
#     sales_file.close()
#
#
# if __name__ == '__main__':
#     main()

# def main():
#     sales_file = open('sales.txt', 'r')
#     for line in sales_file:
#         amount = float(line)
#         print(f'{amount:.2f}')
#     sales_file.close()
#
#
# if __name__ == '__main__':
#     main()

# def main():
#     num_videos = int(input("Enter the number of clips in the projects: "))
#     video_file = open('clips.txt', 'w')
#     for count in range(1, num_videos + 1):
#         print(count)
#         video_length = float(input(f'What is the length of {count} video: '))
#         video_file.write(str(f'{video_length}\n'))
#     video_file.close()
#
#
# if __name__ == '__main__':
#     main()

# def main():
#     video_file = open('clips.txt', 'r')
#     total = 0
#     count = 0
#     print('The length of all video clips:')
#     for line in video_file:
#         # преборазовать строку в число с плавающей точкой
#         run_time = float(line)
#         count += 1
#         # Показать длительность видеоклипа
#         print('Video clip №', count, ":", run_time, sep='')
#         # Прибавить длительность к total
#         total += run_time
#     video_file.close()
#     print(f'Total length is {total} seconds.')
#
#
# if __name__ == '__main__':
#     main()

# def main():
#     file1 = open('file1.txt', 'w')
#     for count in range(1, 11):
#         file1.write(f'{count}\n')
#     file1.close()
#
#
# if __name__ == '__main__':
#     main()
#
# def main():
#     ex_file = open('file1.txt', 'r')
#     line = ex_file.readline()
#     print(line.rstrip('\n'))
#     while line != '':
#         line = ex_file.readline()
#         line_n = line.rstrip('\n')
#         print(line_n)
#     ex_file.close()
#
#
# if __name__ == '__main__':
#     main()

# def main():
#     ex_file = open('file1.txt', 'r')
#     for line in ex_file:
#         print(int(line))
#     ex_file.close()
#
#
# if __name__ == '__main__':
#     main()

# def main():
#     num_emp = int(input('How many employee records ' +
#                         'do you want to create? '))
#     emp_file = open('employees.txt', 'w')
#     for count in range(1, num_emp + 1):
#         name = input('Name: ')
#         id_num = int(input('ID: '))
#         dept = input('Department: ')
#
#         emp_file.write(f'{name}\n')
#         emp_file.write(f'{id_num}\n')
#         emp_file.write(f'{dept}\n')
#         print()
#     emp_file.close()
#     print('Employee records have been written to employees.txt')
#
#
# if __name__ == '__main__':
#     main()

# def main():
#     emp_file = open('employees.txt', 'r')
#     name = emp_file.readline()
#     while name != '':
#         id_num = emp_file.readline()
#         dept = emp_file.readline()
#
#         name = name.rstrip('\n')
#         id_num = id_num.rstrip('\n')
#         dept = dept.rstrip('\n')
#
#         print(f'Name: {name}')
#         print(f'ID: {id_num}')
#         print(f'Department: {dept}')
#         print()
#
#         name = emp_file.readline()
#     emp_file.close()
#
#
# if __name__ == '__main__':
#     main()

# def main():
#     another = 'y'
#     # Создать переменную для управления циклом
#     coffee_file = open('coffee.txt', 'a')
#     while another == 'y' or another == 'Y':
#         descrp = input("Enter brand name: ")
#         qty = int(input("Quantity (in pounds): "))
#         coffee_file.write(f'{descrp}\n')
#         coffee_file.write(f'{qty}\n')
#         print('Do you want to add one more record?')
#         another = input('Y = yes, all other = no: ')
#     coffee_file.close()
#     print('Data is added to coffee.txt')
#
#
# if __name__ == '__main__':
#     main()

# import os
#
#
# def main():
#
#     found = False
#     search = input('Which brend do you want to delet? ')
#
#     coffee_file = open('coffee.txt', 'r')
#     temp_file = open('temp.txt', 'w')
#
#     descr = coffee_file.readline()
#
#     # Read the rest of the list
#     while descr != '':
#         qty = float(coffee_file.readline())
#         descr = descr.rstrip('\n')
#
#         if descr != search:
#             temp_file.write(f'{descr}\n')
#             temp_file.write(f'{qty}\n')
#         else:
#             found = True
#
#         descr = coffee_file.readline()
#
#     coffee_file.close()
#     temp_file.close()
#
#     os.remove('coffee.txt')
#     os.rename('temp.txt', 'coffee.txt')
#
#     # Show the message if search faild
#     if found:
#         print('file updated!')
#     else:
#         print("The value wasn't found")
#
#
# if __name__ == '__main__':
#     main()

# def main():
#     try:
#         hours = int(input("How many hours did you work? "))
#         pay_rate = float(input("Enter your pay rate per hour: "))
#         gross_pay = hours * pay_rate

#         print(f'Gross pay: ${gross_pay:,.2f}')

#     except ValueError:
#         print("Error: worked hours and pay rate per hour ")
#         print("have to be valid values")


# if __name__ == '__main__':
#     main()

# def main():
#     filename = input("Enter file name: ")
#     try:
#         infile = open(filename, 'r')

#         contents = infile.read()
#         print(contents)

#         infile.close()

#     except IOError:
#         print("An error occurred while trying to read the file.")


# if __name__ == '__main__':
#     main()

# def main():
#     total = 0

#     try:
#         infile = open('sales_data.txt', 'r')
#         # Read value from file
#         # and accumulate them in the variable
#         for line in infile:
#             amount = float(line)
#             total += amount

#         infile.close()
#         print(f'{total:,.2f}')

#     except:
#         print("Error occured.")


# if __name__ == '__main__':
#     main()


# def main():
#     try:
#         hours = int(input("How many hours did you work? "))
#         pay_rate = float(input("Enter your pay rate per hour: "))
#         gross_pay = hours * pay_rate

#         print(f'Gross pay: ${gross_pay:,.2f}')

#     except ValueError as err:
#         print(err)


# if __name__ == '__main__':
#     main()


# def main():
#     total = 0

#     try:
#         infile = open('sales_data.txt', 'r')
#         # Read value from file
#         # and accumulate them in the variable
#         for line in infile:
#             amount = float(line)
#             total += amount

#         infile.close()
#         print(f'{total:,.2f}')

#     # Определяем Exception как тип, для отлова всех исключений
#     except Exception as err:
#         print(err)


# if __name__ == '__main__':
#     main()

# def main():
#     name1 = input("Enter your name: ")
#     name2 = input("Enter your surename: ")
#     new_file = open('my_name.txt', 'w')
#     new_file.write(f'{name1}\n')
#     new_file.write(f'{name2}\n')
#     new_file.close()


# if __name__ == '__main__':
#     main()

# def main():
#     myfile = open('my_name.txt', 'r')
#     name = myfile.readline()
#     surename = myfile.readline()
#     name = name.rstrip('\n')
#     surename = surename.rstrip('\n')
#     print(name)
#     print(surename)
#     myfile.close()


# if __name__ == '__main__':
#     main()

# ex 6.3
# def main():
#     file = open('number_list.txt', 'w')
#     for number in range(1, 101):
#         file.write(f'{number}\n')
#     file.close()
#
#
# if __name__ == '__main__':
#     main()

# ex 6.4
# def main():
#     file1 = open('number_list.txt', 'r')
#     for line in file1:
#         data = line
#         data = data.rstrip('\n')
#         print(f'{data}')
#     file1.close()


# if __name__ == '__main__':
#     main()


# def main():
#     file1 = open('number_list.txt', 'r')
#     for line in file1:
#         line = line.rstrip('\n')
#         print(f'{line}')
#     file1.close()


# if __name__ == '__main__':
#     main()

# def main():
#     file1 = open('number_list.txt', 'r')
#     line = file1.readline()
#     while line != '':
#         line = line.rstrip('\n')
#         print(f'{line}')
#         line = file1.readline()
#     file1.close()


# if __name__ == '__main__':
#     main()


# ex 6.5
# def main():
#     total = 0
#     myfile = open('number_list.txt', 'r')
#     for line in myfile:
#         number = int(line)
#         total = total + number
#     print(f'The total value is: {total}')
#     myfile.close()


# if __name__ == '__main__':
#     main()


# ex 6.6
# def main():
#     myfile = open('number_list.txt', 'a')
#     new_value = input("Enter any value: ")
#     myfile.write(f'{new_value}\n')
#     myfile.close()
#
#     myfile = open('number_list.txt', 'r')
#     for line in myfile:
#         line = line.rstrip('\n')
#         print(line)
#
#     myfile.close()
#
#
# if __name__ == '__main__':
#     main()

# ex 6.7
# import os


# def main():
#     found = False
#     search = "Jhon Perz"
#     myfile = open('students.txt', 'r')
#     tempfile = open('studentstemp.txt', 'w')
#
#     name = myfile.readline()
#
#     while name != '':
#         score = int(myfile.readline())
#         name = name.rstrip()
#
#         if name != search:
#             tempfile.write(f'{name}\n')
#             tempfile.write(f'{score}\n')
#         else:
#             found = True
#
#         name = myfile.readline()
#
#     myfile.close()
#     tempfile.close()
#
#     os.remove('students.txt')
#     os.rename('studentstemp.txt', 'students.txt')
#
#     if found:
#         print("File updated")
#     else:
#         print("The name wasn't found")
#
#
# if __name__ == '__main__':
#     main()


# ex 6.8
# import os
#
#
# def main():
#     search = "Julia Millan"
#     newscore = 100
#     found = False
#     myfile = open('students.txt', 'r')
#     tempfile = open('tempstudents.txt', 'w')
#
#     name = myfile.readline()
#     while name != '':
#         name = name.rstrip('\n')
#         score = int(myfile.readline())
#         if name == search:
#             tempfile.write(f'{name}\n')
#             tempfile.write(f'{newscore}\n')
#             found = True
#         else:
#             tempfile.write(f'{name}\n')
#             tempfile.write(f'{score}\n')
#
#         name = myfile.readline()
#
#     myfile.close()
#     tempfile.close()
#
#     os.remove('students.txt')
#     os.rename('tempstudents.txt', 'students.txt')
#
#     if found:
#         print("File was updated")
#     else:
#         print("This name wasn't found")
#
#
# if __name__ == '__main__':
#     main()

# ex 6.2.1
# def main():
#     myfile = open('numbers.txt', 'r')
#     for line in myfile:
#         line = line.rstrip('\n')
#         print(line)
#     myfile.close()
#
#
# if __name__ == '__main__':
#     main()

# OR
# def main():
#     fileread = open('numbers.txt', 'r')
#     content = fileread.read()
#     print(content)
#     fileread.close()
#
#
# if __name__ == "__main__":
#     main()

# ex 6.2.1
# def main():
#     myfile = open('numbers.txt', 'r')
#     number = myfile.readline()
#     while number != '':
#         number = number.rstrip('\n')
#         print(number)
#         number = myfile.readline()
#
#
# if __name__ == '__main__':
#     main()


# ex 6.2.1
# def main():
#     COUNT = 5
#     total = 0
#
#     search = input("Enter file name: ")
#     myfile = open(search, 'r')
#     line = myfile.readline()
#     while line != '' and total < COUNT:
#         line = line.rstrip('\n')
#         print(f'{total + 1}:{line}')
#         line = myfile.readline()
#         total += 1
#
#     myfile.close()
#
#
# if __name__ == '__main__':
#     main()


# def main():
#     total = 0
#
#     search = input("Enter file name: ")
#     myfile = open(search, 'r')
#     line = myfile.readline()
#     while line != '':
#         line = line.rstrip('\n')
#         print(f'{total + 1}:{line}')
#         line = myfile.readline()
#         total += 1
#
#     myfile.close()
#
#
# if __name__ == '__main__':
#     main()

# def main():
#     count = 0
#     myfile = open('names.txt', 'r')
#     for line in myfile:
#         count += 1
#     print(f'Total number of names is: {count}')
#     myfile.close()
#
#
# if __name__ == '__main__':
#     main()

# def main():
#     total = 0
#     myfile = open('numbers.txt', 'r')
#     for line in myfile:
#         line = int(line)
#         total = total + line
#     print(f'{total}')
#     myfile.close()
#
#
# if __name__ == '__main__':
#     main()


# def main():
#     total = 0
#     count = 0
#     myfile = open('numbers.txt', 'r')
#     for line in myfile:
#         count += 1
#         line = int(line)
#         total = total + line
#         average = total / count
#     print(f'average: {average:.2f}')
#     myfile.close()
#
#
# if __name__ == '__main__':
#     main()

# import random
#
#
# def main():
#     quantity = int(input("Enter the number of random numbers: "))
#     random_file = open('random_numbers.txt', 'w')
#
#     for line in range(0, quantity):
#         random_number = random.randint(1, 500)
#         random_file.write(f'{random_number}\n')
#
#     random_file.close()
#
#
# if __name__ == '__main__':
#     main()

# def main():
#     total = 0
#     count = 0
#
#     myfile = open('random_numbers.txt', 'r')
#     for line in myfile:
#         line = line.rstrip('\n')
#         print(f'{line}')
#         number = int(line)
#         count += 1
#         total += number
#     myfile.close()
#     print('')
#
#     print(f'Sum: {total}')
#     print(f'Qantity of average numbers in files: {count}')
#
#
# if __name__ == '__main__':
#     main()


# def main():
#     total = 0
#     count = 0
#
#     try:
#         myfile = open('numbers.txt', 'r')
#         for line in myfile:
#             count += 1
#             line = int(line)
#             total = total + line
#             average = total / count
#         print(f'average: {average:.2f}')
#         myfile.close()
#
#     except IOError:
#         print("IOError! Such file doesn't exist!")
#     except ValueError:
#         print("ValueError!")
#
#
# if __name__ == '__main__':
#     main()

def main():
    golf_file = open('golf.txt', 'w')
    answer = 'y'

    while answer == 'y':
        name = input("Enter your name: ")
        score = int(input("Enter the score: "))
        golf_file.write(f'{name}\n')
        golf_file.write(f'{score}\n')
        answer = input("Do you want to enter new name y/n? ")

    golf_file.close()


if __name__ == '__main__':
    main()

    272
