def quickSort(arr, low, high):
    if low < high:
        index = partition(arr, low, high)

        quickSort(arr, low, index - 1)
        quickSort(arr, index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

arrStr = input("Enter a list of number(Use ',' as separator): ")
arrlist = arrStr.split(",")
arrMap = map(int, arrlist)
arr = list(arrMap)
print("Input Array: " , arr)
#arr = [10, 1, 3, 4, 12, 6, 7, 2]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted Array: " , arr)
