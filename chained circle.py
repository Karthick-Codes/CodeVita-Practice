test=int(input())
for i in range(test):
    res=[]
    x=int(input())
    l=list(input().lower().split())
    fl=[]
    for j in range(len(l)):
        for k in range(len(l)):
            if l[k][0]==l[j][-1]:
                fl.append([l[k],l[j]])
    for i in fl:
        cu=i[0]
        la=i[1]
        pre=i[0][-1]
        ans=[cu,la]
        ind=1
        for j in range(len(l)):
            if l[j]!=cu and l[j]!=la:
                if l[j][0]==pre:
                    pre=l[j][-1]
                    #print(l[j],end=" ")
                    ans.insert(ind,l[j])
                    ind+=1
                
        #print(ans)
        if(ans[-2][-1]==ans[-1][0]):
            res.append(len(ans))
        #print(res)
    if len(res):
        if max(res)>=len(l):
            print(1)
        else:
            print(0)
    else:
        print(0) 
         
Input
2
3
abc bcd cdf
4
ab bc cd da

Output
0
1
        
 Program Logic:
		find a given array elements are form a chained circle (i.e) last character of current element is the first character of next element.

Program Detailed Explanation:
	
	2nd for loop find out all circle first and last elements and store it in a fl[[]  i.e [abc ,cbe]
	3 rd iterate fl[] and find out  last charecter and first character match as per condition update previous value every time.
	if possible then append length of a the list elements.
	if len(res) is equal to original length then print 1 otherwise print 0.
