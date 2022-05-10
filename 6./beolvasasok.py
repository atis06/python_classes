# e_inffor_15maj_fl
MAX_DAY_NR = 11

# 1.

with open("e_inffor_15maj_fl/veetel.txt", "r") as file:
    lines = file.readlines()

    data = []

    i = 0
    while i < len(lines):
        message = {}

        line_1 = lines[i]
        line_2 = lines[i + 1]

        message["day"] = int(line_1.split()[0])
        message["amateur"] = int(line_1.split()[1])
        message["message"] = line_2

        data.append(message)

        i += 2

# 2.
print("2. feladat:")
print(f"Az első üzenet rögzítője: " + str(data[0]["amateur"]))
print(f"Az utolsó üzenet rögzítője: " + str(data[-1]["amateur"]))
print("\n")

# 3.
print("3. feladat:")
for elem in data:
    if "farkas" in elem["message"]:
        print(str(elem["day"]) + ". nap " + str(elem["amateur"]) + ". rádióamatőr")
print("\n")

# 4.
print("4. feladat:")
stat = {}
for i in range(1, MAX_DAY_NR + 1):
    stat[i] = 0

for elem in data:
    day = elem["day"]
    stat[day] = stat[day] + 1

for i in range(1, MAX_DAY_NR + 1):
    print(f"{i}. nap: {stat[i]} rádióamatőr")

print("\n")

# 5.
messages_by_days = {}

for elem in data:
    day = elem["day"]
    if day not in messages_by_days:
        messages_by_days[day] = [elem["message"]]
    else:
        messages_by_days[day].append(elem["message"])

with open("adas.txt", "w") as file_out:
    for day in sorted(messages_by_days.keys()):
        messages = messages_by_days[day]

        msg_orig = ""
        len_msg = len(messages[0])

        for i in range(len_msg):
            next_char = "#"
            for message in messages:
                if message[i] != "#":
                    next_char = message[i]

            msg_orig += next_char

        file_out.write(msg_orig + "\n")

# 6.

"""
Függvény szame(szo:karaktersorozat): logikai
    valasz:=igaz
    Ciklus i:=1-től hossz(szo)-ig
        ha szo[i]<'0' vagy szo[i]>'9' akkor valasz:=hamis
    Ciklus vége
    szame:=valasz
Függvény vége
"""


def szame(szo):
    valasz = True

    i = 0
    while i < len(szo):
        if not szo[i].isdigit():
            valasz = False

        i += 1

    return valasz


# 7.
day_in = int(input("Adja meg a nap sorszámát!\n"))
amateur_in = int(input("Adja meg a rádióamatőr sorszámát!\n"))

found = False
for elem in data:
    if elem["day"] == day_in and elem["amateur"] == amateur_in:
        found = True

        message = elem["message"]
        to_extract = message[0:5]

        species = []
        for i in range(len(to_extract) - 1):
            if to_extract[i].isdigit() and to_extract[i+1].isdigit():
                species.append(int(to_extract[i] + to_extract[i+1]))
            elif to_extract[i].isdigit() and (to_extract[i+1] == "/" or to_extract[i+1] == " "):
                species.append(int(to_extract[i]))
            else:
                pass

        species_num = sum(species)

        if not species:
            print("Nincs információ")

        if species:
            print(f"A megfigyelt egyedek száma: {species_num}")

if not found:
    print("Nincs ilyen feljegyzés")
