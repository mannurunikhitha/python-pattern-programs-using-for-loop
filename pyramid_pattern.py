rows = int(input("Enter rows: "))

for i in range(rows):
    print(" " * (rows - i - 1) + "* " * (i + 1))
