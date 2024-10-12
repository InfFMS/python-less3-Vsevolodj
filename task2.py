# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить, сколько было введено двузначных натуральных чисел,
# и сколько других.
count_poz = 0
count_dr = 0
value = int(input())
while value !=0:
    if value>0 and 9<value<100:
        count_poz+=1
    else:
        count_dr+=1
    value = int(input())
print("Положительных двузначных:",count_poz, "Других:",count_dr )



