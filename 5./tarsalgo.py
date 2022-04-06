print("1.Feladat")
adatok = []

with open("ajto.txt", 'r') as File:
    for line in File.readlines():
        each = line.split()
        adatok.append(
            {
                "hour": int(each[0]),
                "minute": int(each[1]),
                "id": int(each[2]),
                "direction": (each[3]),
            }
        )
print(adatok)

print("2.Feladat")
print("\n")

i = 0
n = len(adatok)
found = True
while i < n and found:
    if adatok[i]["direction"] == "be":
        print(adatok[i]["id"])
        found = False
    else:
        i = i + 1

found = True
ki = []
for adat in adatok:
    if adat["direction"] == "ki":
        ki.append(adat)
h = len(ki)
print(ki[h - 1]["id"])

print("3. Feladat")

print("4.Feladat")
be = set()
for adat in adatok:
    if adat["direction"] == "be":
        be.add(adat["id"])
    else:
        be.remove(adat["id"])
print(be)

print("5. Feladat")

bent = 0
maxbent = 0
i = 0
n = len(adatok)
while i < n:
    if adatok[i]["direction"] == "be":
        bent = bent + 1
        if bent > maxbent:
            maxbent = bent
    else:
        bent = bent - 1
    i = i + 1

i = 0
bent = 0
while i < len(adatok) and bent <= maxbent:
    if adatok[i]["direction"] == "be":
        bent = bent + 1
        if bent == maxbent:
            print(f"Például", adatok[i]["hour"], ":", adatok[i]["minute"], "-kor voltak a legtöbben a társalgóban.")
    else:
        bent = bent - 1
    i = i + 1

print("6.Feladat")
bekert = int(input("Adja meg a személy azonosítóját! "))

print("7.Feladat")

starts = []
ends = []
for a in adatok:
    if a["id"] == bekert:
        h = a["hour"]
        m = a["minute"]
        if a["direction"] == "be":
            starts.append(f"{h:02d}:{m:02d}")
        elif a["direction"] == "ki":
            ends.append(f"{h:02d}:{m:02d}")

i = 0
while i < len(starts):
    line = starts[i] + "-"
    if i < len(ends):
        line += ends[i]

    print(line)
    i += 1

print("8.Feladat")
i = 0
staying_minutes = 0

while i < len(starts):
    if i < len(ends):
        start_hour = int(starts[i].split(":")[0])
        start_minute = int(starts[i].split(":")[1])
        start_time = start_hour * 60 + start_minute

        end_hour = int(ends[i].split(":")[0])
        end_minute = int(ends[i].split(":")[1])
        end_time = end_hour * 60 + end_minute

        staying_time = end_time - start_time

        staying_minutes += staying_time

    i += 1

print(f"A(z) {bekert}. személy összesen {staying_minutes} percet volt bent" +
      (", a megfigyelés végén a társalgóban volt." if len(starts) != len(ends) else "")
      )
