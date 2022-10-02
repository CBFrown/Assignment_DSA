def linearSearch(arr,n,k):
    for i in range(0,n):
        if(arr[i] == k):
             return i
    return -1
             
def BinarySearch(arr,k,low,high):
    if high >= low:
        mid = low + (high - low)//2
        if arr[mid] == k:
             return mid
        elif arr[mid] > k:
            return BinarySearch(arr,k,low,mid-1)
        else:
            return BinarySearch(arr,k,mid + 1,high)
    else:
        return -1
        
def selection_sort(ml):
    il = range(0, len(ml)-1)
    for i in il:
        mv = i
        for j in range(i+1,len(ml)):
            if ml[j] < ml[mv]:
                mv = j
        if mv != i:
            ml[mv], ml[i] = ml[i], ml[mv]
    return ml
    
yy = []
for i in range(10):
    tt = input("Input names:")
    yy.append(tt)

uuu =input("A: SORT B: SEARCH ")
if uuu == 'A' or uuu == 'a':
    print(selection_sort(yy))
    
if uuu == 'B' or uuu == 'b':
    k = str(input("search "))
    arr = list(map(str, yy))
    n = len(arr)
    result = linearSearch(arr, n, k)
    resulta = BinarySearch(arr, k, 0, len(arr) - 1)
    ttl = len(arr)
    print("Element found at index: ", result)
    print(arr)
