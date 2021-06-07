#Question 3
import datetime
now=datetime.datetime.now()
print("Current date and time:",now)
#Question 6
def values():
    values=input("Input numbers seperated by a comma: ")
    lis=values.split(",")
    tup=tuple(lis)
    print("list :",list)
    print("Tuple :",tuple)
    
#Question 9
def exam_st_date(date,month,year):
    print("The examination will start from:{0}/{1}/{2} ".format (date,month,year))


#Question 15
def volume_of_sphere():
    pi=3.14
    radius=input("The radius of the sphere is: ")
    volume=4.0/3.0*pi*int(radius)**3
    print("The volume of the sphere is: ",volume)
#Question 17
def near_thousand():
    n=int(input("The number is: "))            
    return((abs(1000-n)<=100) or (abs(2000-n)<=100))

    
#Question 18
def sum_numbers(x,y,z):
    sump=x+y+z
    if x==y==z:
        sump=sump*3
    return sump




