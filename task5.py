# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить, среднее арифметическое тех введённых чисел,
# которые являются степенями числа 2.
# Вывести "нет", если таких чисел нет.

value = int(input())
while value !=0:
    value = value/2
    if value%2==0:
        sum += value

    value = int(input())
print("Сумма:",sum)




