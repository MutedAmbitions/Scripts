lis = [3, 2, 5, 1, 10, 7, 8, 6, 4, 9]
lis = sorted(lis)
def binary_search(arr, target):
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end)//2
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return start
print(binary_search(lis, 4))
    