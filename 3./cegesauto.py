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
