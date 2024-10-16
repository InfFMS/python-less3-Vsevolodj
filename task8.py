# с клавиатуры вводится число N, а затем – N целых чисел.
# Определить, сколько было введено положительных и
# сколько отрицательных чисел (нули не считать!).
count_poz = 0
count_neg = 0
val = int(input())

while val !=0:
    value = int(input())
    if value>0:
        count_poz+=1
    elif value<0:
        count_neg+=1
    val-=1
print("Положительных:",count_poz, "Отрицательных:",count_neg )
