ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ],
}

# Write a python expression that gets the email address of Ramit.
print(ramit["email"])
print("-----")
# Write a python expression that gets the first of Ramit's interests.
print(ramit["interests"][0]) # 0 because the list starts at 0
print("-----")
# Write a python expression that gets the second of Jan's two interests.
print(ramit["interests"][1]) # 1 because the list starts at 0
print("-----")
                # Write a python expression that gets the email address of Jasmine.
                #print(ramit["friends"]["email"]["jasmine@yahoo.com"])?????????????????
print("-----")
# Write a function countFriends() that accepts a dictionary as an argument and returns a new dictionary that includes a new key friends_count:
ramit["friends_count"] = "2"
print(ramit["friends_count"])
print("-----")

print(ramit)


