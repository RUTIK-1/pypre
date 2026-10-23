#
# with open("1.py", "r") as file:
#    content = file.read()

#print(content)



error_count = 0

try:
    with open("app.log", "r") as file:
        for line in file:
            if "ERROR" in line:
                print(line)
                error_count += 1

    print("Total errors:", error_count)

except FileNotFoundError:
    print("Error: app.log not found")