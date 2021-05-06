marvel_heros = []
marvel_heros.append("Ironman")
marvel_heros.append("Spiderman")
marvel_heros.append("Thor")
marvel_heros.append("Hulk")
marvel_heros.append("Captain America")

# print(marvel_heros[2])

index = 0

#print(len(marvel_heros))

# Here is my WHILE loop
# It starts at index 
# and finishes at the end of the list
print("------WHILE LOOP------")
while index < len(marvel_heros):
    print(marvel_heros[index])
    index = index + 1

# Here is the FOR loop
print("------FOR------")
for heros in marvel_heros:
    print(heros)



# FOR every single item that I am calling HEROS,
# that exists in my COLLECTION OF ITEMS, called MARVEL_HEROS
# PRINT that SINGLE ITEMS'S VALUE


