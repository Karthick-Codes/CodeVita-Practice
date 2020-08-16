Question 2

l=list(map(int,input().split()))
index=[]
m=max(l)
ind=l.index(m)
index.append(ind)
l[ind]=0
while(len(l)):
    x=max(l)
    i=l.index(x)
    l[i]=0
    if (all( ((ind-1)!=i) and ((ind+1)!=i) for ind in index) ):
        m+=x
        index.append(i)
    if ( all( (e==0) for e in l) ):
        break
print(m) 

Program Logic:
	find maximum value but not adjacent.
Program Detailed Explanation:
	find max of list and index value store it in another list 
	check every time max value index is not adjacent of already taken index.
	when all the elements of list is zero break print current m value..
