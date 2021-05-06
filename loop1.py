title = "Rocket League"
# STOP = 10
counter = 0

while counter < len(title):
    print("The counter value is: " + str(counter))
    if (counter % 2) == 0 and title[counter] != " ":
        print(title[counter])
    counter = counter + 1
