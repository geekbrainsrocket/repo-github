# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

number = int(input('Введите целое положительное число: '))
max_number = 0
while (number % 10) > 0:
    temp = number % 10
    if temp > max_number:
        max_number = temp
    number //= 10
print(f'Самая большая цифра числа: {max_number}')
