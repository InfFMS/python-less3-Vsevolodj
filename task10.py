# с клавиатуры вводится число N, а затем – N натуральных чисел.
# Определить минимальное и максимальное среди простых чисел
# (которые делятся на сами не себя и на 1).
# Если таких чисел не было, вывести "нет".
def isPrime(n):
    for i in range(2,n+1):
        if n%i==0 and n!=i:
            return 0
            break
        if n%i==0 and n==i:
            return 1
            break
    return 0



s=[]
val = int(input())
while val !=0:
    value = int(input())
    if isPrime(value) == 1:
        s +=[value]
    val-=1
if len(s)!=0:
    print(f'Минимальное:{min(s)},Максимальное:{max(s)}')
else: print("нет")

