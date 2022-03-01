from typing import List, Dict, Set, Tuple

# Változók

# Egy soros komment

"""
Több
soros
komment
"""

variable = 1
long_variable = 2
CONSTANT = 3

# alap típusok
egesz: int = 1
tort: float = 1.0
szoveg: str = "szoveg"
logikai: bool = True

"""
egeszbol ->
str(egesz)
float(egesz)

tortbol ->
int(tort)
str(tort)
"""

"""szoveg konkatenacio"""
szoveg_2: str = "a" + "b " + str(egesz)
print(szoveg_2)

mondat: str = "a macska fel van maszva a fara"
szavak: List[str] = mondat.split()
print(szavak)

mondat = "a macska fel, van maszva a fara"
szavak = mondat.split(",")
print(szavak)

"""
uj sor karakter \n
"""

# adatszerkezetek
lista: List = ["a", 1, "b"]
dictionary: Dict = {
    "kulcs_1": 1,
    "kulcs_2": 2,
}
halmaz: Set = set("a")
n_es: Tuple = ("a", "b")

lista.append(2)
print(lista)
print("index: " + str(lista.index("b")))

# if - else- elif

"""
if True/1/["a"] (and) (or) ([not] in):
    pass
elif True:
    pass
elif True:
    pass
elif True:
    pass
else:
    pass
"""

# ciklusok
for i in range(0, 5):
    print(i)

for index, i in enumerate(range(0, 5)):
    print(index, i)

while True:
    print("a")
    break

# break, continue, (return)
for i in range(0, 5):
    if i == 2:
        continue  # kihagy egy kört
    elif i == 3:
        print("három")
        break  # kilép a ciklusból
    else:
        print(i)

# I/O
"""
f = open("demofile.txt", "w")
f.close()
"""

with open("demofile.txt", "w") as file:
    file.write("testline")
    file.write("2\n")
    file.write("kiskutya")


with open("demofile_2.txt", "r") as file:
    # print(file.read())
    """for text in file.read():
        print(text)"""
