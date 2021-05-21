def leap(number):
    if(number < 0):
        return "Invalid input"
    if(number%4==0):
        if(number%100 != 0):
            if(number%400 !=0):
                return "Leap Year!"
            else: 
                return "Not a leap year!"
        else:
            return "Leap year!"
    else:
        return "Not a leap year!"