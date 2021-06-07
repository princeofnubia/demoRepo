import random


l = [0, 1, 2, 3, 4]

print(random.choice(l))

#Write a Python program to get the Python version you are using.

import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)

#5. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
def login():
   user_firstname = input('Enter firstname:')
   user_lastname  = input('Enter lastname: ')
   print('Welcome {0} {1}').format(user_lastname, user_firstname)
   

#8. Write a Python program to display the first and last colors from the following list. color_list = ["Red","Green","White" ,"Black"]

def get_last_first_colors():
  color_list = ["Red","Green","White" ,"Black"]
  if (len(color_list) == 0):
    print("Empty data list") 
  else:
    for color in color_list:
      print("%s %s"%color[0], color[-1])
  #"%s %s"% used in place of format() for string formatting
  #else:
    #print("{0} {1}").format(len( color_list[0]), len( color_list)-1)

#10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# 
def compute_int():
  acc = int(input("Enter number here: "))
  n = int(input('{0}').format(acc))
  nn = int(input('{0}{1}').format(acc, acc))
  nnn = int(input('{0}{1}{2}').format(acc, acc, acc))
  return n + nn + nnn



#12. Write a Python program to print the calendar of a given month and year.

import calendar

y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y, m)) 