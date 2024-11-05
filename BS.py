def binary_search(arr, l, r, target):
    if l > r:
        return -1
    mid =int((l + r) / 2)
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, l, mid - 1, target)
    else:
        return binary_search(arr, mid + 1, r, target)


arr = eval(input("Enter Array:"))
if(len(arr)==0):
    print("Error:Input Array is empty")
    exit()
target = eval(input("Enter target:"))
result = binary_search(arr, 0, len(arr) - 1, target)
if result != -1:
    print(result)
else:
    print("Target is not present in array")
