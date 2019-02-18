#!/opt/local/bin/python

import sys

dicetotal = int(sys.argv[1])
numberkept = int(sys.argv[2])
target = int(sys.argv[3])

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

best=choosemax(rolls[dicetotal], numberkept)
results=[]
for x in best:
    results.append(sum(x))

results.sort()
#print results

successcount=0

for x in results:
    if x >= target:
        successcount=successcount+1

#print str(successcount)+"/"+str(len(results))+" ("+str(int(successcount/float(len(results))*100))+"%) rolls of "+sys.argv[1]+" dice keeping "+sys.argv[2]+" are at least "+sys.argv[3]
#print choosemax(rolls[dicetotal], numberkept)
#print rolls[dicetotal]

#choose to reach target
def choosetarget(allrolls, number, target):
    choices=[]
    for x in allrolls:
        pool=list(x)
        z=[]
        #print "my options are"
        #print pool
        #print "and i'm trying to get to " + str(target)

        for y in range(0,number):
            #print z
            if sum(z)<target:
                #print str(sum(z)) + " is less than my target so i'm picking " + str((pool[-1:].pop()))
                z.append(pool[-1:].pop())
                del pool[-1:]
            elif sum(z)>target:
                #print str(sum(z)) + " is more than my target so i'm picking " + str((pool[:1].pop()))
                z.append(pool[:1].pop())
                del pool[:1]
            else:
                #print "at my target, there are " + str(number-y) + " choices left, and the remaining options are"
                #print pool
                if (number-y)>=2 and pool.count(-1) and pool.count(1):
                    #print "I'm at my target and there are 2 choices left and a matched pair, so i'm picking " + str((pool[:1].pop()))
                    z.append(pool[:1].pop())
                    del pool[:1]
                elif pool.count(0):
                    #print "I'm at my target and can't find a matched pair, so i'm picking 0"
                    #print pool
                    z.append(0)
                    pool.remove(0)
                else:
                    #if not pool[0:]:
                    #    print pool
                    #print "I'm at my target but there are no good options, so i'm picking " +  str((pool[:1].pop()))
                    z.append(pool[:1].pop())
                    del pool[:1]
        #z.remove(0)
        #print "i ended up picking"
        #print z
        choices.append(z)
        #print
    return choices

closest=choosetarget(rolls[dicetotal], numberkept, target)
#print rolls[dicetotal]
#print closest

closestresults = []
for x in closest:
    closestresults.append(sum(x))

#print closestresults
#print closest

closestresults.sort()
#
equalcount=0
for x in closestresults:
    if x == target:
        equalcount=equalcount+1

print str(equalcount)+"/"+str(len(results))+" ("+str(int((equalcount/float(len(results)))*100))+"%) rolls of "+sys.argv[1]+" dice keeping "+sys.argv[2]+" can be equal to "+sys.argv[3]
#
