numbers = [94, 14, 27, 85, 41, 97, 43, 57, 45, 4, 78, 80, 28, 68, 92, 60, 61, 59, 89, 74, 10, 78, 84, 32, 85, 17, 56,
           90, 48, 8, 47, 5, 50, 33, 6, 18, 82, 36, 91, 101, 54, 75, 81, 2, 48, 65, 53, 8, 37, 81, 59, 87, 84, 89, 38,
           95, 99, 83, 96, 47, 64, 92, 15, 74, 96, 37, 2, 43, 16, 28, 80, 25, 24, 16, 54, 48, 36, 30, 52, 72, 6, 57, 23,
           77, 39, 61, 26, 65, 22, 75, 67, 28, 33, 84, 80, 67, 1, 38, 25, 2]

"""
Keresés

i = 0
ciklus amíg i<n és t[i]<>ker
    i = i + 1
ciklus vége

Ha i<n akkor
    ki "Van ilyen" 
    ki: "Indexe: ", i
különben
    ki: "A keresett érték nem található"
ha vége
"""
print("Keresés")

# Ver 1

ker = 8
i = 0
n = len(numbers)
while i < n and numbers[i] != ker:
    i = i + 1

if i < n:
    print(f"Van ilyen, index: {i}")
else:
    print("A keresett érték nem található")

# Ver 2
i = 0
found = False
for i, elem in enumerate(numbers):
    if elem == ker:
        found = True
        break

if found:
    print(f"Van ilyen, index: {i}")
else:
    print("A keresett érték nem található")

# Ver 3
print(f"Van ilyen, index: {numbers.index(ker)}") if ker in numbers else print("A keresett érték nem található")

"""

Maximum kiválasztás

max = t[0]
ciklus i = 1 .. n - 1
    ha t[i]> max akkor 
        max = t[i]
    ha vége
ciklus vége
ki max

"""
print("Maxkiv")

# Ver 1
max_val = numbers[0]
i = 0
n = len(numbers)
while i < n:
    if numbers[i] > max_val:
        max_val = numbers[i]

    i = i + 1

print(f"Max {max_val}")

# Ver 2
max_val = numbers[0]
for elem in numbers:
    if elem > max_val:
        max_val = elem

print(f"Max {max_val}")

# Ver 3
print(f"Max {max(numbers)}")

""" 

Kiválogatás

j = 0
ciklus i = 0 .. n - 1
    ha a[i] < 5 
        b[j] = a[i]
        j = j + 1
    ha vége
ciklus vége

"""
print("Kiválogatás")

# Ver 1
j = 0
i = 0
n = len(numbers)
b = []
while i < n:
    if numbers[i] < 5:
        b.append(numbers[i])
    i = i + 1

print(b)

# Ver 2
b = []
for elem in numbers:
    if elem < 5:
        b.append(elem)

print(b)

# Ver 3

b = [elem for elem in numbers if elem < 5]
print(b)