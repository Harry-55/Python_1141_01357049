n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]
ops = input().strip()

def rotate90():
    global mat
    new = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new[j][n - 1 - i] = mat[i][j]
    mat = new

def hor():
    global mat
    for i in range(n // 2):
        mat[i], mat[n - 1 - i] = mat[n - 1 - i], mat[i]

def ver(): 
    global mat
    for i in range(n):
        for j in range(n // 2):
            mat[i][j], mat[i][n - 1 - j] = mat[i][n - 1 - j], mat[i][j]

for op in ops:
    if op == 'R':
        rotate90()
    elif op == 'H':
        hor()
    elif op == 'V':
        ver()

for row in mat:
    print(*row)
