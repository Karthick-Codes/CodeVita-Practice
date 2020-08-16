import itertools
n=int(input())
s=input()
k=list(set(s))
a=list(itertools.combinations(k,2))
l=[]
for i in a:
    t=""
    x,y=i[0],i[1]
    pre=""
    for k in range(len(s)):
        if s[k] in i:
            if t=="":
                pre=s[k]
                t+=s[k]
            else:
                if s[k]!=pre:
                    pre=s[k]
                    t+=s[k]
                else:
                    break
    
    else:
        l.append(len(t))
if len(l):
	print(max(l))
else:
	print(0)
            
Sample Input
10
beabeefeab

Sample Output
5

Program Logic:
	find maximum length of alternative characters (only two alphabets) from the original string.
Program Detailed Expalanatioin:
	find unique characters from given input
	store all the combinaton of unique characters .
	iterate all combination, append characters in t if only characters are in combination and current character should not come again if suppose break the loop and
	move to the next combination.
	finally print the max length of t.
