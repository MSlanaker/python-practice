name_list = ["Matthew", "Carly", "Anna", "Spencer"]

print(name_list)

if len(name_list) > 3:
    print("The room is crowded")


name_list.remove("Spencer")
name_list.remove("Anna")

print(name_list)

if len(name_list) > 3:
    print("The room is crowded")


def crowded(list):
    if len(list) > 3:
        print("The room is crowded")
    else:
        print("The room is NOT very crowded")


crowded(name_list)

name_list.append("Spencer")
name_list.append("Anna")
name_list.append("Katie")
name_list.append("Robb")

print(name_list)


def check_crowd(list):
    if len(list) > 5:
        print("There's a mob in the room")
    elif len(list) >= 3 and len(list) <= 5:
        print("The room is crowded.")
    elif len(list) >= 1 and len(list) <= 2:
        print("The room is not crowded.")
    elif len(list) == 0:
        print("The room is empty.")


check_crowd(name_list)
