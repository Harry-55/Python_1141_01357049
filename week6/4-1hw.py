def cola_recursive(a: int, borrow: bool = True) -> int:
    if a < 3:
        return 1 if borrow and a == 2 else 0

    new = a // 3  
    remain = a % 3 + new  
    return new + cola_recursive(remain, borrow)


while True:
    try:
        n = int(input())
    except EOFError:
        break

    total = n + cola_recursive(n, borrow=True)
    print(total)
