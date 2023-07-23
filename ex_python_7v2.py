# ex 7.8
# def main():
#     boy_names_file = open('BoyNames.txt', 'r')
#     girl_names_file = open('GirlNames.txt', 'r')
#
#     # create boy names lists with elements from files
#     # boy_names_list = []
#     # for name in boy_names_file:
#     #     name = name[:-1]
#     #     boy_names_list.append(name)
#     # print(boy_names_list)
#     # boy_names_file.close()
#
#     # another method
#     boy_names_list = boy_names_file.readlines()
#     for index in range(len(boy_names_list)):
#         boy_names_list[index] = boy_names_list[index].rstrip('\n')
#     boy_names_file.close()
#
#     # create girl names lists with elements from files
#     girl_names_list = []
#     for name in girl_names_file:
#         name = name[:-1]
#         girl_names_list.append(name)
#     girl_names_file.close()
#
#     gender = str(input("What name do you want to find (boy, girl or both): "))
#     if gender == 'boy':
#         boy_name = str(input("Enter the boy's name: "))
#         if boy_name in boy_names_list:
#             print(f'{boy_name} is a popular boy name.')
#         else:
#             print(f'{boy_name} is not popular boy name.')
#     elif gender == 'girl':
#         girl_name = str(input("Enter the girl's name: "))
#         if girl_name in girl_names_list:
#             print(f'{girl_name} is a popular girl name.')
#         else:
#             print(f'{girl_name} is not popular girl name.')
#     elif gender == 'both':
#         boy_name = str(input("Enter the boy's name: "))
#         girl_name = str(input("Enter the girl's name: "))
#         if boy_name in boy_names_list:
#             print(f'{boy_name} is a popular boy name.')
#         else:
#             print(f'{boy_name} is not popular boy name.')
#         if girl_name in girl_names_list:
#             print(f'{girl_name} is a popular girl name.')
#         else:
#             print(f'{girl_name} is not popular girl name.')
#
#
# if __name__ == '__main__':
#     main()

# ex 7.9
# def main():
#     year = 1951
#     # open file
#     us_population_file = open('USPopulation.txt', 'r')
#     # create a list from file
#     us_population_list = population_list_f(us_population_file)
#     us_population_file.close()
#     # print(us_population_list)
#
#     # create a change list
#     changes_list = []
#     list_2 = [item for item in us_population_list]
#     for index in range(len(us_population_list)):
#         num1 = us_population_list[index]
#         del list_2[0]
#         if list_2 != []:
#             num2 = list_2[0]
#             # print(f'num2 {num2}')
#             num3 = num2 - num1
#             changes_list.append(num3)
#
#     total_c = 0
#     for value in changes_list:
#         total_c += value
#
#     # average population change
#     average_change_per_year = (float(us_population_list[-1]) -
#                                float(us_population_list[0])) / \
#         len(us_population_list)
#     print(f'Average change per year: {average_change_per_year:,.2f}')
#
#     # max and min
#     max_pop = max(changes_list)
#     min_pop = min(changes_list)
#
#     # total_pop_change = float(
#     #         us_population_list[-1]) - float(us_population_list[0])
#     # print(f'total_pop_change {total_pop_change}')
#     # print(f'total_c {total_c}')
#
#     # create a year list
#     year_list = year_list_f(changes_list, year)
#
#     for index in range(len(changes_list)):
#         if changes_list[index] == max_pop:
#             print(f'max {max_pop:,.2f} in {year_list[index]}')
#         elif changes_list[index] == min_pop:
#             print(f'min {min_pop:,.2f} in {year_list[index]}')
#
#     print(f'year count {len(year_list)}')
#     print(f'changes count {len(changes_list)}')
#
#
# # create a list from a file
# def population_list_f(myfile):
#     # create a list with population
#     population_list = myfile.readlines()
#     # remove '\n'
#     for index in range(len(population_list)):
#         population_list[index] = float(population_list[index])
#     return population_list
#
#
# # calculate total population for all years
# # def grand_total_f(population_list):
# #     total = 0
# #     for value in population_list:
# #         total += value
# #     return total
#
#
# # create a list with years
# def year_list_f(population_list, year):
#     year_list = []
#     for index in range(len(population_list)):
#         year_list.append(year)
#         year += 1
#     return year_list
#
#
# if __name__ == '__main__':
#     main()

# ex 7.10
# def main():
#     world_winners_file = open('WorldSeriesWinner.txt', 'r')
#     world_win_list = world_winners_file.readlines()
#     # remove '\n' from a list
#     for index in range(len(world_win_list)):
#         world_win_list[index] = world_win_list[index].rstrip('\n')
#     world_winners_file.close()
#
#     # list of years
#     # starting year
#     year = 1903
#     years_list = []
#     for index in range(len(world_win_list)):
#         if year == 1904 or year == 1994:
#             year += 1
#             years_list.append(year)
#             year += 1
#         else:
#             years_list.append(year)
#             year += 1
#     # years_list.remove(YEAR1)
#     # years_list.remove(YEAR2)
#     # print(f'year_list count {len(years_list)}')
#     # print(f'world_win_list count {len(world_win_list)}')
#
#     your_team = input("Enter your team: ")
#     # count = 0
#     # for team in world_win_list:
#     #     if team == your_team:
#     #         count += 1
#
#     # print(f'Your team {your_team} has been winners '
#     #       f'{count} times')
#
#     print(f'Your team {your_team} has been winners '
#           f'{world_win_list.count(your_team)} times')
#
#     for index in range(len(world_win_list)):
#         if world_win_list[index] == your_team:
#             print(f'{your_team} in {years_list[index]}')
#
#
# if __name__ == '__main__':
#     main()

# ex 7.11
import random


# def main():
#     # magic list
#     magic_list = [[4, 9, 2],
#                   [3, 5, 7],
#                   [8, 1, 6]]
#     ROW = 3
#     COL = 3
#
#     # создать пустой двуменрный список
#     # my_list = [[0 for item in range(ROW)] for item in range(COL)]
#     # print(my_list)
#
#     my_list = []
#     for r in range(ROW):
#         my_list.append([0] * COL)
#
#     # fill in the list with your numbers
#     for r in range(ROW):
#         for c in range(COL):
#             your_number = int(input("Enter any number from 1 to 9: "))
#             my_list[r][c] = your_number
#         print(my_list)
#     print(my_list)
#     print(magic_list)
#
#     # # fill in list with random numbers
#     # for r in range(ROW):
#     #     for c in range(COL):
#     #         my_list[r][c] = random.randint(1, 9)
#     # print(my_list)
#     # print(magic_list)
#     #
#     # check if my list is a magic list
#     flag = True
#     for r in range(ROW):
#         for c in range(COL):
#             if magic_list[r][c] == my_list[r][c]:
#                 flag = True
#             else:
#                 flag = False
#             print(flag)
#     print(flag)
#
#
# if __name__ == '__main__':
#     main()

# ex 7.12
def main():
    your_number = int(input("Enter any integer number more then 1: "))
    my_list = []
    for value in range(your_number):
        my_list.append(value + 1)
    del my_list[0]
    prime_comp_numb_f(my_list)


def prime_comp_numb_f(my_list):
    for index in range(len(my_list)):
        count = 0
        for value in my_list:
            number = my_list[index] % value
            if number == 0:
                count += 1
        if count > 1:
            print(f'{my_list[index]} is Complex value')
        else:
            print(f'{my_list[index]} is Prime value')


if __name__ == '__main__':
    main()
