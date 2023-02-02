from utils import start_section

# List (sequence of mutable values)
start_section("List")
names = ["Pepe", "Pedro", "Pelayo", "Petra"]
print(names)
print(names[0])

# Mutate the list
names.append("Peyo")
names[2] = "Peter"
names.sort()
print(names)
print(f"List has {len(names)} elements")


# Tuple (sequence of inmutable values)
start_section("Tupple")
coordinates = (0.0, 1.4)
print(f"X: {coordinates[0]}")
print(f"Y: {coordinates[1]}")

# Not mutable
# coordinates[0] = 10 -> TypeError: 'tuple' object does not support item assignment
print(f"Tuple has {len(coordinates)} elements")

# Set (collection of unique values)
start_section("Set")
s = set()
s.add("lechuga")
s.add("patata")
s.add("rábano")
s.add("col")
s.add("patata")
s.remove("col")
print(s)
print(f"Set has {len(s)} elements")

# Dict (collection of key-value pairs)
start_section("Dict")
ages = {
    "Pepe": 54,
    "Pedro": 34,
    "Pelayo": 72
}
print(ages)
print(f"Pepe's age: {ages['Pepe']}")
print(f"Dictionary has {len(ages)} elements")

# Mutate the dict
ages["Peyo"] = 15
ages["Pepe"] = 10
print(ages)
