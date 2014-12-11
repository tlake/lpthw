def while_loop(height, increment):
    i = 0
    numbers = []

    while i < height:
        print "At the top i is %d" % i
        numbers.append(i)

        i += increment
        print "Numbers now ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "

    for num in numbers:
        print num

while_loop(65, 8)


def for_loop(height, increment):
    numbers = []

    for i in range(0, height, increment):
        print "At top of loop, i is %d" % i
        numbers.append(i)

    print "The numbers: "

    for num in numbers:
        print num

for_loop(65, 8)
