nearest larger number

from itertools import permutations
a,b=input().split()
li=list(a)
b=int(b)
ans=list(permutations(li))
fi=[]
for i in ans:
    n=""
    for e in i:
        n=n+str(e)
    fi.append(int(n))
fi.sort()
for i in fi:
    if i>b:
        print(i)
        break
else:
    print(-1)   

Sample Input: 

459 500 

Sample Output: 
549

Program Logic:
	find nearest larger number than b by interchange the digits.

Program Detailed Expalanation:
	find permutation for A and sort it in ascending order.
	iterate all permutation value if greater than b print value and break 
	suppose none value is break the loop print -1.
