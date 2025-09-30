n, m = map(int, input().split())
A = set(map(int, input().split(" ")))
B = set(map(int, input().split(" ")))

C = A & B
print(len(C))
if C :
    print(" ".join(map(str, sorted(C))))