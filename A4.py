number = input("please enter the number to check : ")
def fizzBuzz (num):
    if (num % 5 == 0 and num % 3 == 0 ):
        print"fizzBuzz"
    elif (num % 5 == 0):
        print "buzz"
    elif (num % 3 == 0 ):
        print "fizz"
    else:
        print "you should enter a number divisible by 5 or 3 or both"

fizzBuzz(number)