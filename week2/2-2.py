n = int(input())
number = input().split(" ")
print(f"排序前的數列: {' '.join(number)}")
number = [int(x) for x in number]
number.sort()
number = [str(x) for x in number]
print(f"排序後的數列: {' '.join(number)} ")
