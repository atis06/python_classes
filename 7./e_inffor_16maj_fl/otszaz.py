# 1. feladat
from collections import Counter

purchases = []

with open("Forrasok/4_Otszaz/penztar.txt", "r") as file:
    purchase = []
    for line in file.readlines():
        stripped_line = line.strip()
        if stripped_line != "F":
            purchase.append(stripped_line)
        else:
            purchases.append(purchase)
            purchase = []

# print(purchases)

# 2. feladat
print("2. feladat")
print(f"A fizetések száma: {len(purchases)}")
print("\n")

# 3. feladat
print("3. feladat")
print(f"Az első vásárló {len(purchases[0])} darab árucikket vásárolt.")
print("\n")

# 4. feladat
print("4. feladat")
"""
p_order = int(input("Adja meg egy vásárlás sorszámát!\n"))
article = input("Adja meg egy árucikk nevét!\n")
article_nr = int(input("Adja meg a vásárolt darabszámot!\n"))
"""
p_order = 2
article = "kefe"
article_nr = 2

print("\n")

# 5. feladat
print("5. feladat")

first = 0
last = 0
c = 0

for i, p in enumerate(purchases):
    if article in p:
        c += 1

        if first == 0:
            first = i + 1

        last = i + 1

print(f"Az első vásárlás sorszáma: {first}")
print(f"Az utolsó vásárlás sorszáma: {last}")
print(f"{c} vásárlás során vettek belőle.")

print("\n")

# 6. feladat
print("6. feladat")


def ertek(nr):
    price = nr * 500

    if nr == 1:
        to_sub = 0
    elif nr >= 2:
        to_sub = 50 + (nr - 2) * 100
    else:
        raise ValueError("Hibas bemenet!")

    price = price - to_sub

    return price


print("\n")

# 7. feladat
print("7. feladat")

selected_purchase = purchases[p_order - 1]

amounts = {}

for elem in selected_purchase:
    if elem not in amounts:
        amounts[elem] = 1
    else:
        amounts[elem] = amounts[elem] + 1

# print(Counter(selected_purchase))
for k, v in amounts.items():
    print(v, k)

print("\n")

# 8. feladat
print("8. feladat")

with open("osszeg.txt", "w") as file_out:
    for i, purchase in enumerate(purchases):
        paid = 0
        article_c = Counter(purchase)
        for count in article_c.values():
            paid += ertek(count)

        file_out.write(f"{i+1}: {paid}\n")

print("\n")

