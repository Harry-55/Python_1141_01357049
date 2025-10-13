while True:
    try:
        a = int(input())
    except EOFError:
        break 
    ans = a
    while a > 2:
        new = a // 3
        ans += new
        a -= new * 3
        a += new
    if a == 2:
        ans += 1
    print(ans)
