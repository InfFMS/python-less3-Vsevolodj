# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить, среднее арифметическое тех введённых чисел,
# которые являются степенями числа 2.
# Вывести "нет", если таких чисел нет.
count=0
sum = 0
val = int(input())

while val !=0:
    value = val
    while value != 0:
        value = value/2
        if value%2==1:
            break
    if value==1:
        sum= sum+val
        count +=1

    val = int(input())
print("Cреднее:",sum/count)




