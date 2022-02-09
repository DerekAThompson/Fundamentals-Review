def BubbleSort(myList):
    for i in range(len(myList)):
        for y in range(len(myList)- i - 1):
            if myList[y] > myList[y + 1]:
                myList[y], myList[y + 1] = myList[y + 1], myList[y]
    return myList
            
print(BubbleSort([33, 72, 14, 51, 50, 30, -35, 22]))

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
