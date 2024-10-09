#с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить, сколько было введено положительных
# и сколько отрицательных чисел.
count_poz = 0
count_neg = 0
value = int(input())
while value !=0:
    if value>0:
        count_poz+=1
    elif value<0:
        count_neg+=1
    value = int(input())
print("Положительных:",count_poz, "Отрицательных:",count_neg )


