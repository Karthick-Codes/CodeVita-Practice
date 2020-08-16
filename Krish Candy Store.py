Krish Candy Store.

for _ in range(int(input())):
    n=int(input())
    l=sorted(list(map(int,input().split())))
    sums=[]
    t=0
    while(len(l)>2):
        x=l[0]
        y=l[1]
        t=x+y
        l.remove(x)
        l.remove(y)
        sums.append(t)
        l.append(t)
        l.sort()
    sums.append(sum(l))
    print(sum(sums)) 

Input :
1
4
1 2 3 4 

Output 
19

Program Logic:
	find minimum time for joint all boxes into single box.(at a time only two box)
Program Detailed Explanation:
	store N boxes in l[] and sort in ascending order.
	sums is another list to store every sum value.
	while loop run until l[] has greater than 2 value.
		add first two element in the list. and remove the value from l[]
		append sum value to sum[] and l[]
		sort l[].
	finally sum remain values in l[] and append in sums[]
	print sum values sums[].
	
