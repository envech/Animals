class Animal:
    def __init__(self, name, genus, year_of_birth, region):
        self.name = name
        self.genus = genus
        self.year_of_birth = year_of_birth
        self.region = region
    def get_age(self, year):
        return year - self.year_of_birth
    def get_info(self):
        return f"{self.name} is a {self.genus}"
    def get_region(self):
        return f"{self.region} a habitat of {self.genus}"
def find_oldest_animal(animals):
    oldest_animal = None
    max_age = -1
    for animal in animals:
        age = animal.get_age(year)
        if age > max_age:
            max_age = age
            oldest_animal = animal
        return oldest_animal
animals = [
    Animal("Dumbo", "elephant", 2008, "Asia"),
    Animal("Kaa", "python", 2021, "South America"),
    Animal("Lucky", "dog", 2017, "Europe"),
    Animal("Tulu", "giraffe", 2019, "Africa"),
]
year = 2024
for animal in animals:
    print(animal.get_info())
    print(f"Age in {year}: {animal.get_age(year)} years")
    print(f"{animal.get_region()}")
oldest_animal = find_oldest_animal(animals)
if oldest_animal:
    print(f"The oldest animal is {oldest_animal.name}, a {oldest_animal.genus}, aged {oldest_animal.get_age(year)} years.")
with open("animals.txt", "w") as file:
    for animal in animals:
        file.write(f"{animal.name} is a {animal.genus}\n")
