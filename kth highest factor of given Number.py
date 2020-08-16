import math
N,k=map(int,input().split())
sq=math.sqrt(N)
e=int(sq)+1
fact=[1,N]
for i in range(2,e+1):
    if N%i==0:
        fact.append(i)
        fact.append(N//i)
fact=list(set(fact))
fact.sort()
if len(fact)>=k:
	print(fact[-k])
else:
	print(-1)
    

Program Logic:
	find kth highest factor of given Number.

Program Detailed Expalanation:
	find all factors. print kth value from last if  not print -1.
