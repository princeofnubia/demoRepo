##Quetsion 9#Question 1
def return_param(param):
    print("param_value", param)

def return_param(param):
    return param                   
#Question 2
def value():
    value=input("Enter a value: ")
    print(value)

#Question 3
def introduction():
    name = input('What is your name? ')
    age= input('How old are you? ')
    address = input('Where do you live? ')
    print("Your name is: ",name)
    print("Your age is: ",age)
    print("Your address is: ",address)
#Question 4
def check(s):
    first_name = input("What is your first name?")
    second_name = input("What is your second name?")
    print(first_name.isalpha())
    print(second_name.isalpha())
#Question 5
def l_count(param):
    count_of_l=0
    for i in param:
        if(i=="l"):
            count_of_l=count_of_l +1
            print("l appeared {0} times". format(count_of_l))
#Question 6
def is_numeric():
    username = input("What is your username?")
    print(username.isnumeric())

##Question 7
def checkdifference():
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    sump=a+b
    prod=a*b
    diff=prod-sump
    print("Difference of product and sum: ",diff)
#Question 8
def checknum ():
    num=int(input("Enter a number: "))
    if (num%2)==0:
        print("{0} is Even number". format(num))
    else:
        print("{0} is Odd number". format(num))
#Question 9
def introduce_yourself():
    name = input('What is your name? ')
    favorite_color = input('What is your favorite color? ')
    favorite_food = input('What is your favorite food? ')
    favorite_tv_show = input('What is your favorite tv show? ')
    favorite_song = input('What is your favorite song? ')
    print(f"Hey, my name is {name}! My favorite color is {favorite_color}. My favorite food is {favorite_food}. My favorite tv show is {favorite_tv_show}. My favorite song is {favorite_song}.")





