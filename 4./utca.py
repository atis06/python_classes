### 2018 okt-nov
# 1. feladat


property = []

with open("kerites.txt", 'r') as file:
    for line in file.readlines():
        fence = line.split()
        property.append(
            {
                "odd": int(fence[0]),
                "width": int(fence[1]),
                "color": fence[2],
            }
        )

print("\n")
print("2. feladat")
print("\n")

n = len(property)
print(f"Az eladott telkek száma: {n}")

print("\n")
print("3. feladat")
print("\n")

n = len(property)
if property[n - 1]["odd"] == 0:
    print("Az utolsó ház a páros oldalon van.")
else:
    print("Az utolsó ház a páratlan oldalon van")
even = 2
sendhelp = 0
for each in property:
    if each["odd"] == 0:
        sendhelp = sendhelp + 1
print(f"Az utolsó telek házszáma: ", even + sendhelp * 2 - 2)

print("\n")
print("4. feladat")
print("\n")

oddside = []
for each in property:
    if each["odd"] == 1:
        oddside.append(each)

i = 0
oddlenght = len(oddside)
found = False

while i < oddlenght and not found:
    if oddside[i]["color"] == oddside[i + 1]["color"] and oddside[i]["color"] != ':' and oddside[i]["color"] != '#':
        found = True

    else:
        i = i + 1
print("A szomszédossal egyezik a kerítés színe: ", i * 2 + 1)

print("\n")
print("5. feladat")
print("\n")

evenside = []
for each in property:
    if each["odd"] == 0:
        evenside.append(each)
evenleght = len(evenside)

request = int(input("Adjon meg egy házszámot! "))
i = 0
short = request // 2 - 1
short1 = request // 2

if request % 2 == 0:
    print(f"A kerítés színe / állapota: ", evenside[short]["color"])
else:
    print(f"A kerítés színe / állapota: ", oddside[short1]["color"])

print("\n")
print("6. feladat")
with open("utcakep.txt", 'w') as file:
    line_one = ""
    line_two = ""
    house_num = 1
    for p in property:
        if p["odd"] == 1:
            for c in range(p["width"]):
                line_one += p["color"]
            line_two += str(house_num) + ((p["width"] - len(str(house_num))) * " ")
            house_num += 2

    file.write(line_one + "\n" + line_two)

print("\n")



