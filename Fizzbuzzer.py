#The first way of doing the thing:
'''for x in range(1,101):
    if x % 3 == 0:
        div3 = 1
    else:
        div3 = 0

    if x % 5 == 0:
        div5 = 1
    else:
        div5 = 0
    
    if x % 15 == 0:
        div15 = 1
    else:
        div15 = 0
    
    if div15 == 1:
        print "fizzbuzz"
    elif div3 == 1:
        print "fizz"
    elif div5 == 1:
        print "buzz"
    else:
        print str(x)'''

#The second way of doing the thing:
'''for x in range(1, 101):
    if x % 3 == 0:
        if x % 5 == 0:
            print str(x) + " fizzbuzz"
        else:
            print str(x) + " fizz"
    else:
        if x % 5 == 0:
            print str(x) + " buzz"
        else:
            print str(x)'''
