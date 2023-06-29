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
def main():
    total = 0
    COUNT = 5
    filename = open(input('Enter file name: '), 'r')
    content = filename.readline()
    while content != '' and total < COUNT:
        total += 1
        content = content.rstrip('\n')
        print(f'{total}: {content}')
        content = filename.readline()
    filename.close()


if __name__ == "__main__":
    main()
