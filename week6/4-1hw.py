def GCD(a, b):
    if b == 0:
        return a
    return GCD(b, a%b)
def solve(a):
    ans = 0
    for i in range(1, a):
        for j in range(i+1, a+1):
            ans += GCD(i, j)
    return ans
while True:
    a = int(input())
    if a == 0:
        break
    print(solve(a))

