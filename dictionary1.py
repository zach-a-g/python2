meal = {
    "entree": "pesto chicken",
    "drink": "aha water",
    "dessert": "ice cream",
    #take out dessert to see comments below work
}
# print(meal["dessert"])
# print("Tonight I will have %s for dinner, with %s for dessert!" % (meal["entree"], meal["dessert"]))
# print("Tonight I will have " + meal["entree"] + " for dinner, with " + meal["dessert"] + " for dessert!")

# If the KEY "dessert" is found in the dictionary meal
# THEN, print the first statement
# If NOT, THEN print the second statement

# if "dessert" in meal:
#    print("OF COURSE Sean had dessert!!")
#else:
#    print("Sean did NOT have dessert, and now he is sad")

print(meal)

# Add a NEW key called "Appetizer", with the value "bacon"
meal["appetizer"] = "bacon"

# Update the key "drink", with the value "sweet tea"
meal["drink"] = "sweet tea"

# Delete an entry by referencing its key
del meal["dessert"]

print(meal)