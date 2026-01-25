class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":
    Plant1 = Plant("Rose", 25, 30)
    Plant2 = Plant("Sunflower", 80, 45)
    Plant3 = Plant("Cactus", 15, 120)

    print(f"{Plant1.name}: {Plant1.height}cm, {Plant1.age} days old")
    print(f"{Plant2.name}: {Plant2.height}cm, {Plant2.age} days old")
    print(f"{Plant3.name}: {Plant3.height}cm, {Plant3.age} days old")
