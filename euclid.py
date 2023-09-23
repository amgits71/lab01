def euclid(first_num, second_num):
    while second_num:
        first_num, second_num = second_num, first_num % second_num
    return first_num


first_num = int(input("Введите первое число: "))
second_num = int(input("Введите второе число: "))
print("НОД чисел ", first_num, " и ", second_num, ": ", euclid(first_num, second_num))