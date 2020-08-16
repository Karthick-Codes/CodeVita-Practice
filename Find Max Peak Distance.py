Find Peak Distance

n=int(input())
l=list(map(int,input().split()))
Fans=[]
last=0
Lans=[]
Llast=0
for i in range(1,n-1):
    pre=l[i-1]
    nxt=l[i+1]
    # having magnitude higher than both its neighbours
    if(l[i]>pre and l[i]>nxt):
        dist=i-last
        Fans.append(dist)
        last=i
    # having magnitude lower than both its neighbours
    if(l[i]<pre and l[i]<nxt):
        ldist=i-Llast
        Lans.append(ldist)
        Llast=i
Fans=Fans[1:]
Lans=Lans[1:]
if(len(Fans)>=1):
    Fanswer=max(Fans)
else:
    Fanswer=0
if(len(Lans)>=1):
    Lanswer=max(Lans)
else:
    Lanswer=0
print(max(Fanswer,Lanswer)) 

Input:
	7
	2 5 4 7 9 6 1
Output:
	3

Program Logic:
	find peak indices , find consecutive maximum distance
	peak: higher than both neighbour,
	      lower than both neighbour

Program Explanation:
	initialy last=0
	if both left and right values less then, dist=i-last, append dist in Fans list
		update last as i
	similary for both neighbour higher

	then from 1 st element of Fans ,Lans because which is not a distance
	find  max (max(list))  
