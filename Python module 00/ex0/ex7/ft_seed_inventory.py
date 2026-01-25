def ft_seed_inventory(seed_type: str, quantity: int, unit: str):
    if (unit == "packets"):
        print(f"{seed_type}: {quantity} {unit} available")
    elif (unit == "grams"):
        print(f"{seed_type}: {quantity} {unit} total")
    elif (unit == "area"):
        print(f"{seed_type}: {quantity} {unit} square meters")
    else:
        print("Unknown unit type")
