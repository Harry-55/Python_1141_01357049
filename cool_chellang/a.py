n, m = list(map(int,(input().split(" "))))
while m:
    arr = []
    cin = input().split(" ")
    arr = list(map(int, cin))
    target = 0
    ans = int(input())
    for i in range(n):
        if arr[i] == ans:
            target = 1
            ans = i
            break
    if target:
        print(ans)
    else:
        print("-1")
    m-=1
