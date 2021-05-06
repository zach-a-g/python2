#1. Sum the Numbers
#Create a list of numbers, print their sum.

# random numbers
list_of_numbers = [123,456,789]
#positive_numbers.append[]
# print(sum(list_of_numbers))

total = 0

#for number in list_of_numbers:
 #   print("The number is now: " + str(number))
  #  total = total + number
   # print("The total is now: " + str(total))

# Largest number
largest = list_of_numbers[0]
for number in list_of_numbers:
   if number > largest:
       largest = number
print("The largest number is: " + str(largest))

# Smallest number
smallest = list_of_numbers[0]
for number in list_of_numbers:
   if number < smallest:
       smallest = number
print("The largest number is: " + str(smallest))

#Even numbers
print("Number 4: ")
