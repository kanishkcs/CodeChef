# Codechef-CU-assignment-Queries-in-an-array-

#code
#please like share subscribe the channel


from sys import stdin, stdout

import os
import io

n, q = stdin.readline().split()

n = int(n)

q = int(q)

arr = [int(n) for n in input().split()]

for i in range(q):

    l, r, x = stdin.readline().split()

    l = int(l)

    r = int(r)

    x = int(x)

    c = -1

    m = l-1

    n = r-1

    while m <= n:

        mid = ((m+n)//2)

        if arr[mid] >= x:

            c = mid

            n = mid-1

        else:

            m = mid+1

    if c == -1:

        stdout.write(str("0")+'\n')

    else:

        stdout.write(str(r-c)+'\n')
