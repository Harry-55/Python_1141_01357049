n = int(input())
for i in range(n):
    str = input()
    strdict = dict()
    for j in str:
        if j in strdict :
            strdict[j]+=1
        else :
            strdict.update({j:1})
    max = 0
    char = None
    for key, value in strdict.items():
        if value > max :
            max = value
            char = key
    print(char)