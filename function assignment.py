##lst=[]
##num=int(input("How many numbers: "))
##for n in range(num):
##    numbers=int(input("Enter number"))
##    lst.append(numbers)
##print("Sum of elements in given list is :", sum(lst))
##print("Mean of elements in given list is:", sum(lst)/num)
##
##def listsum(numList):
##    theSum = 0
##    for i in numList:
##        theSum = theSum + i
##    return theSum
##
##print(listsum([1,2,3,4,5,6,7,8]))


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
