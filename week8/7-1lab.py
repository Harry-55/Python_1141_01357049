def quick_sort(arr, l, r):
    if l >= r: return
    mid = (l + r) >> 1
    pivot = arr[mid]
    i, j = l, r
    if i <= j:
        while(arr[i] < pivot):
            i+=1
        while(arr[j] > pivot):
            j-=1
        if i <= j:
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
            i += 1
            j -= 1
    quick_sort(arr, l, j)
    quick_sort(arr, i , r)

num = list(map(int, input().split()))
quick_sort(num, 0, len(num) - 1)
print(*num)