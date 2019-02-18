#!/opt/local/bin/python

import sys

dicetotal = int(sys.argv[1])
numberkept = int(sys.argv[2])

#generate table up to where we need
def nextrolls(prevrolls):
    options=[-1, 0, 1]
    temp=[]

    if not prevrolls:
        for x in options:
            temp.append([x])
        return temp
    
    for x in prevrolls:
        for y in options:
            z=list(x)
            z.append(y)
            z.sort()
            temp.append(z)
    return temp

rolls=[]
rolls.append([])
for x in range(1, dicetotal+1):
    rolls.append(list(nextrolls(rolls[x-1])))

#choose most
def choosemax(allrolls, number):
    choices=[]
    for x in allrolls:
        z=x[-number:]
        choices.append(z)
    return choices

#choose to reach target
def choosetarget(allrolls, number, target):
    choices=[]
    for x in allrolls:
        pool=list(x)
        z=[]

        for y in range(0,number):
            if sum(z)<target:
                z.append(pool[-1:].pop())
                del pool[-1:]
            elif sum(z)>target:
                z.append(pool[:1].pop())
                del pool[:1]
            else:
                if (number-y)>=2 and pool.count(-1) and pool.count(1):
                    z.append(pool[:1].pop())
                    del pool[:1]
                elif pool.count(0):
                    z.append(0)
                    pool.remove(0)
                else:
                    z.append(pool[:1].pop())
                    del pool[:1]
        choices.append(z)
    return choices

print "TRG:  MEET | EQUAL"
for target in range(-numberkept, numberkept+1):

    best=choosemax(rolls[dicetotal], numberkept)
    results=[]
    for x in best:
        results.append(sum(x))
    results.sort()
    successcount=0
    for x in results:
        if x >= target:
            successcount=successcount+1

    closest=choosetarget(rolls[dicetotal], numberkept, target)
    closestresults = []
    for x in closest:
        closestresults.append(sum(x))
    closestresults.sort()
    equalcount=0
    for x in closestresults:
        if x == target:
            equalcount=equalcount+1

    print str(target).ljust(3) + ": " + str(int((successcount/float(len(results)))*100)).ljust(4) + "% | " + str(int((equalcount/float(len(results)))*100)).ljust(4) + "%"

