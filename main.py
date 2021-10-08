import random as r

unsorted = [r.randint(0,50) for i in range(0,15)]   #Target list
pivotIndex = len(unsorted) // 2
pivotVal = unsorted[pivotIndex]
#pivot = unsorted[r.randint(0,len(unsorted)-1)]      #pivot for splitting list
sList = unsorted[:pivotIndex]                            # list of smaller values (left of pivot)
bList = unsorted[pivotIndex:]                            # list of bigger values (right of pivot)

print(unsorted)
print(sList)
print(bList)
print("PIVOT IS:", pivotVal)

sIndex = 0      #declaring variables that need to be global
smallToBig = "null"
bIndex = 0
bigToSmall = "null"
sListDone = False
bListDone = False
i = 0
y = 0

while sListDone != True or bListDone != True:
    if smallToBig == "null":
        for i in range (i, len(sList)):
            if sList[i] > pivotVal:
                smallToBig = sList[i]
                sIndex = i
                print("s", smallToBig)
            elif i == len(sList):
                sListDone = True
    if bigToSmall == "null":
        for y in range (y, len(bList)):
            if bList[y] < pivotVal:
                bigToSmall = bList[y]
                bIndex = y
                print("b", bigToSmall)
            elif y == len(bList):
                bListDone = True
    unsorted[sIndex] = bigToSmall                  #swapping numbers
    unsorted[bIndex+len(sList)] = smallToBig
    #print(unsorted)
    #print(big, "Is the big value that has been swapped with", small)