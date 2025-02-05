names = set()

name = input("Enter a name or press enter to quit: ")

while name != "":
    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)
    name = input("Enter a name or press enter to quit: ")

print("\nList of names: ")
for name in names:
    print(name)









