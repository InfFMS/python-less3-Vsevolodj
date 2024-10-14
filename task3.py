# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить, сколько было введено простых натуральных чисел
# (которые делятся только сами на себя и на 1), и сколько составных.
value = int(input())
d = 2
allcount = 0
count = 0
while value !=0:
    allcount +=1
    while value % d != 0:
        d += 1
    if d == value:
        count += 1
    value = int(input())
    d=2
print("Положительных простых:",count, "Составных:",allcount-count)


