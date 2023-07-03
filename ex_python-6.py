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
    total = 0
    count = 0

    myfile = open("random2.txt", 'r')
    for line in myfile:
        count += 1
        line = int(line)
        total += line
    myfile.close()
    print(f'Total sum is: {total}')
    print(f'Total count is: {count}')


if __name__ == '__main__':
    main()
