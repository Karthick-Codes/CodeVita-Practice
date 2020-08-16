lexical order

for _ in range(int(input())):
    p=input()
    w=input()
    l=[]
    for i in w:
        l.append(p.index(i))
    l.sort()
    for i in l:
        print(p[i],end="") 

Program Logic :
	rearrange the S based on P 
Program Explaination:
	find the index of all S letters from P.
	index append in a list
	list is sorted
	print sorted index element from P
