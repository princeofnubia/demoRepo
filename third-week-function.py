# Guessing machine
# I take a guess on values within three
# tries
import copy
def guess():
    number_of_tries = 0
    # inner function definition
    def run_guess(no_of_tries):
        MAGIC_NUMBER = 5 # declaration an Integer
        my_guess = int(input("Please enter your guess: ")) #casting to integers
        if(my_guess == MAGIC_NUMBER): #
            print('Yay you Won')
        else:
            no_of_tries = no_of_tries + 1
            if no_of_tries == 3:
                print('Game Over!') # base case
            else:
                run_guess(no_of_tries) #recursive case
    return run_guess(number_of_tries)

def faulty_guess(no_of_tries = 0):
    MAGIC_NUMBER = 5 # declaration an Integer
    my_guess = int(input("Please enter your guess: ")) #casting to integers
    if(my_guess == MAGIC_NUMBER): #
        print('Yay you Won')
    else:
        no_of_tries = no_of_tries + 1
        if no_of_tries == 3:
            print('Game Over!') # base case
        else:
            faulty_guess(no_of_tries) #recursive case
# recursion
def factorial(n):
    if (n == 1): #base case
        return 1
    else: # recursive case
        print('value of n: ', n)
        return n * factorial(n-1)

#factorial(8) =
#       8 * factorial(7) =
#       8 * 7 * factorial(n = 6) =
#       8 * 7 * 6 * factorial(n = 5) =
#       8 * 7 * 6 * 5 * factorial(n = 4) =
#       8 * 7 * 6 * 5 * 4 * factorial(n = 3) =
#       8 * 7 * 6 * 5 * 4 * 3 * factorial(n = 2) = 
#       8 * 7 * 6 * 5 * 4 * 3 * 2 * factorial( n = 1) =
#       8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 = total
#factorial(7) = 7 * 6 * 5 * 4 * 3 * 2 * 1

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def get_total(scores):
    total_sum = 0
    for value in scores:
        print("current sum: ", total_sum)
        print("current value: ", value)
        total_sum = total_sum + value
    print("Final sum: ", total_sum)
    return total_sum
def reverse_list(my_list):
    # Get the length of the list
    # loop from highest index down to the zero index
    # get the value at index and push it to a list
    # when done return it
    list_length = len(my_list) # get the length
    new_list = copy.copy(my_list) # we did a shallow copy we are not copying the reference as it was causing mutation
    for i in range(list_length):
        last_index = list_length - (1 + i)
        print("Lst_index: ", last_index)
        print(" value of I: ", i)
        new_list[i] = my_list[last_index] # side effect
    return new_list


def reverse_list_another(my_list):
    # Get the length of the list
    # loop from highest index down to the zero index
    # get the value at index and push it to a list
    # when done return it
    list_length = len(my_list) # get the length
    new_list = []
    for i in range(list_length):
        last_index = list_length - (1 + i)
        print("Lst_index: ", last_index)
        print(" value of I: ", i)
        new_list.append(my_list[last_index]) # side effect
    return new_list

def reverse_list_simple(my_list):
    list_length = len(my_list) # get the length
    even_dividend = list_length #
    for i in range(even_dividend): #breaking out of the loop
        swap_index = list_length - (1 + i)
        swap_value = my_list[swap_index]
        first_index = i
        first_value = my_list[i]
        my_list[first_index] = swap_value
        my_list[swap_index] = first_value
    return my_list #runs after we break out of the loop


def reverse_recursive(my_list):
    pass


# Assignment for the third week friday

# Your function should do just one thing not several things at a time
def calculate_sum(the_list):
    total_sum = 0
    for each_number in the_list:
        total_sum = total_sum + each_number
    return total_sum

def calculate_mean(a_list):
    # re using the calculate_sum function to get the sum of the list items
    total_sum = calculate_sum(a_list)
    length_of_list  = len(a_list)
    mean = total_sum/length_of_list
    return mean

