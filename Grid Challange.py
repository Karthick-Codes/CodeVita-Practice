1.Grid Challange
-------------------

for _ in range(int(input())):
    last=[]
    state=[]
    for i in range(int(input())):
        al=list(input())
        al.sort()
        if i==0:
            last=al
        else:
            for k in range(len(last)):
                if al[k]<last[k]:
                    state.append(False)
            last=al

    if len(state)==0:
        print("YES")
    else:
        print("NO")

Input

1
5
ebacd
fghij
olmkn
trpqs
xywuv

Output
YES

Program Logic 
	we can rearrange columns within a row.
	if rows and columns in alphabetical order -->YES
	else --> NO

Program Explaination:
	for every testcase grid input, first row will be sorted and directly assign to last[].
	further rows sorted and all the columns check with previous row corresponding columns.
		if al[k]<last[k] then false append to state[]
		after comparison of all elements al[] assigned to last[]
	at the end if length of state is equal to ZERO print YES
	otherwise print NO.
