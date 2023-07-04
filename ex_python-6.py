# 6.2.1
# def main():
#     fileread = open('numbers.txt', 'r')
#     content = fileread.read()
#     print(content)
#     fileread.close()
#
#
# if __name__ == "__main__":
#     main()


# 6.2.2
# def main():
#     total = 0
#     # COUNT = 5
#     filename = open(input('Enter file name: '), 'r')
#     content = filename.readline()
#     while content != '':  # and total < COUNT:
#         total += 1
#         content = content.rstrip('\n')
#         print(f'{total}: {content}')
#         content = filename.readline()
#     filename.close()
#
#
# if __name__ == "__main__":
#     main()

# 6.2.4
# def main():
#     total = 0
#     myfile = open('names.txt', 'r')
#     for count in myfile:
#         total += 1
#     myfile.close()
#     print(f'Total number of names is: {total}')
#
#
# if __name__ == "__main__":
#     main()

# 6.2.5
# def main():
#     total = 0
#     myfile = open("numbers.txt", 'r')
#     for line in myfile:
#         line = float(line)
#         total += line
#     print(f'Total= {total}')
#     myfile.close()
#
#
# if __name__ == '__main__':
#     main()

# 6.2.6
# def main():
#     total = 0
#     count = 0
#     myfile = open("numbers.txt", 'r')
#     for line in myfile:
#         line = float(line)
#         total += line
#         count += 1
#     average = total / count
#     print(f'Average is: {average}')
#     myfile.close()
#
#
# if __name__ == '__main__':
#     main()

# 6.2.7
# import random
#
#
# def main():
#     r_quantity = int(input("How many random numbers do you want? "))
#     myfile = open("random2.txt", 'w')
#     for number in range(0, r_quantity):
#         number = random.randint(1, 500)
#         myfile.write(f'{number}\n')
#     myfile.close()
#     print("Numbers have been written successfully.")
#
#
# if __name__ == '__main__':
#     main()

# 6.2.8
# def main():
#     total = 0
#     count = 0
#
#     myfile = open("random2.txt", 'r')
#     for line in myfile:
#         count += 1
#         line = int(line)
#         total += line
#     myfile.close()
#     print(f'Total sum is: {total}')
#     print(f'Total count is: {count}')
#
#
# if __name__ == '__main__':
#     main()


# 6.2.9
# def main():
#     total = 0
#     count = 0
#     try:
#         myfile = open("numbers.txt", 'r')
#         for line in myfile:
#             total += line
#             count += 1
#         average = total / count
#         print(f'Average is: {average}')
#         myfile.close()
#     except IOError:
#         print("ERROR while opening file.")
#     except ValueError:
#         print("Value Error")
#     except:
#         print("Error")
#
#
# if __name__ == '__main__':
#     main()

# 6.2.10
# def main():
#     myfile = open("golf.txt", 'w')
#
#     answer = 'y'
#     while answer == 'y' or answer == 'Y' or answer == 'yes' \
#         or answer == 'Yes':
#         name = input("Enter player name: ")
#         score = int(input("Enter the score: "))
#         myfile.write(f'{name}\n')
#         myfile.write(f'{score}\n')
#         answer = input("Do you want to enter one more name (y/n)? ")
#         print()
#     myfile.close()
#
#     g_answer = input("Do you want to see the list of players (y/n)? ")
#     if g_answer == 'y' or 'Y' or 'yes':
#         golf_players = open("golf.txt", 'r')
#         players = golf_players.read()
#         print("Players:")
#         print(players)
#         golf_players.close()
#     else:
#         print("Buy!")
#
#
# if __name__ == "__main__":
#     main()

# 6.2.11
# def main():
#     name = input("Enter your name: ")
#     your_text = input("Describe yourself: ")
#     html_template = open("html_template.txt", 'w')
#     print()
#     html_template.write('<html>' + '\n')
#     html_template.write('<head>' + '\n')
#     html_template.write('</head>' + '\n')
#     html_template.write('<body>' + '\n')
#     html_template.write(f' {"<center>"}' + '\n')
#     html_template.write(f'  {"<h1>"}{name}{"</h1>"}' + '\n')
#     html_template.write(f' {"</center>"}' + '\n')
#     html_template.write(f' {"<hr />"}' + '\n')
#     html_template.write(f' {your_text}' + '\n')
#     html_template.write(f' {"<hr />"}' + '\n')
#     html_template.write('</body>' + '\n')
#     html_template.write('</html>' + '\n')
#     html_template.close()
#
#     read_html = open('html_template.txt', 'r')
#     html = read_html.read()
#     print(html)
#     read_html.close()
#
#
# if __name__ == "__main__":
#     main()

# 6.2.12
def main():
    months = ('January', 'Fabruary', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December')
    days = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30)
    myfile = open("steps.txt", 'r')
    for x in range(12):
        total = 0
        average = 0
        for y in range(days[x]):
            steps = int(myfile.readline())
            total = total + steps
        average = total / days[x]
        print(f'The average steps in {months[x]} is: {average:.2f}')


if __name__ == "__main__":
    main()
