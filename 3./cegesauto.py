print("1. feladat")

cars = []

with open("autok.txt", "r") as file:
    for line in file.readlines():
        data = line.split()
        cars.append(
            {
                "day": int(data[0]),
                "time": data[1],
                "plate": data[2],
                "id": int(data[3]),
                "km": int(data[4]),
                "drive_in": int(data[5]),
            }
        )

print("\n")
print("2. feladat")

i = len(cars) - 1
while i >= 0:
    if cars[i]["drive_in"] == 0:
        last_day = cars[i]["day"]
        last_plate = cars[i]["plate"]
        print(f"{last_day}. nap rendszám: {last_plate}")
        break
    i -= 1

print("\n")
print("3. feladat")

day_in = int(input("Nap: "))
print(f"Forgalom a(z) {day_in}. napon:")

traffic = []
for car in cars:
    if car["day"] == day_in:
        traffic.append(car)

# 12:50 CEG303 561 ki
for car in traffic:
    if car["drive_in"] == 1:
        in_out = "be"
    else:
        in_out = "ki"

    print(car["time"], car["plate"], car["id"], in_out)

print("\n")
print("4. feladat")

car_out = set()

for car in cars:
    if car["drive_in"] == 0:
        car_out.add(car["plate"])
    else:
        car_out.remove(car["plate"])

print(f"A hónap végén {len(car_out)} autót nem hoztak vissza.")

print("\n")
print("5. feladat")

minimums = {}
maximums = {}

for car in cars:
    plate = car["plate"]
    km = car["km"]

    if plate not in minimums:
        minimums[plate] = km

    maximums[plate] = km

for key in maximums.keys():
    diff = maximums[key] - minimums[key]
    print(f"{key} {diff} km")

print("\n")
print("6. feladat")

# 1. külső ciklus amíg végig nem érek X
# 2. belső ciklus amíg ugyan az az autó, ugyan az az ember és bejövő
# 3. különbség számítása
# 4. ha a max érték kisebb mint a jelenlegi különbség akkor max = jelenlegi

maximum_km = 0
maximum_person = ""

i = 0
n = len(cars)
while i < n:
    actual_car = cars[i]

    if actual_car['drive_in'] == 0:
        j = i + 1

        found = False
        while j < n and not found:
            if cars[j]['plate'] == actual_car['plate'] \
                    and cars[j]['id'] == actual_car['id'] \
                    and cars[j]['drive_in'] == 1:
                found = True
                diff = cars[j]['km'] - actual_car['km']
                if diff > maximum_km:
                    maximum_km = diff
                    maximum_person = cars[j]['id']
                    max_pair = (actual_car, cars[j])

            j += 1

    i += 1

print(f"Leghosszabb út: {maximum_km} km, személy: {maximum_person}")

print("\n")
print("7. feladat")

plate_in = input("Rendszám: ")

with open(f"{plate_in}_menetlevel.txt", "w") as file:
    for car in cars:
        if car['plate'] == plate_in:
            id = car['id']
            day = car['day']
            time = car['time']
            km = car['km']

            write_out = f"{id}\t{day}. {time}\t{km} km"

            if car['drive_in'] == 0:
                write_out += "\t"
            else:
                write_out += "\n"

            file.write(write_out)

print("Menetlevél kész.")
