def solve(a, b):
    carry = 0
    ans = 0
    while(a or b):
        carry = (a%10 + b%10 + carry)//10
        ans += carry
        a//=10
        b//=10
    if ans == 1:
        print(str(ans) + " carry operation.")
    elif ans:
        print(str(ans) + " carry operations.")
    else :
        print("No carry operation.")


while True:
    a, b = map(int, input().split())
    if not(a or b):
        break
    solve(a, b)
