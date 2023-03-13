
# Find the numbers plus or minus
# Task 10

def find_plus_minus(a,b):
    if a<0 and b<0:
        print('Both are negative')

    elif a>0 and b>0:
        print('Both are postitive')

    else:
        print('One of them is postive the other is negative')

find_plus_minus()


#Task 11
# Find sum of digits

def sum_numbers(a,b,c):
    print(a+b+c)

sum_numbers()


#Task 12
# Find days of week

def find_days(day):
    if day == 1:
        print('Monday')
    elif day == 2:
        print('Tuesday')

    elif day == 3:
        print('Wednesday')

    elif day == 4:
        print('Thursday')
    
    elif day == 5:
        print('Friday')

    elif day == 6:
        print('Saturday')

    elif day == 7:
        print('Sunday')

    else:
        print('There are seven days in week')

find_days()


# Task 13
def check_units_equals_tens(num):
    if num < 10 or num > 99:
        print(" Number should be 2 digits")
    elif num % 11 == 0:
        print("yes")
    else:
        print("no")

#Task 14
def check_units_equals_hundreds(num):
    if num < 100 or num > 999:
        print("Number should be 3 digits")
    elif num % 100 == num // 100:
        print("yes")
    else:
        print("no")



# Task 15
def check_units_equals_tens(num):
    if num < 1000 or num > 9999:
        print("Number should be 4 digits")
    elif num % 100 == num // 10 % 10:
        print("yes")
    else:
        print("no")

        


