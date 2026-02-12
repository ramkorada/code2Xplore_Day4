lists = input("Enter elements separated by space: ").split()

number = []
string = []

numberCount = 0
stringCount = 0

name = input("Enter Your Name: " )

for i in range(len(lists)):
    if lists[i] == "":
        continue

    if lists[i].isdigit():
        number = number + [int(lists[i])]
        numberCount = numberCount + 1
    else:
        string = string + [lists[i]]
        stringCount = stringCount + 1

name_length = len(name)

if name_length % 2 == 0:
    if len(number) > 0:
        number = number[1:]
    if len(string) > 0:
        string = string[1:]
else:
    if len(number) > 0:
        number = number[:-1]
    if len(string) > 0:
        string = string[:-1]

print("Numbers List:", number)
print("Strings List:", string)
print("Total Numbers:", numberCount)
print("Total Strings:", stringCount)
