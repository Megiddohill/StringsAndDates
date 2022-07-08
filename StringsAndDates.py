# David Prato
# CIS 261
# Strings and Date

date = input("Enter a Date in Month DD, YYYY Format: ")
while date != '-1': #This will cause the loop to loop until -1
    parts = date.split() # Splits the string into sub-strings
    month = parts[0] 
    if month == 'January':
        month_int = 1
    elif month == 'February':
        month_int = 2
    elif month == 'March':
        month_int = 3
    elif month == 'April':
        month_int = 4
    elif month == 'May':
        month_int = 5
    elif month == 'June':
        month_int = 6
    elif month == 'July':
        month_int = 7
    elif month == 'August':
        month_int = 8
    elif month == 'September':
        month_int = 9
    elif month == 'October':
        month_int = 10
    elif month == 'November':
        month_int = 11
    elif month == 'December':
        month_int = 12
    else:
        month_int = 0 # The transformation of char to int occurs here

    if len(parts) >= 3 and month != 0: # parts must in 3 parts and month can't be "0"
        day = parts[1] #The second index where the "DD," section is
        if day[len(day) -1] == ',': #This checks the last index of the day variable, where the "," will be
            day = day[0:len(day)-1] #This substracts the last index from the "day" variable
            year = parts[2] #year section of substrings
            print(str(month_int) + '/' + day + '/' +str(year)) # Prints if all conditions are met
        else:
            print("Date is invalid, Enter: Month DD, YYYY")
    else:
        print ("Date is invalid, EnterL Month DD, YYYY")
    date = input ("Enter a Date in Month DD, YYYY Format: ") # starts loop again
