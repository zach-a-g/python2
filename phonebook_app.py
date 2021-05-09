# print("""
# Electronic Phone Book
# =====================
# 1. Look up an entry
# 2. Set an entry
# 3. Delete an entry
# 4. List all entries
# 5. Quit
# """)

cycle = True

# Started dictionary being empty (phonebook_dictionary{}),
# but then added names & numbers as a starting point.
phonebook_dictionary = {
    'Alice': '703-493-1834',
    'Bob': '857-384-1234',
    'Elizabeth': '484-584-2923',
    'James': '546-756-987',
    'Marge': '645-934-3425'
}

# Kept menu inside of the WHILE loop so it would always
# be printed after a completed command.
while cycle == True:
    print("""
Electronic Phone Book
---------------------
1. Look up an entry
2. Set a new entry
3. Delete an entry
4. List all entries
5. Quit
""")
  
    user_input = int(input("What do you want to do (1-5)? "))

# Looking up an entry
    if user_input == 1:
        name = input("Name: ")
        names_found = []
        if name in phonebook_dictionary:
            #names_found.append(name)
            #print("Found entry for %s: %s:" % (name, phonebook_dictionary[name]["phone_number"]))
            print("")
            print("Name: " + name + " Phone Number: " + phonebook_dictionary[name])
            print("")
        else:
            print("")
            print(name + " not found.")
            print("")

# Setting a new entry
    elif user_input == 2:
        name = input("New name: ")
        phone_number = input("New phone number: ")
        #phonebook_dictionary[name] = 
            #"phone_number": phone_number
        phonebook_dictionary[name] = phone_number
        print("")
        print("New entry, " + name + ", has been stored.")
        print("")

# Deleting an entry
    elif user_input == 3:
        name = input("Name to delete info: ")
        if name in phonebook_dictionary:
            del phonebook_dictionary[name]
            print("")
            print(name + " was deleted.")
            print("")
        else:
            print("")
            print("Name was not found")
            print("")

# Listing all entries
    elif user_input == 4:
        print("")
        print(phonebook_dictionary)
        print("")
         

# Quitting the menu
    elif user_input == 5:
        print("")
        print("Thank you for using Zach's Phonebook Directory")
        print("")
        cycle = False