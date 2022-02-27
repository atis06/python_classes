numbers = [94, 14, 27, 85, 41, 97, 43, 57, 45, 4, 78, 80, 28, 68, 92, 60, 61, 59, 89, 74, 10, 78, 84, 32, 85, 17, 56,
           90, 48, 8, 47, 5, 50, 33, 6, 18, 82, 36, 91, 101, 54, 75, 81, 2, 48, 65, 53, 8, 37, 81, 59, 87, 84, 89, 38,
           95, 99, 83, 96, 47, 64, 92, 15, 74, 96, 37, 2, 43, 16, 28, 80, 25, 24, 16, 54, 48, 36, 30, 52, 72, 6, 57, 23,
           77, 39, 61, 26, 65, 22, 75, 67, 28, 33, 84, 80, 67, 1, 38, 25, 2]


"""
Keresés

ker = 30
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

#24 a keresett érték
i=0
for elem in numbers:
    if i<n and numbers[i] !=24 :
        i=i+1
if i<n:
    print("Van ilyen")
    print("Az indexe: ",i)
else:
    print("Az érték nem található")
            #for elem in numbers:
             # if numbers[i] !=24:
             #    i=i+1
             #if i<n:
              #   print("Van ilyen")
               #  print("Indexe: ",i)
             #else:
                  #print("A keresett érték nem található")


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
print("Maximum kiválasztás")
max= numbers[0]
for i, elem in enumerate(numbers):
    if numbers[i]> max:
        max=numbers[i]
print(max)
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

b=[]
j=0
for i, elem in enumerate(numbers):
    if numbers[i] <80:
        b.append(numbers[i])
        j=j+1
print(b)




