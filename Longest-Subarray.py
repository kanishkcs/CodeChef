import sys
t = int(input())


subarrays =[]

def longests(arr):

    result = []
    conitnue = []
    length_of_result = []

    for arry_items in arr:
        if arry_items % 2 == 0:
            conitnue.append(arry_items)
            if arry_items == arr[-1]:
                result.append(conitnue)
        else:
            result.append(conitnue)
            conitnue = []


    for a in range(0, len(result)):
        length_of_result.append(len(result[a]))
        pass

    return max(length_of_result)

while t > 0:
    n = int(input())
    arr = list(map(int, input().split()))
    subarrays.append(longests(arr))
    t -= 1

for ans in subarrays:
    print(ans)
