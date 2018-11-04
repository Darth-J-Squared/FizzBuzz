import numbers
print "Ready for FizzBuzz?"
raw_input("Press enter to continue...")
x = 0
def c():
    global x
    x += 1
    if x == 101:
        print "All done"
    elif x % 3 == 0:
        if x % 5 == 0:
            print "FizzBuzz"
            c()
        else:
            print "Fizz"
            c()
    elif x % 5 == 0:
        print "Buzz"
        c()
    else:
        print x
        c()
c()
