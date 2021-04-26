#Take input from user for leap year
leapYearInput = int(input("Please input a year \n"))
#base case for only positive integers
while(leapYearInput < 0):
    print("Invalid input, try again")
    leapYearInput = int(input("Please input a year \n"))
if(leapYearInput%4==0):
    if(leapYearInput%100 != 0):
        if(leapYearInput%400 !=0):
            print("Leap Year!")
        else: 
            print("Not a leap year!")
    else:
        print("Leap year!")
else:
    print("Not a leap year!")