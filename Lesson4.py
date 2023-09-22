#Задание 1
mn1 = set()
mn2 = set()
n = int(input("Введите длину первого множества: "))
m = int(input("Введите длину второго множества: "))
    
print("Ввод первого множества:")
for i in range(n):
    e = int(input())
    mn1.add(e)

print("Ввод второго множества:")
for i in range(m):
    e = int(input())
    mn2.add(e)

res = list(mn1.intersection(mn2))
   
print("Общие элементы, отсортированные по возрастанию:")
for e in res:
   print(e)



#Задание 2

# Чтение данных из файла
with open("input.txt", "r") as file:
    # Считываем количество кустов
    n = int(file.readline().strip())

    # Считываем количество ягод на каждом кусте
    berries = list(map(int, file.readline().strip().split()))

n = len(berries)

if n == 0:
    max_berries = 0

if n == 1:
    max_berries = berries[0]

# Инициализация массива для хранения максимального количества собранных ягод
max_collected = [0] * n

# Инициализация значений для первых двух кустов
max_collected[0] = berries[0]
max_collected[1] = max(berries[0], berries[1])

# Вычисляем максимальное количество собранных ягод для каждого куста
for i in range(2, n):
    max_collected[i] = max(max_collected[i - 1], max_collected[i - 2] + berries[i], max_collected[i - 2] + berries[i - 1] + berries[i])

max_berries = max_collected[-1]

# Выводим результат
print("Максимальное количество ягод, которое можно собрать за один заход:", max_berries)
