rows = int(input("Enter rows: "))

for i in range(rows):
    print(" " * (rows - i - 1) + "* " * (i + 1))

for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "* " * i)
