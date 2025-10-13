reflect = {
    'A' : 'A',
    'E' : '3',
    'H' : 'H',
    'I' : 'I',
    'J' : 'L',
    'L' : 'J',
    'M' : 'M',
    'O' : 'O',
    'S' : '2',
    'T' : 'T',
    'U' : 'U',
    'V' : 'V',
    'W' : 'W',
    'X' : 'X',
    'Y' : 'Y',
    'Z' : '5',
    '1' : '1',
    '2' : 'S',
    '3' : 'E',
    '5' : 'Z',
    '8' : '8',
    '0' : 'O'
}

def getAns( a ) -> int:
    n = len(a)
    mir = True
    pal = True
    for i in range(n//2 + 1):
        l = a[i]
        r = a[n - 1 - i]
        if l != r: pal = False
        if l not in reflect or r not in reflect:
            mir = False
        else :
            if reflect[l] != r: mir = False
        if not mir and not pal:
            break
    if mir and pal : return 0
    elif mir : return 1
    elif pal : return 2
    return 3
            
    
    

try:
    while True:
        uwu = input().strip()
        result = getAns(uwu)
        print( f"{uwu} -- is a mirrored palindrome." if result == 0 else f"{uwu} -- is a mirrored string." if result == 1 else f"{uwu} -- is a regular palindrome." if result == 2 else f"{uwu} -- is not a palindrome." )

except EOFError:
    pass