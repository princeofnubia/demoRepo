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




