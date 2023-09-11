n = int(input('Количество монеток: '))
o = 0
m = 0
for i in range (n):
    c = int(input('Орел=1, Решка=0: '))
    if c == 1:
        o += 1

r = n - o
if r < o:
    m = r
else:
    m = o
print(m)



a = int(input('Введите сумму чисел: '))
b = int(input('Введите произведение чисел: '))
c = a + b
f = 0
for i in range(c):
    if f == 1:
        break
    for j in range(c):
        if i + j == a and i * j == b:
            f = 1
            res = [i, j]
            print(res)
            break


N = int(input('Введите число N, которое нельзя превосходить))): '))
k = 0
while 2**k <= N:
    print(2**k)
    k += 1