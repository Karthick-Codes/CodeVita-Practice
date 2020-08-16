 Counting Rock Samples

n,r=map(int,input().split())
l=list(map(int,input().split()))
for _ in range(r):
    s,e=map(int,input().split())
    cnt=0
    for i in l:
        if i>=s and i<=e:
            cnt+=1
    print(cnt,end=" ")

Input: 
10 2
345 604 321 433 704 470 808 718 517 811
300 350
400 700

Output: 
2 4

Program Logic:
	print the count of rock samples in the given range.
Program Explanation:
	store rock samples in a l[].
	for loop run upto number of ranges(R).
		intialize count as ZERO.
		if element of l  in range of s and e then increase count by 1.
		end of second for loop print count value.
	
