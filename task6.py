# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить минимальное и максимальное из введённых чисел.
value = int(input())
max=0
min=1000000000
while value !=0:
    if value > max:
        max=value
    if value < min:
        min = value
    value = int(input())
print(max, min)
