import random as r

unsorted = [r.randint(0,50) for i in range(0,15)]   #Target list
pivot = unsorted[r.randint(0,len(unsorted)-1)]      #pivot for splitting list
sList = unsorted[pivot:]                            # list of smaller values (left of pivot)
bList = unsorted[:pivot]                            # list of bigger values (right of pivot)

print(unsorted)
print("PIVOT IS:", pivot)

sIndex = 0      #declaring variables that need to be global
small = 0
bIndex = 0
big = 0
sListDone = False
bListDone = False

while sListDone != True or bListDone != True:
    sList = unsorted[pivot:]
    bList = unsorted[:pivot]
    for i in range (0, len(sList)):
        if sList[i] > pivot:
            small = sList[i]
            sIndex = i
            print("s", small)
            break
        else:
            sListDone = True

    for y in range (0, len(bList)):
        if bList[y] < pivot:
            big = bList[y]
            bIndex = y
            print("b", big)
            break
        else:
            bListDone = True
    unsorted[sIndex] = big
    unsorted[bIndex+len(sList)] = small

    #print(big, "Is the big value that has been swapped with", small)