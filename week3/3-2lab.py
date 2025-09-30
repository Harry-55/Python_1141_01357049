def check(n, arr):
    index = 1
    stack = []
    for i in arr :
        while index <= n and (not stack or stack[-1] != i):
            stack.append(index)
            index+=1
        if stack and stack[-1] == i:
            stack.pop()
        else: 
            return False
    return True
    
c = True
while True:
    if not c:
        break
    n = int(input())
    if n == 0:
        break
    while True:
        line = input().strip()
        if line == "0":
            c = False
            break
        lst = list(map(int, line.split()))
        if check(n, lst):
            print("YES")
        else:
            print("NO")

