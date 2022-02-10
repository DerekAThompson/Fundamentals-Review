def GetElement(arr, key):
        lenArr = int(len(arr) / 2)
        pivot = findPivot(arr, 0, lenArr - 1)





def findPivot(arr, low, high):
    if high < low:
        return -1
    if high == low:
        return low
























print(GetElement([5, 6, 7, 8, 9, 10, 1, 2, 3], 3))