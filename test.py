my_list = [2, 3, 4, 5, 6, 7, 8, 9]
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
        
