n = input()
n = int(n)
if n <= 0:
    print("輸入錯誤")
else:
    num = 1
    x = n * (n+1) // 2
    s = len(str(x))
    for i in range(n):
        for j in range(i+1):
            print(f"{num:>{s}}", end = " ")
            num += 1  
        print()