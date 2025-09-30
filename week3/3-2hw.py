pre = list(map(int, input().split()))
inorder = list(map(int, input().split()))
def treeh(pt, it):
    if not(pt) or not(it):
        return 0
    root = pt[0]
    rootind = it.index(root)
    lit = it[:rootind]
    rit = it[rootind+1:]

    lpr = pt[1 : 1 + len(lit)]
    rpr = pt[1 + len(lit):]
    return max(treeh(lpr, lit), treeh(rpr, rit)) + 1
print(treeh(pre, inorder))
    
