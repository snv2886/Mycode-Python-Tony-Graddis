# def main():
#     str1 = 'one two three four'
#     str2 = '10:20:30:40:50'
#     str3 = 'a/b/c/d/e/f'
#
#     # Функция выводит лексемы в каждом строковом литерале
#     display_tokens(str1, ' ')
#     print()
#     display_tokens(str2, ':')
#     print()
#     display_tokens(str3, '/')
#     print()
#
#
# def display_tokens(data, delimiter):
#     tokens = data.split(delimiter)
#     for item in tokens:
#         print(f'Лексемы: {item}')
#
#
# if __name__ == "__main__":
#     main()

# def main():
#     csv_file = open('test_scores.csv', 'r')
#     # Прочитать строки файла в список
#     lines = csv_file.readlines()
#     csv_file.close()
#     print(lines)
#
#     # Обработать строки
#     # создать отдельные списки для каждой строки
#     for line in lines:
#         tokens = line.split(',')
#         print(tokens)
#
#     # Подсчитать общее количество баллов
#         total = 0
#         for token in tokens:
#             total += float(token)
#             print(f'Total = {total}')
#
#         # Подсчитать средний балл
#         average = total / len(tokens)
#         print(f'Average = {average}')
#
#
# if __name__ == "__main__":
#     main()

# mystring = 'Hello World! My name iS NiKiTa!'
# count = 0
# for item in range(len(mystring)):
#     if mystring[item].isupper():
#         count += 1
# print(count)

# ex 8.1
# def main():
#     first_name = input("Enter your first name: ")
#     surname = input("Enter your surname: ")
#     last_name = input("Enter your last name: ")
#     print(f'{first_name[0]}.{surname[0]}.{last_name[0]}')
#
#
# if __name__ == "__main__":
#     main()

# ex 8.2
# def main():
#     number = input("Enter any number without delimiters: ")
#     total = 0
#     for ch in number:
#         total += float(ch)
#     print(total)
#
#
# if __name__ == "__main__":
#     main()

# ex 8.3
# def main():
#     month = (
#         'january', 'february', 'march', 'april', 'may', 'june', 'july',
#         'august', 'september', 'october', 'novermber', 'december'
#     )
#     date = input("Enter any date in format dd/mm/yyyy: ")
#     date_list = date.split('/')
#     print(f'{int(date_list[0])} {month[int(date_list[1]) - 1]} '
#           f'{date_list[2]}.y')
#
#
# if __name__ == "__main__":
#     main()

# ex 8.4
# def main():
#     morze_symbol = (
#         ' ', ',', '.', '?', '0', '1', '2', '3', '4', '5', '6', '7', '8',
#         '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
#         'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
#         'Z', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К',
#         'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч',
#         'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я'
#     )
#     morze_code = (
#         'space', '--..--', '.-.-.-', '..--..', '-----', '.----', '..---', '...--',
#         '....-', '.....', '-....', '--...', '---..', '----.', '.-', '-...',
#         '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..',
#         '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-',
#         '.--', '-..-', '-.-', '--..', '.-', '-...', '.--', '--.', '-..', '.',
#         '.', '...-', '--..', '..', '.---', '-.-', '.-..', '--', '-.', '---',
#         '.--.', '.-.', '...', '-', '..-', '..-.', '....', '-.-.', '---.',
#         '----', '--.-', '.--.-.', '-.--', '-..-', '..-..', '..--', '.-.-'
#     )
#     your_text = input("Enter any text: ")
#     morze_text = ''
#     for ch in your_text:
#         morze_index = morze_symbol.index(ch.upper())
#         morze_text += morze_code[morze_index] + ' '
#     print(morze_text.rstrip())
#
#
# if __name__ == "__main__":
#     main()

# ex 8.5
# def main():
#     set1 = ['A', 'B', 'C']
#     set2 = ['D', 'E', 'F']
#     set3 = ['G', 'H', 'I']
#     set4 = ['J', 'K', 'L']
#     set5 = ['M', 'N', 'O']
#     set6 = ['P', 'Q', 'R', 'S']
#     set7 = ['T', 'U', 'V']
#     set8 = ['W', 'X', 'Y', 'Z']
#
#     your_number = input("Enter the nuber with letters "
#                         "like this (XXX-XXX-XXXX): ")
#     your_number = your_number.upper()
#     digit_number = ''
#     for ch in your_number:
#         if ch in set1:
#             digit_number += '2'
#         elif ch in set2:
#             digit_number += '3'
#         elif ch in set3:
#             digit_number += '4'
#         elif ch in set4:
#             digit_number += '5'
#         elif ch in set5:
#             digit_number += '6'
#         elif ch in set6:
#             digit_number += '7'
#         elif ch in set7:
#             digit_number += '8'
#         elif ch in set8:
#             digit_number += '9'
#         else:
#             digit_number += ch
#
#     print(digit_number)
#
#
# if __name__ == "__main__":
#     main()

# ex 8.6
# def main():
#     my_file = open('text.txt', 'r')
#     my_list = my_file.readline()
#     line_sentence = my_list.split()
#     count_sentence = 0
#     total_count = 0
#     while my_list != '':
#         count_sentence += 1
#         total_count += len(line_sentence)
#         my_list = my_file.readline()
#         line_sentence = my_list.split()
#     my_file.close()
#     average = total_count / count_sentence
#     print(f'Average sentences in line is {average:,.0f}')
#
#
# if __name__ == "__main__":
#     main()

# ex 8.6
# def main():
#     my_file = open('text.txt', 'r')
#     my_list = my_file.readlines()
#     my_file.close()
#     total = 0
#     for sentence in my_list:
#         total += len(sentence.split())
#     average = total / len(my_list)
#     print(f'Average sentences in line is {average:,.0f}')
#
#
# if __name__ == "__main__":
#     main()


# ex 8.7
# def main():
#     my_file = open('text.txt', 'r')
#     my_list = my_file.readlines()
#     my_file.close()
#     uppercase = 0
#     lowercase = 0
#     digits = 0
#     spaces = 0
#     other = 0
#     for sentence in my_list:
#         for ch in sentence:
#             if ch.isupper():
#                 uppercase += 1
#             elif ch.islower():
#                 lowercase += 1
#             elif ch.isdigit():
#                 digits += 1
#             elif ch.isspace():
#                 spaces += 1
#             else:
#                 other += 1
#     total = uppercase + lowercase + digits + spaces
#     print(f'Uppercase ={uppercase}')
#     print(f'Lowercase ={lowercase}')
#     print(f'Digits ={digits}')
#     print(f'Spaces ={spaces}')
#     print(f'Total ={total} vs other={other}')
#     print()
#
#
# if __name__ == "__main__":
#     main()
#
#
# # v2
# def main():
#     my_file = open('text.txt', 'r')
#     my_list = my_file.read()
#     print(len(my_list))
#     my_file.close()
#     uppercase = 0
#     lowercase = 0
#     digits = 0
#     spaces = 0
#     other = 0
#     for ch in my_list:
#         if ch.isupper():
#             uppercase += 1
#         elif ch.islower():
#             lowercase += 1
#         elif ch.isdigit():
#             digits += 1
#         elif ch == ' ':
#             spaces += 1
#         else:
#             other += 1
#     total = uppercase + lowercase + digits + spaces
#     print(f'Uppercase ={uppercase}')
#     print(f'Lowercase ={lowercase}')
#     print(f'Digits ={digits}')
#     print(f'Spaces ={spaces}')
#     print(f'Total ={total} vs other={other}')
#
#
# if __name__ == "__main__":
#     main()

# ex 8.8
# def main():
#     your_sentence = input("Enter your sentence: ")
#     sentence_list = your_sentence.split('.')
#     print(mod_sentence(sentence_list))
#
#
# def mod_sentence(stc_list):
#     answer = ''
#     for stc in stc_list:
#         if stc != '':
#             stc_line = stc.strip(' ')
#             stc_line += '.'
#             stc_line = stc_line[0].upper() + stc_line[1:] + ' '
#             answer += stc_line
#     return answer
#
#
# if __name__ == "__main__":
#     main()

# ex v2 8.8
# def main():
#     enter_string = input('Please enter a string: ')
#     answer = ''
#     sentence_start = True
#     for character in enter_string:
#         if sentence_start is True:
#             if character.isalpha():
#                 character = character.upper()
#                 sentence_start = False
#         if character == '.' or character == '!' or character == '?':
#             sentence_start = True
#         answer += character
#
#     print('The modified string is:', answer)
#
#
# if __name__ == "__main__":
#     main()

# ex 8.9
# def main():
#     consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N',
#                   'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
#     vowels = ['A', 'E', 'I', 'O', 'U']
#
#     text = input("Enter your text: ")
#     conson_vowels(text, consonants, vowels)
#
#
# def conson_vowels(text, consonants, vowels):
#     consonants_count = 0
#     vowels_count = 0
#
#     for ch in text:
#         if ch.upper() in consonants:
#             consonants_count += 1
#         elif ch.upper() in vowels:
#             vowels_count += 1
#     print(f'Consonants ={consonants_count}, vowels ={vowels_count}')
#     print(f'Total count={len(text)}')
#
#
# if __name__ == "__main__":
#     main()

# ex v1 8.10
# def main():
#     mylist = []
#     count_list = []
#     your_text = input("Enter any text: ")
#     print(your_text)
#     for ch in your_text:
#         mylist.append(ch.lower())
#     for ch in range(len(mylist)):
#         count_list.append(mylist.count(mylist[ch]))
#         # print(f'{mylist[ch]} ={count_list[ch]}')
#     print(f'max element is {mylist[count_list.index(max(count_list))]} '
#           f'={max(count_list)} ')
#
#
# if __name__ == "__main__":
#     main()


# ex v2 8.10
# def main():
#     your_text = input("Enter any text: ")
#     a = your_text.lower()
#     print(a)
#     max_count = 0
#     max_element = ''
#     for i in a:
#         q = a.count(i)
#         if q > max_count:
#             max_count = q
#             max_element = i
#     print(f'element <{max_element}> has maximum reps ={max_count}')
#
#
# if __name__ == "__main__":
#     main()

# ex 8.11

