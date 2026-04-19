def checker():
    number = int(input("Enter the number: "))
    if number > 0:
        print("Positive number")
    elif number < 0:
        print("Negative number")
    else:
        print("The number is zero")
    

    if number != 0:
        num = abs(number)
        if num%2 == 1:
            print("The number is odd")
        else: 
            print("The number is even")
    else:
        print("The number is even")

caller = str(input("Want to check the number? YES / NO:"))
if caller == "YES":
    checker()
