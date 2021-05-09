# Week 1 - Zach's Journey into Grid

My first week at Digital Crafts has been nothing short of awesome. I came into this class with zero previous coding knowledge and was pretty nervous on how things would go. I have already experienced the highs of seeing your code succeed, and the lows of spending countless hours of not understanding what on earth I've done wrong. The week of pre-class work I completed did help me better understand certain terms and navigation, and I am very thankful to have spent so much time memorizing and researching the information they gave us. I say that, because this first week of class was definitely an information overload. Although it was a lot, I can confidently say I have never been so passionate and determined to learn and succeed in my life! 

## Highs and Lows 

Apart from the basic class introductions and expectations, we spent most of the time this week setting up our systems, getting comfortable in the terminal and in git/Github, and learning the basics of Python. I feel that I understand and picked up quickly how to navigate and use the terminal and git/github, but Python has proven to be a worthy opponent of my patience. I am a very competitive person, so its hard to see other students quickly grasping concepts and finishing assignments before me. I am also stubborn in the fact that if I am struggling, I have to do whatever I can to figure it out on my own and never ask questions. I've learned that all that thinking has to go. My low this week was spending so much time trying to make my "tip calculator" pre-class assignment work in python, that it made me question if coding was something that I could be good at. Thankful, I put my pride to the side and got some help from a friend. I learned that my code was close, but I was just missing a few "+" signs that helped piece it all together. Seeing the calculator finally work was actually the spark that has me determined to continue and succeed.

My high for the week came these past two days where I've been working on the phonebook_app.py exercise. This exercise honestly started out rough where I barely knew where to begin. Thankfully I was able to meet up with some other students outside of class and they helped me get the exact outcome I was hoping for. 

After A LOT of trial and error, here is a snippet of what my first big python code looks like:

```python
cycle = True
# phonebook_dictionary = {}
phonebook_dictionary = {
    'Alice': '703-493-1834',
    'Bob': '857-384-1234',
    'Elizabeth': '484-584-2923',
    'James': '546-756-987',
    'Marge': '645-934-3425'
}
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
```

I first completed the dictionary as being completely empty because I kept getting error messages when I tried to run the program. I made it to where the user needed to put in a contact first in order to see any output at all. My system worked! But I wasn't satisfied with it. The previous code can be seen in my comments within the code. After meeting up with other students on Saturday, I was able to correctly insert contacts into the dictionary and add line 54 that saved new contacts in the same dictionary. I really like that look that you see in the terminal when you run the program and you can see that below:

```python
Electronic Phone Book
---------------------
1. Look up an entry
2. Set a new entry
3. Delete an entry
4. List all entries
5. Quit

What do you want to do (1-5)? 4

{'Alice': '703-493-1834', 'Bob': '857-384-1234', 'Elizabeth': '484-584-2923', 'James': '546-756-987', 'Marge': '645-934-3425'}


Electronic Phone Book
---------------------
1. Look up an entry
2. Set a new entry
3. Delete an entry
4. List all entries
5. Quit

What do you want to do (1-5)? 2
New name: Zach
New phone number: 123-456-789

New entry, Zach, has been stored.


Electronic Phone Book
---------------------
1. Look up an entry
2. Set a new entry
3. Delete an entry
4. List all entries
5. Quit

What do you want to do (1-5)? 3
Name to delete info: Alice

Alice was deleted.


Electronic Phone Book
---------------------
1. Look up an entry
2. Set a new entry
3. Delete an entry
4. List all entries
5. Quit

What do you want to do (1-5)? 5

Thank you for using Zach's Phonebook Directory
```

## Conclusion

To wrap things up, I am really proud of what I have learned and created so far and I cant wait to see whats next!