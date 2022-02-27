numbers = [94, 14, 27, 85, 41, 97, 43, 57, 45, 4, 78, 80, 28, 68, 92, 60, 61, 59, 89, 74, 10, 78, 84, 32, 85, 17, 56,
           90, 48, 8, 47, 5, 50, 33, 6, 18, 82, 36, 91, 101, 54, 75, 81, 2, 48, 65, 53, 8, 37, 81, 59, 87, 84, 89, 38,
           95, 99, 83, 96, 47, 64, 92, 15, 74, 96, 37, 2, 43, 16, 28, 80, 25, 24, 16, 54, 48, 36, 30, 52, 72, 6, 57, 23,
           77, 39, 61, 26, 65, 22, 75, 67, 28, 33, 84, 80, 67, 1, 38, 25, 2]
"""
Összegzés

osszeg = 0
ciklus i = 0 .. n-1
    osszeg = osszeg + t[i]
ciklus vége
ki osszeg
"""
print("Összegzés")
# 1. ver
s = 0
i = 0
n = len(numbers)
while i <= n - 1:
    s = s + numbers[i]
    i += 1

print(s)

# 2. ver
s = 0
for elem in numbers:
    s = s + elem

print(s)

# 3. ver
print(sum(numbers))

"""
Megszámlálás

szamlalo = 0
ciklus i = 0 .. n - 1
    ha t[i] < 0 akkor 
        szamlalo = szamlalo + 1
    ha vége
ciklus vége
ki szamlalo
"""
print("Megszámlálás")
# 1. ver
c = 0
i = 0
while i <= n - 1:
    if numbers[i] <= 50:
        c = c + 1

    i += 1

print(c)

# 2. ver
c = 0
for elem in numbers:
    if elem <= 50:
        c += 1

print(c)

"""
Eldöntés 

van = 0
ciklus i = 0 .. n-1
ha tomb[i] = keresett_ertek akkor
    van = 1
ha vége
ciklus vége
"""
print("Eldöntés")
# 1. ver
found = False
i = 0
while i <= n - 1 and not found:
    if numbers[i] == 75:
        found = True
        # break
    i = i + 1

print(found)

# 2. ver
found = False
for elem in numbers:
    if elem == 75:
        found = True
        break

print(found)

"""
Kiválasztás

i = 0
ciklus amíg tomb[i] <> ker
    i = i + 1
ciklus vége
ki i + 1
"""
# 1. ver
print("Kiválasztás")
i = 0
while numbers[i] != 75:
    i = i + 1
print(i)

# 2. ver
for i, elem in enumerate(numbers):
    if numbers[i] == 75:
        break

print(i)

###############################################

# Keresés
# Maximum kiválasztás

# Kiválogatás



