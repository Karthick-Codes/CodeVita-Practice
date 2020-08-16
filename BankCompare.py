Bank Compare

import math
loanAmount=int(input())
Tot=int(input())
ans=[]
for _ in range(2):
    x=int(input())
    TotPay=0
    for i in range(x):
        year,interest=map(float,input().split())
        year=int(year)
        div=math.pow((1+interest),(year*12))
        pay=((loanAmount*interest)/1-(1/div))
        TotPay+=pay
    ans.append(TotPay)
if ans[0]<ans[1]:
    print("Bank A")
else:
    print("Bank B")

Sample Input :

10000
20
3
5 9.5
10 9.6
5 8.5
3
10 6.9
5 8.5
5 7.9

Sample Output :

Bank B

Program Logic :
	find minimum emi amount based on  print Bank A or Bank B
Program Explaination :
	by using EMI formula problem can be solved.
	calculate EMI bank A and append in ans[]
	calculate EMI bank B and append in ans[].
	compare both value if ans[0] less than ans[1] then print Bank A
	else print Bank B.
