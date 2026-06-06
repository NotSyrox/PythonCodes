strs = input("Enter Three names (Separeted by spaces): ")

names = strs.split(" ")


for i, name in enumerate(names):
    print(f"Name{i+1}: {name}")