file = open("teams.txt", "w")

file.write("lakers\n",)
file.write("man utd\n")
file.write("man city\n")
file.write("arsenal\n")
file.write("liverpool\n")

file = open("teams.txt", "r")
for line in range (5):
    if line == 0:
        print(file.readline())
    elif line == 3:
        print(file.readline())
    else:
        file.readline()


file.close()
