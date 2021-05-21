# demoRepo

# Function week

1. Write a function that calculates the sum of a list items Ex [1,2,3,4,5,6,7,8] the sum = 36
2. Write a function that calculates the mean of a data Ex [1,2,3,4,5,6,7,8] the mean 36/8 = 4.5

def calculate_sum(the_list):
    total_sum=0
    for each_number in the_list:
        total_sum=total_sum+each_number
    return total_sum

def calculate_mean(the_list):
    total_sum=0
    for each_number in the_list:
        total_sum=total_sum+each_number
    length_of_list=len(the_list)
    mean=total_sum/length_of_list
    return mean

def calculate_mean(the_list):
    total_sum=calculate_sum(the_list)
    
    length_of_list=len(the_list)
    mean=total_sum/length_of_list
    return mean

# Assignment for the fourth week

1. Write function that prints what it is given as parameter
2. Write function that prompts the user to enter a value and print that value back
3. Write a function that asks the user for the following questions:
        1. What is your name?
        2. How old are you?
        3. Where do you live?
  Print back
        Your name is: [name provided by the user]
        Your age: [age provided in the input]
        address: [location provided in the input]
5. Write a function that detects if a letter is in a string e.g 

6. Write function that counts the number of times l appears in 
   the string  "lslaldjalasdasdlasdlasllllldlldasdaslllfsdlfsll"
   hints: a string behave just like a list, so use [for letter in range(len(the_string))]



7. Write a function that checks whether a number is in a string

8. Write a function that takes two numbers and return the difference between its product and sum

9. Write a function that checks whethe a number is even or odd

10. Write a function that tells me about who you are