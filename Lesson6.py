# Task 1
def progression(a1, d, n):
    prog = [a1 + (i * d) for i in range(n)]
    return prog

a1 = int(input("First element: "))
d = int(input("Progression difference: "))
n = int(input("Elements count: "))

prog = progression(a1, d, n)

print("Элементы арифметической прогрессии:")
for i in progression:
    print(i)


#Task 2
def f_index(arr, min, max):
    indices = []
    for i, value in enumerate(arr):
        if min <= value <= max:
            indices.append(i)
    return indices

arr = [7, 12, 24, 40, 15, 3]
min = 12
max = 40

temp = f_index(arr, min, max)
print(temp)