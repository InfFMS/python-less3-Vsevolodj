# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить сумму тех введённых чисел, которые делятся на 5.
sum= 0
value = int(input())
while value !=0:
    if value%5==0:
        sum += value
    value = int(input())
print("Сумма:",sum)



