def linearSearch(arr,n,k):
    # Going through array sequencially
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




while True:
    print("Input numbers to be sorted separated by a space:")
    print("i.e. 1 2 3 4")
    arr = list(map(int, input("Type in here:   ").split()))
    ttl = len(arr)
    k = int(input("search "))
    n = len(arr)
    result = linearSearch(arr, n, k)
    resulta = BinarySearch(arr, k, 0, len(arr) - 1)
    if ttl >= 21:
        print("Max input 10")
        break

    else:
        if resulta != -1:
            print("Element is present at index " + str(resulta))
        else:
            print("Element found at index: ", result)
    break