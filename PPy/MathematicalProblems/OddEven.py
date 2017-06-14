val = input()
print(val)
if 1 <= val <= 100:
    if val % 2 == 0 and 2 <= val <= 5:
        print("Not Weird")
    elif val % 2 == 0 and 6 <= val <= 20:
        print("Weird")
    elif val % 2 == 0 and val > 20:
        print("Not Weird")
    elif bool(val & 1) is True:
        print("Weird")